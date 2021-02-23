import json
import facebook
import requests
import re
import base64


def mostrar_menu():
    """
    POST:
        Visualiza en pantalla el menú de opciones disponibles.
    """
    var = (
        "************* ACCIONES DISPONIBLES *************\n\n"
        "1. Ver posteos hechos.\n"
        "2. Darle like a un posteo.\n"
        "3. Actualizar un posteo.\n"
        "4. Subir un nuevo posteo, sólo escritura.\n"
        "5. Subir un nuevo posteo con imagen incluida.\n"
        "6. Mostrar cantidad de amigos.\n"
        "7. Actualizar datos de la página.\n"
        "8. Comentar una publicación.\n\n"

        "Elige una opción a ejecutar.\n"
    )

    return var


def obtener_nombre_usuario():
    """
    POST:
        Devuelve un diccionario con {id: id del usuario,
        nombre: nombre del usuario}
    """
    token = seleccion_token('consumidor_cuenta', token_solo=True)
    dicc = requests.get(f"https://graph.facebook.com/v9.0/me?fields=id%2Cname&access_token={token}")
    dicc_json = dicc.json()
    return (dicc_json)


def ver_posts():
    """
    POST:
        muestra todos los posteos hechos y devuelve una lista: id_publicacion
        la misma contiene las id de los posts ubicadas en la posicion del
        número de post.
    """
    auxiliar = []
    id_publicacion = []
    posts_lista = []
    token = seleccion_token('consumidor_pagina', token_solo=True)
    lista_de_posts = requests.get(f"https://graph.facebook.com/v9.0/me?fields=posts&access_token={token}")
    lista_de_posts_json = lista_de_posts.json()
    contador = 0
    for i in lista_de_posts_json['posts']['data']:
        if contador < len(lista_de_posts_json['posts']['data']):
            auxiliar.append(i)
            id_publicacion.append(auxiliar[contador]['id'])
            try:
                fecha = limpiar_fecha(auxiliar[contador]['created_time'])
                linea = (
                    "*********************************************\n" +
                    f"Post Nº: {contador} \n\nPublicado el:\n {fecha}" +
                    "\n\nMensaje:\n " + auxiliar[contador]['message'] + "\n")

            except KeyError:
                fecha = limpiar_fecha(auxiliar[contador]['created_time'])
                linea = (
                    "*********************************************\n" +
                    f"Post Nº: {contador} \n\nPublicado el:\n {fecha}" +
                    "\n\nMensaje:\n" + auxiliar[contador]['story'] + "\n")
            
            posts_lista.append(linea)
        contador += 1

    return id_publicacion, posts_lista


def dar_like_posteo(eleccion):
    """
    POST:
        genera un like en el posteo enviado
    """
    combo = ver_posts()
    id_publicacion = combo[0]
    # Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    # Se solicita id del posteo a dar like
    eleccion = list(eleccion)
    eleccion.remove("N")
    eleccion.remove(":")
    eleccion = "".join(eleccion)
    identificador = generar_identificador(int(eleccion), id_publicacion)
    # Se utiliza la api para dar like al posteo y se imprime por pantalla el resultado
    darlike = graph.put_like(object_id=identificador)
    if darlike:
        linea = "Se ha dado like al posteo."

    else:
        linea = "Hubo un problema, intente nuevamente."

    return linea


def actualizar_posteo(dato):
    """
    POST:
        Devuelve un diccionario con todas las caracteristicas
        del posteo seleccionado
    """
    token, graph = seleccion_token("empresarial_pagina")
    combo = ver_posts()
    id_publicacion = combo[0]
    dato = dato.split(" ")
    eleccion = dato[0]
    dato[0] = ""
    eleccion = list(eleccion)
    eleccion.remove("N")
    eleccion.remove("-")
    eleccion = "".join(eleccion)
    mensaje = " ".join(dato)
    identificador = generar_identificador(int(eleccion), id_publicacion)
    actualizacion = graph.put_object(parent_object=identificador, connection_name='', message=mensaje)
    if actualizacion:
        linea = "¡Modificación exitosa!"
    else:
        linea = "Hubo un problema, intente nuevamente."

    return linea


def subir_posteo(mensaje):
    """
    POST:
        permite escribir un texto y lo publica en una pagina la cual se solicita el id al usuario.
    """
    # Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    mensaje = list(mensaje)
    mensaje.remove("M")
    mensaje.remove(":")
    mensaje = "".join(mensaje)
    id_pagina = 105249781540470
    posteo = graph.put_object(parent_object=id_pagina, connection_name="feed", message=mensaje)
    if posteo:
        linea = "El posteo ha sido publicado con éxito."
    else:
        linea = "Hubo un problema, intente nuevamente."

    return linea


