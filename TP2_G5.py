import json
import facebook
import requests
import fbchat
import re

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
    ##opcion 1 tira error
    ##ej: putlike = graph.put_like(object_id = id_posteo) # id_posteo = USERID_POSTID
    #putlike = graph.put_like(object_id ="101662381858155_101493071875086") 
    #print(json.dumps(putlike, indent = 4))
    ##tira error:
    ##facebook.GraphAPIError: (#3) Publishing likes through the API is only available for page access tokens
    ##facebook.GraphAPIError: (#2) Service temporarily unavailable

def leer_posteo(id_usuario):
    """
    PRE:
       id_usuario debe ser un string con el id del usuario
    POST:
        Solicita id del posteo e imprime el mensaje del posteo seleccionado
    """
    id_posteo = input('Ingrese el id del posteo: ')
    identificador = str(id_usuario + '_' + id_posteo)
    #token utilizado el de app comercial #id = 'USERID_POSTID' #ej: identificador = 101662381858155_101493071875086
    posteo = graph.get_object(id = identificador, fields ='message, attachments{description}') 
    print(posteo['message'])
    

def subir_posteo(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        permite escribir un texto y lo publica
    """
    ##opcion 1 con error
    #mensaje = input('Ingrese el mensaje del posteo: ')
    #posteo = graph.put_object(parent_object ="me", connection_name ="feed", message = mensaje) 
    #print(json.dumps(posteo, indent = 4)) 
    ##tira error:
    '''facebook.GraphAPIError: (#200) If posting to a group, requires app being installed in the group, and \
          either publish_to_groups permission with user token, or both pages_read_engagement \
          and pages_manage_posts permission with page token; If posting to a page, \
          requires both pages_read_engagement and pages_manage_posts as an admin with \
          sufficient administrative permission'''

def subir_foto(token):
    """
    PRE:
        token debe ser un string, la llave de acceso 
    POST:
        solicita al usuario que indique la ubicación de una foto y la publica
    """
    #opcion 1 error:
    # camino_imagen = input("Ingrese la ubicación de la imagen: ")
    # archivo = open(camino_imagen, 'rb')
    #graph.put_photo(archivo, 'me/photos')
    #facebook.GraphAPIError: (#200) This endpoint is deprecated since the required permission publish_actions is deprecated

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
    amigos = graph.get_object('me', fields='friends')
    #Excepcion: Solo los amigos que han instalado esta aplicación estarán en la versión 2.0 o superior de la API.
    print("La cantidad de amigos que tienes es: " + str(amigos['friends']['summary']['total_count']))
    #ver como obtener nombre de los que tienen la api

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

def enviar_mensaje_usuario(nombre_usuario):
    """
    PRE:
        nombre_usuario debe ser un string que indique el nombre de usuario de la cuenta de facebook.
    POST:
       envia un mensaje a usuario posteriormente ingresado.
    """
    #seteo de variables para fbchat.Client (sino genera un error)
    fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
    fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

    #nombre_usuario = 'crux.bot.1'
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
    #token: ver de hacer funcion para seleccion de empresarial o consumidor o pagina..
    #empreserial
    token = 'EAAPQlFICfVYBAONyy5cBcqpzZCEQBpIjdGJk1Vx2UsDVlXi8WYGY6MvMTNjablhOSAkfOUDhUjJwumEkj6hZA5xtZAdYBevTZAcKC9Ox55elkEJerSL1xpcjMTQPLsEN5dKLHuNRGgGlXcDl0UsZBGqqAJsCnMTUSZAiwzZABJZClcaPvtmXb5oa1eYJVbHQTcqQCQR8wpGcsxvbGVoIzSyZA1h14vP54Vp0ykU0n8hMZCCQZDZD'
    #consumidor
    token = 'EAADBGgWWrIABAFjAiHvjZA3K8zZCcYLJf7tNYTKB19C2ZAqVCnxubL4KRLX0eXZCDYTSaWtc7rbMOSPZCD9ZCF06WMagWIZAef7YkTo896rF9I8voWIdJBmfzOm1fW52fChZArsRiq1ZCLrUMzbMJ9jvKIFGSPBQVGLEOt7QGiRZAkJZBQjZCDI1hpLfqCvjTQRDdTwGxAezYTYLMMZC24SLbPhZB1TYsjs3eBD02fzmduRxuIvAZDZD'
    #empresaria - Crux bot pagina
    token = 'EAAPQlFICfVYBAFdXNXmWpgRZBetJt2iUZCB3nwzqqbibAeEDnINOSAfc0vkDTCuG3f6SplrbU6n73nS2NV08Vjba5GoK4gZAYYMAC6W6cXzCwWm0KDJA8ePHxOo4ZAI8o7nPpoO35tEkVaYAMRnlGZA4Sm4RWU7uzciydgsSHpgZBRk0iV5Yeymt6wufVRQhBxq4t4lEwK6PMneFT3N3NAmTCjFziRwYHJebqBXiZBzPAZDZD'
    #Consumidor - Crux Bot Pagina
    token = 'EAADBGgWWrIABADelCf8PksTvyxTOqVQkiwZBZBVohdDpOTZAm6Vw08B2CaiPnv8ZAoZAxRElUyV27m7t08pipRnUcBNHJz74xfIynlHEzjR1G3rDPCjxTsDxX2tLIUiUzJpAeSAVjt41t7szFPUSLp3FLHEftHCIE46ZCADX8eSef262QjZC9TH40qUMABqPpFWZBojnDWiXshayPJnLKJisAUKtoXZAdduTV5iPxSqsPRQZDZD'
    
    graph = facebook.GraphAPI(token)

if __name__ == "__main__":
    main()