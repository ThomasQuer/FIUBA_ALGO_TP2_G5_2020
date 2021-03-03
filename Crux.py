# Chatbot con entrenamiento mediante archivos de texto
# con respuesta en terminal.
"""
Para limpiar el aprendizaje previo del bot.

bot = ChatBot("Crux")
bot.storage.drop()
"""

import os
import time
from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters
from TP2_G5 import mostrar_menu, ver_posts, dar_like_posteo, actualizar_posteo
from TP2_G5 import subir_posteo, subir_foto, listar_amigos, actualizar_datos_pagina
from TP2_G5 import comentar_objeto, listar_seguidores, listar_likes
from TP2_G5 import visualizar_informacion_cuenta_ig, mostrar_informacion_basica_ig, visualizar_post_publicados_ig, visualizar_informacion_post_seleccionado_ig
from TP2_G5 import visualizar_insights_post, visualizar_comentarios_post_ig, borrar_comentario, responder_comentario, visualizar_post_hashtag, postear_imagen_ig

def capturar_peticiones(nombre, bot, seguir):
    """
    PRE:
        nombre debe ser un str, bot debe ser el llamado al ChatBot.
        seguir debe ser un booleano.
    POST:
        Imprime en pantalla la respuesta del bot a las peticiones ingresadas
        por el usuario haciendo el llamado a las funciones correspondientes.
        Al finalizar devolverá seguir que indicará la continuación o
        finalización del programa.
    """
    peticion = input(nombre + ": ")
    log(
        time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
        ", " + nombre + ', "' + peticion + '"'
        )

    respuesta = bot.get_response((peticion.capitalize()))
    print("Crux: ", str(respuesta) + "\n\n")
    log(
        time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
        ", Crux, " + '"' + str(respuesta) + '"'
        )
    if (str(respuesta).lower()).find("instagram") != -1:

        if (str(respuesta).lower()).find("cuenta") != -1:
            visualizar_informacion_cuenta_ig()

        elif (str(respuesta).lower()).find("atributos") != -1:
            mostrar_informacion_basica_ig()

        elif (str(respuesta).lower()).find("comentario") != -1:
            if (str(respuesta).lower()).find("mostra") != -1:           
                visualizar_comentarios_post_ig()
            elif (str(respuesta).lower()).find("borra") != -1:
                borrar_comentario()
            else:
                responder_comentario()

        elif (str(respuesta).lower()).find("hashtag") != -1:
            visualizar_post_hashtag()

        elif (str(respuesta).lower()).find("imagen") != -1:      
            postear_imagen_ig()

        elif (str(respuesta).lower()).find("post") != -1:
            if (str(respuesta).lower()).find("insights") != -1:
                visualizar_insights_post()
            elif (str(respuesta).lower()).find("información") != -1:
                visualizar_informacion_post_seleccionado_ig()
            else:
                visualizar_post_publicados_ig()


    else:
        if (str(respuesta).lower()).find("listando") != -1:
            if (str(respuesta).lower()).find("seguís") != -1:
                listar_likes()
                
            else:
                ver_posts()

        elif (str(respuesta).lower()).find("existentes") != -1:
            if (str(respuesta).lower()).find("actualizar") != -1:
                actualizar_posteo()
            else:
                dar_like_posteo()

        elif (str(respuesta).lower()).find("subamos") != -1:
            if (str(respuesta).lower()).find("foto") != -1:
                subir_foto()
            else:
                subir_posteo()

        elif (str(respuesta).lower()).find("amigos") != -1:
            listar_amigos()

        elif (str(respuesta).lower()).find("datos") != -1:
            actualizar_datos_pagina()

        elif (str(respuesta).lower()).find("comentar") != -1:
            comentar_objeto()

        elif (str(respuesta).lower()).find("seguidores") != -1:
            listar_seguidores()

    if (str(respuesta).lower()).find("menú") != -1:
        mostrar_menu()

    elif (peticion.lower()).find("salir") != -1:
        seguir = False

    return seguir


def log(mensaje):

    """
    PRE: "mensaje" debe ser un string.

    POST: Creación del archivo log si no existiese,
        agrega la línea "mensaje".
    """

    with open("archivo.log", "a") as ptroArchivo:
        ptroArchivo.write(mensaje + "\n")


def chatbot():

    """
    POST: Tras saludar al usuario responde las preguntas hechas
        mediante el aprendizaje previo.
    """

    bot = ChatBot(
        'Crux', read_only=True,
        logic_adapters=[
            {
                'import_path': "chatterbot.logic.BestMatch",
                "statement_comparison_function": (
                    comparisons.LevenshteinDistance
                ),
                "response_selection_method": (
                    response_selection.get_first_response
                ),
                "default_response": (
                    "Lo siento, no entendí tu pregunta. "
                    "¿Podrías volver a intentarlo?"
                ),
                'maximum_similarity_threshold': 0.90
            },
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ],
        filters=[
            filters.get_recent_repeated_responses
        ]
    )

    nombre = input("¿Cuál es tu nombre?: ")

    log("\nInicio nueva charla.")
    saludo = (
        f"\n\n¡Hola, {(nombre)}! Soy Crux, asistente de ayuda virtual. "
        "Para empezar te mostraré mi menú de acciones.\n"
        "Sin embargo, también podes ingresar tu solicitud directamente mediante texto.\n"
        "Para volver a visualizar mi menú sólo debes ingresar 'menú'.\n"
        "Para finalizar ingresa 'salir'.\n\n"
        )
    log(
        time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
        ", Crux, " + '"' + saludo + '"'
        )
    print(saludo)
    mostrar_menu()
    seguir = True

    while seguir:
        seguir = capturar_peticiones(nombre, bot, seguir)

    log("Fin de la charla.")


def main():

    """
    POST: Realiza el llamado a la función "chatbot"
    """

    chatbot()


main()