def subir_foto(dato): #Crea un bucle terrible en messenger y relentiza al bot
    """
    POST:
        Solicita al usuario que indique la ubicación de una foto y la publica en la pagina de Crux.
    """
    # El posteo foto es en la pagina de Crux:
    # con token empresa_cuenta y consumidor_cuenta : facebook.GraphAPIError: (#200) This endpoint is deprecated since the required permission publish_actions is deprecated
    # con token consumidor_pagina : facebook.GraphAPIError: (#200) The permission(s) pages_read_engagement,pages_manage_posts are not available. It could because either they are deprecated or need to be approved by App Review.
    token, graph = seleccion_token("empresarial_pagina")
    dato = dato.split(",")
    camino_imagen = dato[0]
    dato[0] = ""
    mensaje = " ".join(dato)
    posteo = graph.put_photo(image=open(camino_imagen, 'rb'), message=mensaje)
    if posteo:
        linea = "Su posteo fue realizado con éxito."
    else:
        linea = "Hubo un problema, intente nuevamente."

    return linea


def listar_amigos():  # Devuelve la cantidad de amigos.
    """
    POST:
        Devuelve una lista con los amigos.
    """
    token, graph = seleccion_token("consumidor_cuenta")
    amigos = graph.get_object('me', fields='friends')
    # Excepcion: Solo los amigos que han instalado esta aplicación estarán
    # en la versión 2.0 o superior de la API.
    print(
        "La cantidad de amigos que tienes es: " +
        str(amigos['friends']['summary']['total_count'])
    )
    # ver como obtener nombre de los que tienen la api
    # lista_amigos = request.get(f"https://graph.facebook.com/v9.0/{friend-list-id}?access_token={token}")


def actualizar_datos_pagina():
    """
    POST:
        Muestra los atributos de la pagina que pueden ser moodificados,
        permite al usuario seleccionar uno y modificarlo.
    """
    token = seleccion_token('empresarial_pagina', token_solo=True)
    campos_lista = ['name', 'about', 'website', 'bio']
    campos_string = ", ".join(campos_lista)
    datos = requests.get(f"https://graph.facebook.com/me?fields={campos_string}&access_token={token}")
    # Muestra campos y pide seleccion de uno a modificar
    eleccion = input(
        'Los campos actuales son:\n'
        '1.Name\n2.About\n3.Website\n\n¿Cuál desea actualizar?: ')

    while not eleccion.isnumeric() or int(eleccion) < 1 or int(eleccion) > 3:
        eleccion = input("Opción no válida. Por favor vuelva a ingresar: ")
  
    for i in range(len(campos_lista)):
        if int(eleccion)-1 == i:
            campo = campos_lista[i]

    print(f'El campo {campo} contiene: {datos.json()[campo]}')
    modificacion = input("Ingrese la modificación a realizar: ")
    accion = requests.post(f'https://graph.facebook.com/me?{campo}={modificacion}&access_token={token}')
    if accion.json()['success']:
        print('Se han realizado los cambios.')
    else:
        print('Ha surgido un problema, intente nuevamente.')


def comentar_objeto():
    """
    POST:
        permite escribir un comentario en el objeto cuyo id es solicitado al usuario.
    """
    token, graph = seleccion_token("empresarial_pagina")
    id_publicacion = ver_posts()
    eleccion = input("Indique el número del post que desea comentar: ")
    while not eleccion.isnumeric() or int(eleccion) < 0 or int(eleccion) > (len(id_publicacion)-1):
        eleccion = input("Opción no válida. Por favor vuelva a ingresar: ")
    mensaje = input("Ingrese el mensaje a comentar: ")
    identificador = generar_identificador(int(eleccion), id_publicacion)
    comentario = graph.put_object(parent_object=identificador, connection_name='comments', message=mensaje)
    if comentario:
        print("Su comentario ha sido exitoso.")
    else:
        print("Ha ocurrido un error, intente nuevamente.")

