import json
import facebook
import requests
import re


def obtener_nombre_usuario(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Devuelve un diccionario con {id: id del usuario,
        nombre: nombre del usuario}
    """
    dicc = requests.get(
        "https://graph.facebook.com/v9.0/me?fields=id%2Cname&access_token=" +
        token
    )
    dicc_json = dicc.json()
    visualizar_nombre_usuario(dicc_json)
    return (dicc_json)

def visualizar_nombre_usuario(diccionario_nombres):
    """
    PRE:
        Diccionario debe ser de la forma: {id: , nombre:}
    POST:
        visualiza el nombre y el id del usuario
    """
    print('El ID del usuario es:', diccionario_nombres['id'], 'y el nombre es:', diccionario_nombres['name'])

def buscar_usuario(graph, id_usuario):
    """
    PRE:
        token debe ser un string, la llave de acceso
        id_usuario debe ser un entero 
    POST:
        devuelve el ID de un usuario como string
    """
    user = graph.get_object(id=id_usuario, fields='name' )
    print(user)



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


def main():
    # token: ver de hacer funcion para seleccion de empresarial,
    # consumidor o pagina.
    # Consumidor - Crux Bot Pagina
    token_consumidor = 'EAADBGgWWrIABAIKATkayQRUZAS2nS7fZAMVzyuO5ZBSOoZC1YeXaTKOjXRWaH90ZC1ZBRyXGYQvJZBQboNypU4jZA1XGCHd7QiXMNYEWwKylHrDqhH1fSB9782uaaWILwAJn3WvsgphiIVpadnZA8H82pjNn5BnwldXH2IshvT3foKItz5ZBeKUIJvLbLZAgdCvsTZB0Kn9K8D7uDb3xbEnYGH5XTEahNHTrlpZBqse39bZAtuzgZDZD'
    # empreserial
    token_empresarial = 'EAAPQlFICfVYBAHpLSHBZC5K9MDZCkqs4lSXHSOgbIKE66kohaAZAgr98ZCFBtVCnFdhltEOQGzDXpXbQxYdsyqQc9y6Ulckye0S4WHzBtfx9wSPWiLmMJVYWHj4HPwg0MZCZBkbzZAlMetAID8sTfzUuDk23vReXCRgmQCzR3M9RUrxae9dmGnaZBETOof64OqQvdYBS1J5zXFGgqUHBWdv3uDzQdJ2MpZCiCdZASe1cesJwZDZD'
    graph = facebook.GraphAPI(token_empresarial)
    subir_posteo(graph)


if __name__ == "__main__":
    main()

