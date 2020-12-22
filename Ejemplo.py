import json
import facebook
import requests


def obtener_nombre_usuario(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        Devuelve un diccionario con {id: id del usuario, nombre: nombre del usuario}
    """
    dicc = requests.get("https://graph.facebook.com/v9.0/me?fields=id%2Cname&access_token="+token)
    dicc_json = dicc.json()
    return (dicc_json)

def buscar_usuario(token, nombre_usuario):
    """
    PRE:
        token debe ser un string, la llave de acceso 
        nombre_usuario debe ser un string
    POST:
        devuelve el ID de un usuario como string
    """
    return usuario_ID

def dar_like_posteo(token, id_posteo):
    """
    PRE:
        token debe ser un string, la llave de acceso 
        id_posteo debe ser un string con el id del posteo
    POST:
        genera un like en el posteo enviado
    """

def leer_posteo(token, id_posteo):
    """
    PRE:
        token debe ser un string, la llave de acceso 
        id_posteo debe ser un string con el id del posteo
    POST:
        Devuelve un diccionario con todas las caracteristicas del posteo seleccionado
    """
    return diccionario_post

def subir_posteo(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        permite escribir un texto y lo publica
    """

def subir_foto(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        solicita al usuario que indique la ubicación de una foto y la publica
    """

def actualizar_posteo(token, id_posteo):
    """
    PRE:
        token debe ser un string, la llave de acceso 
        id_posteo debe ser un string con el id del posteo
    POST:
        Devuelve un diccionario con todas las caracteristicas del posteo seleccionado
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
    return lista_amigos

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

def enviar_mensaje_usuario(token, usuario_id):
    """
    PRE:
        token debe ser un string, la llave de acceso 
        usuario_id debe ser un string que indique el id del usuario
    POST:
       envia un mensaje al usuario seleccionado
    """

def actualizar_datos_perfil(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        Muestra los atributos que pueden ser moodificados, permite al usuario seleccionar uno
        y modificarlo. 
    """


def ver_ultimos_posts(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        muestra tus últimos posts
    """
    lista_de_posts = requests.get("https://graph.facebook.com/v9.0/me?fields=posts&access_token="+token)
    lista_de_posts_json = lista_de_posts.json()
    print(lista_de_posts_json)

def main():
    token =  "EAADBGgWWrIABAOnh9tn83v9oCMh3fZAIE4PDiDyQZBxxZBQEo6m3ZCzt4iJVYCpabBi7SWZCcmDVPXORil96mQT1k6NfO2GJP0hmkXBBJ4goVUc1ZBOgOhI2nZAZAfJfgZBkGXfNpMAXtj70ZAQnjJtWTGajFL9bjZAKDtBWqLaR4Rnt0KuNZAAqzmqRO1omtWLAzzY5TbjMWlscsG7Y70256lUH"
    graph = facebook.GraphAPI(token)
    #ver_posts(token)
    obtener_nombre_usuario(token)

if __name__ == "__main__":
    main()