# funciones para otras funciones
def seleccion_token(tipo_token, token_solo=False):
    """
    PRE:
        necesita un string indicando el tipo de token a devolver. 
        Opciones: empresarial_cuenta, empresarial_pagina, consumidor_cuenta, consumidor_pagina.
        Si token_solo se especifica True, solo devuelve el token.
    POST:
        devuelve un string con el token segun tipo de aplicación y el objeto graph 
        del tipo 'facebook.GraphAPI' cuando token_solo = False.
    """
    if tipo_token == "empresarial_cuenta":
        token = 'EAAPQlFICfVYBAHQTuF4SA84zmZBZCWZAdJH7qIeAvL6JRYY2gZCsIwwhua67QHtVYJFCOpa3sLpN2lwkwddmIqy8ZCfejRaeReWcExZCtDzaGW6ifnWrwXlD1DZAS36T5pyYSRujfLxNcNDZBZBeA9PqZAVOzHGNkeYvAhbSKUvDsbyAZDZD'
    elif tipo_token == "empresarial_pagina":
        token = 'EAAPQlFICfVYBAGksuFWsbDomJ5DFFYuL4MQ5gzIKYDXVfsJRzCk9uoNK9hZCcnDSdiDiDz5Y4HFvO1G7r63Jnx1sZA5bj3cT9pQVAeyUdMUaVd6VqX7BPMztN8jYDrqdIN7fIeYc0ZBwEKZB9ZCZCryTZAtmXFrJua76OPJZC8bYLwZDZD'
    elif tipo_token == "consumidor_cuenta":
        token = 'EAADBGgWWrIABAOCBW4316mP4J3D5iqZAcEQ48wKBrftnoOFnb452KPO4wdlfpN5MAWu8h3DGyPdqZCLMjUgH9A6nJLZASMnnxQZCHwELkM47biGgc3WJbkXLZAxOMknHblPJLvnZCsgwtfqoagitQaY0gHpRoxDbp2o56xWDZBDNwZDZD'
    elif tipo_token == "consumidor_pagina":
        token = 'EAADBGgWWrIABAMXUFHlijThaTleKULX1yFhNPZCilHQipyAzdMZBir14OI8C981hIsyvpiidZBR3FpZAC2XoAkZAgvZCaf4UFf2PsfG3bzKBYPGWEZAnS9JhIKKZCZAYNL1TaEzjJbOzucssde7kny7zz1pttFZBtX9oUbobmT9GRRfwZDZD'
    graph = facebook.GraphAPI(token)
    if not token_solo:
        return token, graph
    else:
        return token


def generar_identificador(numero_posteo, id_publicacion):
    """
    PRE:
        numero_posteo debe ser un int
        id_publicacion debe ser una lista con las id de las publicaciones
        ubicadas en la posicion del número de post.
    POST:
        devuelve el identificador del objeto en cuestion como IDUSUARIO_IDPOST.
    """

    for i in range(len(id_publicacion)):
        if numero_posteo == i:
            identificador = id_publicacion[i]

    return identificador


# de uso interno
def generar_token_extendido():
    """
    POST:
        devuelve por pantalla el token extendido.
    """
    id_empresarial = "1073760379764054"
    app_secret_empresarial = "713e642a5b1713edd95a3318fcc53d9c"
    id_comercial = "212317507071104"
    app_secret_comercial = "76993c5b1107a3771fc4bf8b7cd977aa"
    token_corto = input("Ingrese el token de corto período: ")
    tipo_app = int(input("Ingrese si 1 si es app empresarial o 2 si es app comercial: "))

    if tipo_app == 1:
        id_app = id_empresarial
        app_secret = app_secret_empresarial
    elif tipo_app == 2:
        id_app = id_comercial
        app_secret = app_secret_comercial

    token_extendido = requests.get(f"https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={id_app}&client_secret={app_secret}&fb_exchange_token={token_corto}")
    print("Token extendido: " + token_extendido.json()['access_token'])


def generar_token_pagina():
    """
    POST:
        devuelve por pantalla token de pagina. Si el token de la app en la función seleccion_token()
        es de larga vida, el token de pagina no caduca
    """

    tipo = int(input("Ingrese 1-empresarial_cuenta o 2-consumidor_cuenta: "))
    if tipo == 1:
        tipo_token = "empresarial_cuenta"
    elif tipo == 2:
        tipo_token = "consumidor_cuenta"
    token = seleccion_token(tipo_token)
    token_pagina = requests.get(f"https://graph.facebook.com/v9.0/105249781540470?fields=access_token&access_token={token}")
    print("El token pagina es: " + token_pagina.json()['access_token'])


def limpiar_fecha(dato):
    """
    PRE:
        dato debe ser un str.
    POST:
        Devuelve un str: formato_fecha. El mismo contiene los valores de dato
        reacomodados de la siguiente forma: "dd/mm/aa  HH:MM:SS"
    """
    fecha = list(dato)
    tiempo = []
    anio = []
    mes = []
    dia = []

    for i in range(len(fecha)):
        if i >= 11 and i <= 18:
            tiempo.append(fecha[i])
        elif i >= 0 and i <= 3:
            anio.append(fecha[i])
        elif i >= 5 and i <= 6:
            mes.append(fecha[i])
        elif i >= 8 and i <= 9:
            dia.append(fecha[i])

    tiempo = "".join(tiempo)
    anio = "".join(anio)
    mes = "".join(mes)
    dia = "".join(dia)

    formato_fecha = f"{dia}/{mes}/{anio}  {tiempo}"

    return formato_fecha



