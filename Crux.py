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
from TP2_G5 import mostrar_informacion_basica, visualizar_post_publicados_ig
from TP2_G5 import mostrar_comentarios, realizar_comentario, responder_comentario
from TP2_G5 import borrar_comentario, visualizar_insights_post, visualizar_post_hashtag
from TP2_G5 import postear_imagen_ig


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
    continuar = '¿Desea lo ayude en algo más? Puede ingresar "menú" para continuar o "salir" para despedirnos.\n'
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

    if (str(respuesta).lower()).find("listando") != -1:
        if (str(respuesta).lower()).find("seguís") != -1:
            listar_likes()  #10
        else:  #1
            ver_posts()
        print(continuar)

    elif (str(respuesta).lower()).find("existentes") != -1:
        if (str(respuesta).lower()).find("actualizar") != -1:  #3
            actualizar_posteo()
        else:  #2
            dar_like_posteo()
        print(continuar)

    elif (str(respuesta).lower()).find("subamos") != -1:
        if (str(respuesta).lower()).find("foto") != -1:  #5
            subir_foto()
        else:  #4
            subir_posteo()
        print(continuar)

    elif (str(respuesta).lower()).find("amigos") != -1:  #6
        listar_amigos()
        print(continuar)

    elif (str(respuesta).lower()).find("datos") != -1:  #7
        actualizar_datos_pagina()
        print(continuar)

    elif (str(respuesta).lower()).find("comentar") != -1:
        if (str(respuesta).lower()).find("respondido") != -1:  #15
            responder_comentario()
        elif (str(respuesta).lower()).find("necesitaré") != -1:  #14
            realizar_comentario()
        elif (str(respuesta).lower()).find("seleccionar") != -1:  #13
            mostrar_comentarios()
        else:  #8
            comentar_objeto()
        print(continuar)

    elif (str(respuesta).lower()).find("seguidores") != -1: #9
        listar_seguidores()
        print(continuar)

    elif (str(respuesta).lower()).find("cuenta") != -1:  #11
        mostrar_informacion_basica()
        print(continuar)

    elif (str(respuesta).lower()).find("publicados") != -1:  #12
        visualizar_post_publicados_ig()
        print(continuar)

    elif (str(respuesta).lower()).find("borrado") != -1:  #16
        borrar_comentario()
        print(continuar)

    elif (str(respuesta).lower()).find("alcance") != -1:  #17
        visualizar_insights_post()
        print(continuar)

    elif (str(respuesta).lower()).find("hashtag") != -1:  #18
        visualizar_post_hashtag()
        print(continuar)

    elif (str(respuesta).lower()).find("día") != -1:  #19
        postear_imagen_ig()
        print(continuar)

    elif (str(respuesta).lower()).find("menú") != -1:
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


if __name__ == "__main__":
    chatbot()

