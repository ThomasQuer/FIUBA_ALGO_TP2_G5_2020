import json
import facebook
import requests
import re
import base64

def obtener_nombre_usuario(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Devuelve un diccionario con {id: id del usuario,
        nombre: nombre del usuario}
    """
    diccionario_nombres = graph.get_object(id='me')
    print('El ID del usuario es:', diccionario_nombres['id'], 'y el nombre es:', diccionario_nombres['name'])
    return diccionario_nombres['id']

def visualizar_nombre_usuario(diccionario_nombres):
    """
    PRE:
        Diccionario debe ser de la forma: {id: , nombre:}
    POST:
        visualiza el nombre y el id del usuario
    """
    print('El ID del usuario es:', diccionario_nombres['id'], 'y el nombre es:', diccionario_nombres['name'])


def dar_like_posteo(graph, id_posteo):
    """
    PRE:
        token debe ser un string, la llave de acceso
        id_posteo debe ser un string con el id del posteo
    POST:
        genera un like en el posteo enviado
    """
    # con token de pagina desde app empresarial
    # ej: putlike = graph.put_like(object_id = id_posteo)
    # id_posteo = USERID_POSTID
    darlike = graph.put_like(object_id="105249781540470_106764151389033")

    if darlike:
        print("Se ha dado like al posteo.")

    else:
        print("Hubo un problema, intente nuevamente.")


def leer_posteo(graph, id_usuario):
    """
    PRE:
       id_usuario debe ser un string con el id del usuario
    POST:
        Solicita id del posteo e imprime el mensaje del posteo seleccionado
    """
    id_posteo = input('Ingrese el id del posteo: ')
    identificador = str(str(id_usuario) + '_' + id_posteo)
    # token utilizado el de app comercial #id = 'USERID_POSTID'
    # ej: identificador = 101662381858155_101493071875086
    posteo = graph.get_object(
        id=identificador, fields='message, attachments{description}'
    )
    print(posteo['message'])


def subir_posteo(graph):
    """
    PRE:
        id pagina debe ser un string
    POST:
        permite escribir un texto y lo publica en una pagina
    """
    # con token de pagina desde app empresarial
    mensaje = input('Ingrese el mensaje del posteo: ')
    # posteo = graph.put_object(parent_object = id_pagina,
    # connection_name ="feed", message = mensaje)
    posteo = graph.put_object(
        parent_object="105249781540470",
        connection_name="feed", message=mensaje
    )
    if posteo:
        print("Su posteo número: " + posteo['id'] + " ha sido publicado.")

    else:
        print("Hubo un problema, intente nuevamente.")


def subir_foto(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        solicita al usuario que indique la ubicación de una foto y la publica
    """
    # opcion 1 error:
    # camino_imagen = input("Ingrese la ubicación de la imagen: ")
    # archivo = open(camino_imagen, 'rb')
    # graph.put_photo(archivo, 'me/photos')
    # facebook.GraphAPIError: (#200) This endpoint is deprecated since
    # the required permission publish_actions is deprecated


def actualizar_posteo(token, id_posteo):
    """
    PRE:
        token debe ser un string, la llave de acceso
        id_posteo debe ser un string con el id del posteo
    POST:
        Devuelve un diccionario con todas las caracteristicas
        del posteo seleccionado
    """


def listar_seguidores(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Devuelve una lista con los seguidores
    """
    return lista_seguidores


def listar_amigos(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Devuelve una lista con los amigos
    """
    amigos = graph.get_object('me', fields='friends')
    # Excepcion: Solo los amigos que han instalado esta aplicación estarán
    # en la versión 2.0 o superior de la API.
    print(
        "La cantidad de amigos que tienes es: " +
        str(amigos['friends']['summary']['total_count'])
    )
    # ver como obtener nombre de los que tienen la api


def seguir_usuario(token, usuario_id):
    """
    PRE:
        token debe ser un string, la llave de acceso
        usuario_id debe ser un string que indique el id del usuario
    POST:
        sigue al usuario seleccionado
    """


def solicitar_amistad(token, usuario_id):
    """
    PRE:
        token debe ser un string, la llave de acceso
        usuario_id debe ser un string que indique el id del usuario
    POST:
        solicita amistad al usuario seleccionado
    """
    return

"""
def enviar_mensaje_usuario(nombre_usuario):
    PRE:
        nombre_usuario debe ser un string que indique el nombre de usuario
        de la cuenta de facebook.
    POST:
       envia un mensaje a usuario posteriormente ingresado.

    # seteo de variables para fbchat.Client (sino genera un error)
    fbchat._util.USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    ]
    fbchat._state.FB_DTSG_REGEX = re.compile(
        r'"name":"fb_dtsg","value":"(.*?)"'
    )

    # nombre_usuario = 'crux.bot.1'
    contraseña = input("Ingrese su contraseña: ")
    cliente = fbchat.Client(nombre_usuario, contraseña)
    nombre_amigo = input("Ingrese el nombre y apellido del amigo: ")
    amigos = cliente.searchForUsers(nombre_amigo)
    amigo = amigos[0]
    mensaje = input("Ingrese el mensaje a enviar: ")
    envio = cliente.sendMessage(mensaje, thread_id=amigo.uid)
    if envio:
        print("Se ha enviado correctamente el mensaje.")

    else:
        print("Hubo un problema, intente nuevamente.")

"""
def actualizar_datos_perfil(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Muestra los atributos que pueden ser moodificados,
        permite al usuario seleccionar uno
        y modificarlo.
    """


def ver_ultimos_posts(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        muestra tus últimos posts
    """
    lista_de_posts = requests.get(
        "https://graph.facebook.com/v9.0/me?fields=posts&access_token=" +
        token
    )
    lista_de_posts_json = lista_de_posts.json()
    print(lista_de_posts_json)

###ARRANCA PARTE DE INSTAGRAM

def obtener_informacion_cuenta_ig(token_empresarial):
"""
PRE:
    token debe ser un string, la llave de accesso
POST:
    trae un diccionario "informacion_usuario_ig" con la informacion de la cuenta de ig, con la siguiente estructura:
    {follower_count:,
    follows_count:,
    ig_id:, 
    media_count:, 
    prefile_picture_url:, 
    media:, 
    recentrly_searched_hashtags:, 
    id:}
"""
    id_pagina = requests.get("https://graph.facebook.com/v9.0/me/accounts?access_token="+
                         token_empresarial).json()['data'][2]['id']
    try:
        id_instagram =requests.get('https://graph.facebook.com/v3.2/'+
                                id_pagina+'?fields=instagram_business_account&access_token='+
                                token_empresarial).json()['instagram_business_account']['id']
    except:
        raise TypeError("Verificar que la página seleccionada tenga asociada correctamente una cuenta de instagram") 
                        
    informacion_usuario_ig = requests.get("https://graph.facebook.com/v9.0/"+id_instagram+
                                   "?fields=biography%2Cfollowers_count%2Cfollows_count%2Cig_id%2Cmedia_count%2Cprofile_picture_url%2Cmedia%2Crecently_searched_hashtags%2Cstories%2Ctags&access_token="+
                                   token_empresarial).json()
    return informacion_usuario_ig

def seleccionar_atributo_para_mostrar(informacion_usuario_ig):
"""
PRE:
    "informacion_usuario_ig" debe ser un diccionario con la siguiente estructura:
    {follower_count:,
    follows_count:,
    ig_id:, 
    media_count:, 
    prefile_picture_url:, 
    media:, 
    recentrly_searched_hashtags:, 
    id:}
POST:
    Selecciona uno de los atributos del diccionario y devuelve ese atributo seleccionado
"""   
    atributos_usuario = list(informacion_usuario_ig.keys())
    print('los siguientes atributos disponibles son los siguientes:')
    print(atributos_usuario)
    atributo_seleccionado = str(input('Escriba que atributo quiere visualizar:'))
    while atributo_seleccionado not in atributos_usuario:
        atributo_seleccionado = str(input('ERROR, escriba correcamente que atributo quiere visualizar:'))
    return atributo_seleccionado

def mostrar_informacion_basica_ig(informacion_usuario_ig, atributo_seleccionado):
"""
PRE:
    "informacion_usuario_ig" debe ser un diccionario con la siguiente estructura:
    {follower_count:,
    follows_count:,
    ig_id:, 
    media_count:, 
    prefile_picture_url:, 
    media:, 
    recentrly_searched_hashtags:, 
    id:}
    atributo_selecionado debe ser un str con el atributo que se desea visualizar
POST:
    visualiza la informacion del atributo seleccionado
"""       
    print('el valor del atributo {0} es: {1}'.format(atributo_seleccionado, informacion_usuario[atributo_seleccionado]))

def obtener_post_publicados_ig(token_empresarial, id_instagram):
"""
PRE:
    token debe ser un string, la llave de accesso
    id_instragram debe ser un string con la identificacion del usuario de instagram
POST:
    Devuelve un diccionario con la informacion de los post realizados por el usuario, con la siguiente estructura:
    {media_url:,
    permalink:,
    caption:, 
    comments_count:, 
    ig_id:, 
    like_count:, 
    media_type:, 
    owner:
    id:}
    atributo_selecionado debe ser un str con el atributo que se desea visualizar
"""       
    post_publicados = requests.get("https://graph.facebook.com/v9.0/"+id_instagram+"/media?fields=media_url,permalink,caption,comments_count,ig_id,like_count,media_type,owner, comments&access_token="+token_empresarial).json()
    return post_publicados['data']

def visualizar_post_publicados_ig(post_publicados):
"""
PRE:
    post_publicados debe ser un diccionarion la informacion de los post realizados por el usuario, con la siguiente estructura:
    {media_url:, co
    permalink:,
    caption:, 
    comments_count:, 
    ig_id:, 
    like_count:, 
    media_type:, 
    owner:
    id:}
POST:
    Visualiza los post publicados de la siguiente manera:
        numero del posteo, id del posteo, link del posteo, cantidad de likes y cantidad comentarios
"""      
    print('A continuación se muestra información de los posts publicados:')
    for post in range(len(post_publicados)):
        print('post N {0}: ID: {4}, link: {1} , tiene {2} likes y {3} comentarios.'.
        format(post, post_publicados[post]['permalink'], post_publicados[post]['like_count'], post_publicados[post]['like_count'], post_publicados[post]['id'] ))

def validacion_entero(valor, rango):
"""
PRE:
    valor es lo que se validara como un entero
POST:
    intenta transformar el valor en entero. De no ser posible pide al usuario que vuelva a entrar un valor hasta que cumpla con este requerimiento
"""             
    while not valor.isdigit() or int(numero_de_post_seleccionado) < 0 or int(numero_de_post_seleccionado) > rango:: 
        valor = input("seleciones un número entero")
    valor = int(valor)
    return valor

def obtener_id_post_ig(post_publicados):
"""
PRE:
    post_publicados debe ser un diccionarion la informacion de los post realizados por el usuario, con la siguiente estructura:
    {media_url:,
    permalink:,
    caption:, 
    comments_count:, 
    ig_id:, 
    like_count:, 
    media_type:, 
    owner:
    id:}
POST:
    para el numero de post seleccionado, devuelve el id del mismo.
"""         
    visualizar_post_publicados_ig(post_publicados)
    numero_de_post_seleccionado = input('seleccion el numero del post del cual quiere obtener el ID: ')
    numero_de_post_seleccionado = validacion_entero(numero_de_post_seleccionado, len(post_publicados))
    id_post = post_publicados[numero_de_post_seleccionado]['id']
    return id_post

def obtener_informacion_post_ig(id_post, token_empresarial):
"""
PRE:
    token debe ser un string, la llave de accesso
    id_post debe ser un str, el id del post que se quiere obtener informacion
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
        {numero comentario: [id comentario, texto comentrario], 
        ...}
"""     
    informacion_post_seleccionado = requests.get("https://graph.facebook.com/v9.0/"+
                            media_id+"?fields=like_count,id,comments_count,caption,ig_id,media_type,owner,media_url,permalink,comments&access_token="
                            +token_empresarial).json()
    diccionario_comentarios = {}
    for comentario in range(len(informacion_post_seleccionado['comments']['data'])):
        diccionario_comentarios[comentario] = [informacion_post_seleccionado['comments']['data'][comentario]['text'],
                                            informacion_post_seleccionado['comments']['data'][comentario]['id']]
    return informacion_post_seleccionado, diccionario_comentarios

def visualizar_informacion_post_seleccionado_ig(informacion_post_seleccionado):
"""
PRE:
    informacion_post_seleccionado debe ser un diccionario con la siguiente estructura:
        likes = informacion_post_seleccionado['like_count']
        motivo = informacion_post_seleccionado['caption']
        tipo = informacion_post_seleccionado['media_type']
        propietario = informacion_post_seleccionado['owner']['id']
        url_imagen = informacion_post_seleccionado['media_url']
        url_post = informacion_post_seleccionado['permalink']
        cantidad_comentarios  = informacion_post_seleccionado['comments_count']

    diccionario_comentarios debe ser un diccionario con la siguiente estrucutra:
        {numero comentario: [id comentario, texto comentrario], 
        ...}
POST:
    Visualiza la informacion de un post
""" 
    diccionario_informacion_post = {'likes': informacion_post_seleccionado['like_count'],
    "motivo": informacion_post_seleccionado['caption'],
    "tipo": informacion_post_seleccionado['media_type'],
    "propietario": informacion_post_seleccionado['owner']['id'],
    "url_imagen": informacion_post_seleccionado['media_url'],
    "url_post": informacion_post_seleccionado['permalink'],
    "cantidad_comentarios": informacion_post_seleccionado['comments_count']}
    print('la informacion disponible para visualizar es la siguiente: {} '.format(diccionario_informacion_post.keys()))
    elemento_visualizar = input('seleccione un elemento para visualizar')
    while elemento_visualizar not in diccionario_informacion_post.keys():
        elemento_visualizar = input('ERROR, selecione un elemento para visualizar')
    print('el elemento seleccionado es el "{}" y su valor es {}'.format(elemento_visualizar, diccionario_informacio[elemento_visualizar]))

def visualizar_comentarios_post_ig(diccionario_comentarios):
"""
PRE:

    diccionario_comentarios debe ser un diccionario con la siguiente estrucutra:
        {numero comentario: [id comentario, texto comentrario], 
        ...}
POST:
    Visualiza los comentarios de un post y pregunta si el usuario desea responder a alguno.
""" 
    for elementos in diccionario_comentarios.keys():
        print('Comentario N.{}: {}'.format(elementos, diccionario_comentarios[elementos][0]))
    
def obtener_id_comentario(diccionario_comentarios):
"""
PRE:

    diccionario_comentarios debe ser un diccionario con la siguiente estrucutra:
        {numero comentario: [id comentario, texto comentrario], 
        ...}
POST:
    obtiene el ID de un comentario en particular
""" 
    numero_comentario = input('seleccione el numero de comentario:')
    numero_comentario = validacion_entero(numero_comentario, len(diccionario_comentarios))
    id_comentario = diccionario_comentarios[str(numero_comentario)][1]
    return id_comentario

def borrar_comentario(id_comentario, token_empresarial):
"""
PRE:
    id_comentario debe ser un str con el ID del comentario que se desea borrar
    token debe ser un string, la llave de accesso
POST:
    Borra el comentario seleccionado
"""     
    try:
        requests.delete("https://graph.facebook.com/v9.0/"+id_comentario+"?access_token="+token_empresarial).json()
    except:
        raise TypeError("no se pudo completar la operación") 

def responder_comentario(id_comentario, token_empresarial):
"""
PRE:
    id_comentario debe ser un str con el ID del comentario que se desea borrar
    token debe ser un string, la llave de accesso
POST:
    responde el comentario seleccionado
"""     
    texto_respuesta = input('ingrese el texto de la respuesta para comentario seleccionado')
    texto_respuesta = texto_respuesta.replace(' ','%20')
    try:
        requests.post("https://graph.facebook.com/v9.0/"+comentario_id+"/replies?message="+texto_respuesta+"&access_token="+token_empresarial).json()
    except:
        raise TypeError("No se pudo completar la operación") 

def visualizar_insights_post(token_empresarial, id_post):
    """
PRE:
    token debe ser un string, la llave de accesso
    id_post debe ser un str, el id del post que se quiere obtener informacion
POST: Visualiza los insights del post y explica que significa cada uno
"""
insights = ['impressions', 'reach', 'engagement', 'saved']

    for elementos in insights:
        insights_media = requests.get("https://graph.facebook.com/v9.0/"+
                                    id_post+"/insights?metric="+
                                    elementos+"&access_token="+
                                    token_empresarial).json()
        print('el atritbuto "{0}" del post es {1} ({2})'.format(insights_media['data'][0]['title'],
                                                    insights_media['data'][0]['values'][0]['value'], 
                                                    insights_media['data'][0]['description']))
def buscar_hashtag(token_empresarial, id_instagram):
"""
PRE:
    token debe ser un string, la llave de accesso
    id_instragram debe ser un string con la identificacion del usuario de instagram
POST:
    busca el hashtag ingresado y devuelve un diccionario de la forma:
    {numero hashtag: [url_post, id_post], 
    ...}
"""  
    hashtag = str(input('ingrese el hashtag que desea buscar'))
    try:
        id_hashtag = requests.get("https://graph.facebook.com/v9.0/ig_hashtag_search?user_id="+
                                id_instagram+"&q="+hashtag+"&access_token="+token_empresarial).json()['data'][0]['id']
    except: 
        raise TypeError("No existe ese Hashtag (Pruebe sin # y sin espacios)") 
    #Buscando informacion de ese hashtag
    info_hashtag = requests.get("https://graph.facebook.com/v9.0/"+id_hashtag+
                                "/recent_media?fields=media_url,media_type,like_count,permalink&user_id="+
                                id_instagram+"&access_token="+token_empresarial).json()['data']
    diccionario_posts_hashtag = {}
    for post in range(len(info_hashtag)):
        diccionario_posts_hashtag[post] = [info_hashtag[post]['permalink'], info_hashtag[post]['id']]
    return diccionario_posts_hashtag
 
def visualizar_post_hashtag(diccionario_posts_hashtag):
"""
PRE:
    diccionario_posts_hashtag debe ser un diccionario de la forma:
    {numero hashtag: [url_post, id_post], 
    ...}
POST:
    visualiza los post con el hashtag seleccionado
"""                                        
    for elemento in diccionario_posts_hashtag.keys():
        print('Post N.{}, url:{}, post ID:{}'.format(elemento, diccionario_posts_hashtag[elemento][0], diccionario_posts_hashtag[elemento][1]))


def subir_imagen_servidor():
"""
POST:
    Sube una foto que se encuentre en la carpeta donde se este ejecutando el codigo al servido imgBB para asi obtener un url y poder subirlo a instragram luego.
"""  
    key_imgBB = 'b50256d3abf80d9465fbbf0cbb39004d'
    nombre_imagen = input('ingrese el nombre de la imagen:')
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

def postear_imagen_ig(token_empresarial, id_instagram):
"""
PRE:
    token debe ser un string, la llave de accesso
    id_instragram debe ser un string con la identificacion del usuario de instagram
POST:
    Postea una foto en instagram 
"""  
    url_imagen_subida = subir_imagen_servidor()
    motivo = input('ingrese el texto que quiere publicar con la foto')
    id_para_posteo = requests.post("https://graph.facebook.com/"+id_instagram+"/media?image_url="+url_imagen_subida+"&caption="+motivo+"&access_token="+token_empresarial).json()['id']
    requests.post("https://graph.facebook.com/"+id_instagram+"/media_publish?creation_id="+id_para_posteo+"&access_token="+token_empresarial)

def main():
    # token: ver de hacer funcion para seleccion de empresarial,
    # consumidor o pagina.
    # Consumidor - Crux Bot Pagina
    token_consumidor = 'EAADBGgWWrIABAJz0wqMNm3rluqU4V3YWtVL9X2XUbkkJ8CZCQ0nkZBZCQXwCv9fTlDv6ZArYYEGapv2RRHqqDaawRqCqm0dE01sw8Qrs8ZBvlZCac53aorVQCBUpXhPrcFY7a2HPv1vpsZBxZBy0Q4TGY8BmwQreVF9rdAdbWUxStwZDZD'
    # empreserial
    token_empresarial = 'EAAPQlFICfVYBACZCXpJYPVzynYOUPhiTlrTIwsYKvV7bleDOtBluceWcmE7d7qFCCSPwfZC1huzvBZCUB7vr2NyJ6M4NGGkoi3tWIqz21tPwlXEzoiNi9xyTqygAb32qZA0nuv2ndEnUs8BuKwVEzqsJjydPHXoZBpJebYZCxJ0gZDZD'
    graph = facebook.GraphAPI(token_empresarial)
    subir_posteo(graph)


if __name__ == "__main__":
    main()

