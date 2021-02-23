import json
import facebook
import requests
import re
import base64


def mostrar_menu():
    """
    POST:
        Devuelve el menú de acciones, str.
    """
    menu = (
        "************* ACCIONES DISPONIBLES *************\n\n"
        "1. Ver posteos hechos.\n"
        "2. Darle like a un posteo.\n"
        "3. Actualizar un posteo.\n"
        "4. Subir un nuevo posteo, sólo escritura.\n"
        "5. Función desactivada.\n"
        "6. Mostrar cantidad de amigos.\n"
        "7. Actualizar datos de la página.\n"
        "8. Comentar una publicación.\n"
        "9. Mostrar la cantidad de seguidores.\n"
        "10. Mostrar las páginas seguidas.\n\n"

        "Elige una opción a ejecutar.\n"
    )

    return menu


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
        Devuelve una tupla compuesta de id_publicacion, una lista con las ids ubicadas
        en la posición del número de post, y posts_lista, una lista con las publicaciones
        hechas enumeradas según más reciente.
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
    PRE:
        eleccion debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
    """
    tupla = ver_posts()
    id_publicacion = tupla[0]
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
    PRE:
        dato debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
    """
    token, graph = seleccion_token("empresarial_pagina")
    tupla = ver_posts()
    id_publicacion = tupla[0]
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
    PRE:
        mensaje debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
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


def subir_foto(dato):  # Crea un bucle terrible en messenger y relentiza al bot. Función desactivada en messenger
    """
    PRE:
        dato debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
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
        Devuelve un string con la respuesta de la acción.
    """
    token, graph = seleccion_token("consumidor_cuenta")
    amigos = graph.get_object('me', fields='friends')
    # Excepcion: Solo los amigos que han instalado esta aplicación estarán
    # en la versión 2.0 o superior de la API.
    linea = "La cantidad de amigos que tienes es: " + str(amigos['friends']['summary']['total_count'])
    # ver como obtener nombre de los que tienen la api
    # lista_amigos = request.get(f"https://graph.facebook.com/v9.0/{friend-list-id}?access_token={token}")

    return linea


def actualizar_datos_pagina(dato):
    """
    PRE:
        dato debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
    """
    token = seleccion_token('empresarial_pagina', token_solo=True)
    campos_lista = ['name', 'about', 'website', 'bio']
    campos_string = ", ".join(campos_lista)
    datos = requests.get(f"https://graph.facebook.com/me?fields={campos_string}&access_token={token}")
    dato = dato.split(" ")
    eleccion = dato[0]
    dato[0] = ""
    eleccion = list(eleccion)
    eleccion.remove("A")
    eleccion.remove(":")
    eleccion = "".join(eleccion)
    modificacion = " ".join(dato)

    for i in range(len(campos_lista)):
        if int(eleccion)-1 == i:
            campo = campos_lista[i]

    accion = requests.post(f'https://graph.facebook.com/me?{campo}={modificacion}&access_token={token}')
    if accion.json()['success']:
        linea = 'Se han realizado los cambios.'
    else:
        linea = 'Ha surgido un problema, intente nuevamente.'

    return linea


def comentar_objeto(dato):
    """
    PRE:
        dato debe ser un string
    POST:
        Devuelve un string con la respuesta de la acción.
    """
    token, graph = seleccion_token("empresarial_pagina")
    id_publicacion = ver_posts()
    tupla = ver_posts()
    id_publicacion = tupla[0]
    dato = dato.split(" ")
    eleccion = dato[0]
    dato[0] = ""
    eleccion = list(eleccion)
    eleccion.remove("C")
    eleccion.remove("-")
    eleccion = "".join(eleccion)
    mensaje = " ".join(dato)
    identificador = generar_identificador(int(eleccion), id_publicacion)
    comentario = graph.put_object(parent_object=identificador, connection_name='comments', message=mensaje)
    if comentario:
        linea = "Su comentario ha sido exitoso."
    else:
        linea = "Ha ocurrido un error, intente nuevamente."

    return linea


def listar_seguidores():
    """
    POST:
        Muestra la cantidad de seguidores de la pagina de crux.
    """
    token = seleccion_token("consumidor_pagina", token_solo = True)
    seguidores = requests.get(f"https://graph.facebook.com/v9.0/105249781540470?fields=followers_count&access_token={token}").json()
    if seguidores:
        cantidad_seguidores = seguidores['followers_count']
    linea = f'La cantidad de seguidores es: {cantidad_seguidores}'

    return linea


def listar_likes():
    """
    POST:
        devuelve una lista con el nombre en string de las paginas likeadas por el usuario.
    """
    token, graph = seleccion_token('consumidor_cuenta')
    likes = graph.get_connections(id="me", connection_name="likes")
    lista_likes = ['Las páginas seguidas son:\n']
    for i in likes['data']:
        lista_likes.append(i['name'])

    lista_likes = "\n".join(lista_likes)

    return lista_likes


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



