import json
import facebook
import requests
import re
import base64

TOKEN_CUENTA_EMPRESARIAL = 'EAAPQlFICfVYBAHQTuF4SA84zmZBZCWZAdJH7qIeAvL6JRYY2gZCsIwwhua67QHtVYJFCOpa3sLpN2lwkwddmIqy8ZCfejRaeReWcExZCtDzaGW6ifnWrwXlD1DZAS36T5pyYSRujfLxNcNDZBZBeA9PqZAVOzHGNkeYvAhbSKUvDsbyAZDZD'
TOKEN_PAGINA_EMPRESARIAL = 'EAAPQlFICfVYBAGksuFWsbDomJ5DFFYuL4MQ5gzIKYDXVfsJRzCk9uoNK9hZCcnDSdiDiDz5Y4HFvO1G7r63Jnx1sZA5bj3cT9pQVAeyUdMUaVd6VqX7BPMztN8jYDrqdIN7fIeYc0ZBwEKZB9ZCZCryTZAtmXFrJua76OPJZC8bYLwZDZD'
TOKEN_CUENTA_CONSUMIDOR = 'EAADBGgWWrIABAOCBW4316mP4J3D5iqZAcEQ48wKBrftnoOFnb452KPO4wdlfpN5MAWu8h3DGyPdqZCLMjUgH9A6nJLZASMnnxQZCHwELkM47biGgc3WJbkXLZAxOMknHblPJLvnZCsgwtfqoagitQaY0gHpRoxDbp2o56xWDZBDNwZDZD'
TOKEN_PAGINA_CONSUMIDOR = 'EAADBGgWWrIABAMXUFHlijThaTleKULX1yFhNPZCilHQipyAzdMZBir14OI8C981hIsyvpiidZBR3FpZAC2XoAkZAgvZCaf4UFf2PsfG3bzKBYPGWEZAnS9JhIKKZCZAYNL1TaEzjJbOzucssde7kny7zz1pttFZBtX9oUbobmT9GRRfwZDZD'


def mostrar_menu():
    """
    POST:
        Visualiza en pantalla el menú de opciones disponibles.
    """
    print(
        "************* ACCIONES DISPONIBLES *************\n\n"
        "FACEBOOK:\n\n"
        "1. Ver posteos hechos.\n"
        "2. Darle like a un posteo.\n"
        "3. Actualizar un posteo.\n"
        "4. Subir un nuevo posteo, sólo escritura.\n"
        "5. Subir un nuevo posteo con imagen incluida.\n"
        "6. Mostrar cantidad de amigos.\n"
        "7. Actualizar datos de la página.\n"
        "8. Comentar una publicación.\n"
        "9. Mostrar la cantidad de seguidores.\n"
        "10. Mostrar las páginas seguidas.\n\n"
        "INSTAGRAM:\n\n"
        "11. Mostrar información de la cuenta.\n"
        "12. Ver posteos hechos.\n"
        "13. Ver comentarios.\n"
        "14. Comentar un posteo.\n"
        "15. Responder un comentario.\n"
        "16. Borrar un comentario.\n"
        "17. Mostrar alcance de un posteo específico.\n"
        "18. Buscar un hashtag.\n"
        "19. Subir un nuevo posteo.\n\n"
        "Elige una opción a ejecutar.\n"
    )


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


def ver_posts():
    """
    POST:
        muestra todos los posteos hechos y devuelve una lista: id_publicacion
        la misma contiene las id de los posts ubicadas en la posicion del
        número de post.
    """
    auxiliar = []
    id_publicacion = []
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
                print(
                    "*********************************************\n" +
                    f"Post Nº: {contador} \n\nPublicado el:\n {fecha}" +
                    "\n\nMensaje:\n " + auxiliar[contador]['message'] + "\n")

            except KeyError:
                fecha = limpiar_fecha(auxiliar[contador]['created_time'])
                print(
                    "*********************************************\n" +
                    f"Post Nº: {contador} \n\nPublicado el:\n {fecha}" +
                    "\n\nMensaje:\n" + auxiliar[contador]['story'] + "\n")
        contador += 1

    return id_publicacion


