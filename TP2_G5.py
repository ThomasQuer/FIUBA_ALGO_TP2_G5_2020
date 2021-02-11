import json
import facebook
import requests
#import fbchat
#import re
def obtener_nombre_usuario(token):
    """
    PRE:
        token debe ser un string, la llave de acceso
    POST:
        Devuelve un diccionario con {id: id del usuario,
        nombre: nombre del usuario}
    """
    token=seleccion_token('consumidor_cuenta', token_solo=True)
    dicc = requests.get(f"https://graph.facebook.com/v9.0/me?fields=id%2Cname&access_token={token}")
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

def dar_like_posteo():
    """
    PRE:
        token debe ser un string, la llave de acceso
        id_posteo debe ser un string con el id del posteo
    POST:
        genera un like en el posteo enviado
    """
    #Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    #Se solicita id del posteo a dar like
    id_posteo = input("Ingrese el id del posteo utilizando la forma 'IDUSUARIO_IDPOSTEO': ") #ej: 105249781540470_106764151389033
    #Se utiliza la api para dar like al posteo y se imprime por pantalla el resultado
    darlike = graph.put_like(object_id = id_posteo)
    if darlike:
        print("Se ha dado like al posteo.")

    else:
        print("Hubo un problema, intente nuevamente.")


def leer_posteo(id_usuario):
    """
    PRE:
       
    POST:
        Solicita id del posteo e imprime el mensaje del posteo seleccionado
    """
    token, graph = seleccion_token("consumidor_cuenta")
    id_usuario = input('Ingrese el id del usuario: ') # 101662381858155
    id_posteo = input('Ingrese el id del posteo: ') #ej 101493071875086
    identificador = str(id_usuario + '_' + id_posteo)
    posteo = graph.get_object(id = identificador, fields ='message, attachments{description}') 
    print(posteo['message'])
    
def subir_posteo():
    """
    PRE:
    POST:
        permite escribir un texto y lo publica en una pagina
    """
    #Se selecciona token de pagina desde una app empresarial y se utiliza api
    token, graph = seleccion_token("empresarial_pagina")
    mensaje = input('Ingrese el mensaje del posteo: ')
    id_pagina = input('Ingrese el id de la página: ') #ej "105249781540470"
    posteo = graph.put_object(parent_object = id_pagina, connection_name ="feed", message = mensaje)
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
    # opcion 1 error: "C:\GIT\ALGOI\crux.jpg"
    #token, graph = seleccion_token("consumidor_cuenta")
    #camino_imagen = input("Ingrese la ubicación de la imagen: ")
    #archivo = open(camino_imagen, 'rb')
    #graph.put_photo(archivo, 'me/photos')
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

def listar_amigos():
    """
    PRE: necesita funcion seleccion_token()
    POST: Devuelve una lista con los amigos.
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

"""#momentaneamente desactivado
def enviar_mensaje_usuario(nombre_usuario):
    """
   # PRE:
    #    nombre_usuario debe ser un string que indique el nombre de usuario de la cuenta de facebook.
    #POST:
     #  envia un mensaje a usuario posteriormente ingresado.
    """
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


def ver_ultimos_posts():
    """
    PRE:
    POST:
        muestra tus últimos tres posts.
    """
    token=seleccion_token('consumidor_pagina', token_solo=True)
    lista_de_posts = requests.get(f"https://graph.facebook.com/v9.0/me?fields=posts&access_token={token}")
    lista_de_posts_json = lista_de_posts.json()
    print(lista_de_posts_json['posts'])
    contador = 0
    for i in lista_de_posts_json['posts']['data']:
        contador+=1
        if contador <= 3:
            print(i)

def seleccion_token(tipo_token, token_solo = False):
    """
    PRE: necesita un string indicando el tipo de token a devolver. Opciones: empresarial_cuenta, empresarial_pagina, consumidor_cuenta, consumidor_pagina.
    Si token_solo se especifica True, solo devuelve el token.
    POST: devuelve un string con el token segun tipo de aplicación y el objeto graph del tipo 'facebook.GraphAPI'.
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
    if token_solo == False:
        return token, graph
    else:
        return token
#de uso interno
def generar_token_extendido():
    """PRE
    POST: devuelve por pantalla el token extendido."""
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
    """ PRE: utiliza función seleccion_token()
    POST: devuelve por pantalla token de pagina. Si el token de la app en la función seleccion_token() es de larga vida, el token de pagina no caduca"""

    tipo = int(input("Ingrese 1-empresarial_cuenta o 2-consumidor_cuenta: "))
    if tipo == 1:
        tipo_token = "empresarial_cuenta"
    elif tipo == 2:
        tipo_token = "consumidor_cuenta"
    token = seleccion_token(tipo_token)
    token_pagina = requests.get(f"https://graph.facebook.com/v9.0/105249781540470?fields=access_token&access_token={token}")
    print("El token pagina es: " + token_pagina.json()['access_token'])

#main
def main():



if __name__ == "__main__":
    main()