def dar_like_posteo():
    """
    POST:
        genera un like en el posteo enviado e informa el resultado de la acción.
    """
    id_publicacion = ver_posts()
    eleccion = input("Indique el número de post al que desea darle like: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)
    # Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    # Se solicita id del posteo a dar like
    identificador = obtener_id_post(int(eleccion), id_publicacion)
    # Se utiliza la api para dar like al posteo y se imprime por pantalla el resultado
    darlike = graph.put_like(object_id=identificador)
    if darlike:
        print("Se ha dado like al posteo.")

    else:
        print("Hubo un problema, intente nuevamente.")


def actualizar_posteo():
    """
    POST:
        Genera una modificación en el número de post indicado e informa el resultado de la acción.
    """
    token, graph = seleccion_token("empresarial_pagina")
    id_publicacion = ver_posts()
    eleccion = input("Indique el número del post que desea actualizar: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)
    identificador = obtener_id_post(int(eleccion), id_publicacion)
    mensaje = input('Ingrese el mensaje para modificar al posteo: ')
    actualizacion = graph.put_object(parent_object=identificador, connection_name='', message=mensaje)
    if actualizacion:
        print("¡Modificación exitosa!")
    else:
        print("Hubo un problema, intente nuevamente.")


def subir_posteo():
    """
    POST:
        permite escribir un texto y lo publica en la página de Crux
        e informa el resultado de la acción.
    """
    # Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    mensaje = input('Ingrese el mensaje del posteo: ')
    id_pagina = 105249781540470
    posteo = graph.put_object(parent_object=id_pagina, connection_name="feed", message=mensaje)
    if posteo:
        print("El posteo ha sido publicado con éxito.")
    else:
        print("Hubo un problema, intente nuevamente.")


def subir_foto():
    """
    POST:
        Solicita al usuario que indique la ubicación de una foto y la publica en la página de Crux
        e informa el resultado de la acción.
    """
    # El posteo foto es en la pagina de Crux:
    # con token empresa_cuenta y consumidor_cuenta : facebook.GraphAPIError: (#200) This endpoint is deprecated since the required permission publish_actions is deprecated
    # con token consumidor_pagina : facebook.GraphAPIError: (#200) The permission(s) pages_read_engagement,pages_manage_posts are not available. It could because either they are deprecated or need to be approved by App Review.
    token, graph = seleccion_token("empresarial_pagina")
    camino_imagen = input(
        "Ingrese la ubicación de la imagen + el nombre del mismo acompañado de la extensión .jpg, "
        "por ej. C:\GIT\ALGOI\imagen.jpg : ")  # ej "C:\GIT\ALGOI\crux.jpg"
    mensaje = input("Ingrese el mensaje de la foto: ")
    posteo = graph.put_photo(image=open(camino_imagen, 'rb'), message=mensaje)
    if posteo:
        print("Su posteo fue realizado con éxito.")
    else:
        print("Hubo un problema, intente nuevamente.")


def listar_amigos():  # Devuelve la cantidad de amigos.
    """
    POST:
        Devuelve un string con la cantidad de amigos.
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
        permite al usuario seleccionar uno y modificarlo. Al finalizar,
        devuelve el resultado de la acción.
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
        Al finalizar, devuelve el resultado de la acción.
    """
    token, graph = seleccion_token("empresarial_pagina")
    id_publicacion = ver_posts()
    eleccion = input("Indique el número del post que desea comentar: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)
    mensaje = input("Ingrese el mensaje a comentar: ")
    identificador = obtener_id_post(int(eleccion), id_publicacion)
    comentario = graph.put_object(parent_object=identificador, connection_name='comments', message=mensaje)
    if comentario:
        print("Su comentario ha sido exitoso.")
    else:
        print("Ha ocurrido un error, intente nuevamente.")


def listar_seguidores():
    """
    POST:
        Muestra la cantidad de seguidores de la pagina de crux.
    """
    token = seleccion_token("consumidor_pagina", token_solo=True)
    seguidores = requests.get(f"https://graph.facebook.com/v9.0/105249781540470?fields=followers_count&access_token={token}").json()
    if seguidores:
        cantidad_seguidores = seguidores['followers_count']
    print(f'La cantidad de seguidores es: {cantidad_seguidores}')


def listar_likes():
    """
    POST:
        devuelve una lista con el nombre en string de las paginas likeadas por el usuario.
    """
    token, graph = seleccion_token('consumidor_cuenta')
    likes = graph.get_connections(id="me", connection_name="likes")
    print('Las páginas seguidas son:')
    for i in likes['data']:
        print(i['name'])


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
        token = TOKEN_CUENTA_EMPRESARIAL
    elif tipo_token == "empresarial_pagina":
        token = TOKEN_PAGINA_EMPRESARIAL
    elif tipo_token == "consumidor_cuenta":
        token = TOKEN_CUENTA_CONSUMIDOR
    elif tipo_token == "consumidor_pagina":
        token = TOKEN_PAGINA_CONSUMIDOR
    graph = facebook.GraphAPI(token)
    if not token_solo:
        return token, graph
    else:
        return token


def obtener_id_post(numero_posteo, id_publicacion):
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


### ARRANCA PARTE DE INSTAGRAM

# Funciones para otras funciones
def obtener_informacion_cuenta_ig():
    """
    POST:
        trae un diccionario "informacion_usuario_ig" con la informacion de la
        cuenta de ig,con la siguiente estructura:
        {follower_count:, follows_count:, ig_id:, media_count:,
        profile_picture_url:, media:, recentrly_searched_hashtags:, id: }
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    id_pagina = requests.get(
        "https://graph.facebook.com/v9.0/me/accounts?access_token=" +
        token_empresarial).json()['data'][2]['id']
    try:
        id_instagram = requests.get(
            'https://graph.facebook.com/v3.2/' +
            id_pagina + '?fields=instagram_business_account&access_token=' +
            token_empresarial).json()['instagram_business_account']['id']
    except:
        raise TypeError("Verificar que la página seleccionada tenga asociada correctamente una cuenta de instagram")

    informacion_usuario_ig = requests.get(
        "https://graph.facebook.com/v9.0/" + id_instagram +
        "?fields=biography%2Cfollowers_count%2Cfollows_count%2Cig_id%2Cmedia_count%2Cprofile_picture_url%2Cmedia%2Crecently_searched_hashtags%2Cstories%2Ctags&access_token=" +
        token_empresarial).json()
    
    return informacion_usuario_ig


def obtener_post_publicados_ig():
    """
    POST:
        Devuelve un diccionario con la informacion de los post realizados por el usuario, con la siguiente estructura:
        {media_url:, permalink:, caption:, comments_count:, ig_id:, like_count:, media_type:, owner: id: }
        atributo_selecionado debe ser un str con el atributo que se desea visualizar
    """
    informacion = obtener_informacion_cuenta_ig()
    id_instagram = informacion['id']
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    post_publicados = requests.get(
        "https://graph.facebook.com/v9.0/" + id_instagram +
        "/media?fields=media_url,permalink,caption,comments_count,ig_id,like_count,media_type,owner, comments&access_token="
        + token_empresarial).json()

    return post_publicados['data']


def obtener_informacion_post_ig():
    """
    POST:
        obtiene informacion de un post particular, con la estructura de un diccionario, de la forma de:
            likes = informacion_post_seleccionado['like_count']
            motivo = informacion_post_seleccionado['caption']
            tipo = informacion_post_seleccionado['media_type']
            propietario = informacion_post_seleccionado['owner']['id']
            url_imagen = informacion_post_seleccionado['media_url']
            url_post = informacion_post_seleccionado['permalink']
            cantidad_comentarios  = informacion_post_seleccionado['comments_count']
            ademas se obtiene un diccionario con los comentarios del post de la forma de:
            {numero comentario: [id comentario, texto comentrario], ...}
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    id_publicacion = visualizar_post_publicados_ig()
    eleccion = input("Indique el número de post: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)
    id_post = obtener_id_post(int(eleccion), id_publicacion)

    informacion_post_seleccionado = requests.get(
        "https://graph.facebook.com/v9.0/" + id_post +
        "?fields=like_count,id,comments_count,caption,ig_id,media_type,owner,media_url,permalink,comments&access_token="
        + token_empresarial).json()
    diccionario_comentarios = {}

    try:
        for comentario in range(len(informacion_post_seleccionado['comments']['data'])):
            diccionario_comentarios[comentario] = (
                [informacion_post_seleccionado['comments']['data'][comentario]['text'],
                informacion_post_seleccionado['comments']['data'][comentario]['id']])
    except KeyError:
        diccionario_comentarios = {}

    return informacion_post_seleccionado, diccionario_comentarios


def obtener_id_comentario(diccionario_comentarios):
    """
    PRE:
        diccionario_comentarios debe ser un dict no vacío.
    POST:
        obtiene el ID de un comentario en particular
    """

    for elementos in diccionario_comentarios.keys():
        print('Comentario N.{}: {}'.format(elementos, diccionario_comentarios[elementos][0]))

    numero_comentario = input('seleccione el numero de comentario:')
    numero_comentario = validar_rango(numero_comentario, len(diccionario_comentarios)-1)
    id_comentario = diccionario_comentarios[int(numero_comentario)][1]

    return id_comentario


def validar_rango(valor, rango):
    while not valor.isnumeric() or int(valor) < 0 or int(valor) > rango:
        valor = input("Opción no válida. Por favor vuelva a ingresar: ")

    return valor


def verificar_existencia_comentario(diccionario_comentarios):
    """
    PRE:
        diccionario_comentarios debe ser un dict.
    POST:
        Si dicciomario_comentarios se encuentra
        vacío devolverá False, de lo contrario, True.
    """
    existe = False
    if diccionario_comentarios != {}:
        existe = True

    return existe


def subir_imagen_servidor():
    """
    POST:
        Sube una foto que se encuentre en la carpeta donde se este ejecutando el codigo
        al servido imgBB para asi obtener un url y poder subirlo a instragram luego.
    """
    key_imgBB = 'b50256d3abf80d9465fbbf0cbb39004d'
    nombre_imagen = input('ingrese el nombre de la imagen acompañada de su extensión: ')
    try:
        with open(nombre_imagen, "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": key_imgBB,
                "image": base64.b64encode(file.read()),
            }
        res = requests.post(url, payload)
        return res.json()['data']['url']
    except:
        raise TypeError("ERROR, Verificar que el nombre de la imagen este bien escrito, que se haya puesto la extension de imagen y que la misma se encuentre en la carpeta donde esta programa .py funcionando.")


# Funciones de acciones
def mostrar_informacion_basica():
    """
    POST:
        visualiza la informacion del atributo seleccionado
    """
    informacion_usuario_ig = obtener_informacion_cuenta_ig()
    atributos_usuario = list(informacion_usuario_ig.keys())
    print(
        "Usted tiene {0} seguidores.\nSigue a {1} cuentas.\n"
        "Tiene un total de {2} publicaciones realizadas.\nLa URL de su imagen es: {3}".format(
            informacion_usuario_ig['followers_count'], informacion_usuario_ig['follows_count'],
            informacion_usuario_ig['media_count'], informacion_usuario_ig['profile_picture_url']))


def visualizar_post_publicados_ig():
    """
    POST:
        Visualiza los post publicados de la siguiente manera:
        numero del posteo, id del posteo, link del posteo, cantidad de likes y cantidad comentarios
    """
    lista_id_post = []
    post_publicados = obtener_post_publicados_ig()
    print('A continuación se muestra información de los posts publicados:')
    for post in range(len(post_publicados)):
        print(
            "***********************************************************\n" +
            'post Nº {0}:\n\nMensaje: {4}\n\nlink: {1} , tiene {2} likes y {3} comentarios.\n'.
            format(post, post_publicados[post]['permalink'], post_publicados[post]['like_count'], post_publicados[post]['comments_count'], post_publicados[post]['caption']))
        lista_id_post.append(post_publicados[post]['id'])

    return lista_id_post


def realizar_comentario():
    """
    POST:
        Crea un nuevo comentario en el post seleccionado.
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    id_publicacion = visualizar_post_publicados_ig()
    eleccion = input("Indique el número de post en el que desea realizar un nuevo comentario: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)
    id_comentario = obtener_id_post(int(eleccion), id_publicacion)
    texto_respuesta = input('ingrese el texto para realizar el comentario: ')
    texto_respuesta = texto_respuesta.replace(' ', '%20')
    responder = requests.post(
        "https://graph.facebook.com/v9.0/" + id_comentario + "/comments?message=" + texto_respuesta +
        "&access_token=" + token_empresarial).json()
    if responder:
        print("El comentario ha sido realizado con éxito.")
    else:
        print("Ups! Algo ha salido mal, no se pudo completar la acción.")


def responder_comentario():
    """
    POST:
        Si existe un comentario en el post seleccionado responderá en el mismo
        el mensaje ingresado por el usuario. De no existir, lo informará.
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    tupla = obtener_informacion_post_ig()
    diccionario_comentarios = tupla[1]
    existe = verificar_existencia_comentario(diccionario_comentarios)
    if existe:
        id_comentario = obtener_id_comentario(diccionario_comentarios)
        texto_respuesta = input('ingrese el texto de la respuesta para comentario seleccionado: ')
        texto_respuesta = texto_respuesta.replace(' ', '%20')
        responder = requests.post(
            "https://graph.facebook.com/v9.0/" + id_comentario + "/replies?message=" + texto_respuesta +
            "&access_token=" + token_empresarial).json()
        if responder:
            print("El comentario ha sido realizado con éxito.")
        else:
            print("Ups! Algo ha salido mal, no se pudo completar la acción.")
    
    else:
        print("El post seleccionado no contiene comentarios existentes en los cuáles responder.")


def borrar_comentario():
    """
    POST:
        Si existen comentarios en el post seleccionado los mostrará y preguntará
        al usuario el que quiera eliminar. De no existir, lo informará.
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    tupla = obtener_informacion_post_ig()
    diccionario_comentarios = tupla[1]
    existe = verificar_existencia_comentario(diccionario_comentarios)
    if existe:
        id_comentario = obtener_id_comentario(diccionario_comentarios)
        borrar = requests.delete(
            "https://graph.facebook.com/v9.0/" + id_comentario + "?access_token=" + token_empresarial).json()
        if borrar:
            print("El comentario ha sido eliminado con éxito.")
        else:
            print("Ups! Algo ha salido mal, no se pudo completar la acción.")

    else:
        print("El post seleccionado no contiene comentarios existentes para poder cumplir la solicitud.")


def visualizar_insights_post():
    """
    POST:
        Visualiza los insights del post y explica que significa cada uno
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    id_publicacion = visualizar_post_publicados_ig()
    eleccion = input("Indique el número de post del cuál quiere obtener información: ")
    eleccion = validar_rango(eleccion, len(id_publicacion)-1)

    id_post = obtener_id_post(int(eleccion), id_publicacion)
    insights = ['impressions', 'reach', 'engagement', 'saved']

    for elementos in insights:
        insights_media = requests.get(
            "https://graph.facebook.com/v9.0/" + id_post + "/insights?metric=" +
            elementos + "&access_token=" + token_empresarial).json()
        print('el atributo "{0}" del post es {1} ({2})'.format(
            insights_media['data'][0]['title'], insights_media['data'][0]['values'][0]['value'],
            insights_media['data'][0]['description']))


def visualizar_post_hashtag():
    """
    POST:
        busca el hashtag ingresado y devuelve un diccionario de la forma:
        {numero hashtag: [url_post, id_post], ...} y visualiza los post
        con el hashtag seleccionado
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    informacion = obtener_informacion_cuenta_ig()
    id_instagram = informacion['id']
    hashtag = input('ingrese el hashtag que desea buscar: ')
    try:
        id_hashtag = requests.get(
            "https://graph.facebook.com/v9.0/ig_hashtag_search?user_id=" +
            id_instagram + "&q=" + hashtag + "&access_token=" + token_empresarial).json()['data'][0]['id']
    except KeyError:
        print("No existe ese Hashtag (Pruebe sin # y sin espacios)")
    # Buscando informacion de ese hashtag
    info_hashtag = requests.get(
        "https://graph.facebook.com/v9.0/" + id_hashtag +
        "/recent_media?fields=media_url,media_type,like_count,permalink&user_id=" +
        id_instagram + "&access_token=" + token_empresarial).json()['data']
    diccionario_posts_hashtag = {}
    for post in range(len(info_hashtag)):
        diccionario_posts_hashtag[post] = [info_hashtag[post]['permalink'], info_hashtag[post]['id']]

    for elemento in diccionario_posts_hashtag.keys():
        print('Post N.{}, url:{}, post ID:{}'.format(
            elemento, diccionario_posts_hashtag[elemento][0], diccionario_posts_hashtag[elemento][1]))


def postear_imagen_ig():
    """
    POST:
        Postea una foto en instagram
    """
    token_empresarial = seleccion_token('empresarial_cuenta', token_solo=True)
    informacion = obtener_informacion_cuenta_ig()
    id_instagram = informacion['id']
    url_imagen_subida = subir_imagen_servidor()
    motivo = input('ingrese el texto que quiere publicar con la foto: ')
    id_para_posteo = requests.post(
        "https://graph.facebook.com/" + id_instagram + "/media?image_url="+ url_imagen_subida +
        "&caption=" + motivo + "&access_token="+token_empresarial).json()['id']
    posteo = requests.post(
        "https://graph.facebook.com/" + id_instagram + "/media_publish?creation_id=" +
        id_para_posteo + "&access_token=" + token_empresarial)

    if posteo:
        print("La imagen se ha subido con éxito.")

    else:
        print("Ups! Algo ha salido mal.")


#main
def main():
    # token: en función seleccion_token

if __name__ == "__main__":
    main()

