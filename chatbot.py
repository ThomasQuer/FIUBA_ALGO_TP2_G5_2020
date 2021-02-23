import os
import time

import json
from flask import Flask, request
from bot import Bot

from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters

from funciones_fb import mostrar_menu, obtener_nombre_usuario, ver_posts, dar_like_posteo
from funciones_fb import actualizar_posteo, subir_posteo, subir_foto, listar_amigos
from funciones_fb import actualizar_datos_pagina, comentar_objeto


PAGE_ACCESS_TOKEN = 'EAAPQlFICfVYBANAGfhETlDucMuf5ZAZCRyY15u2AbYCy22QajvRa1QKLeZCAd65e7UoS5ss3ZBOmvZANXxZBqYwnKOyK9EcJnCvvUTUXtvOMvsSBmHAjMbg14b3dEd2HaZAH0ssr3pNQ1M1OKMIH3vPNEnlSPfz0sI5Gp8sDZCMKP8kmzrQaZBEMD'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    """
    POST: Se encarga de devolver un mensaje respuesta al usuario
        según el entrenamiento del bot a través del archivo de texto.
    """

    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'cruxbot':
            return str(challenge)
        return '400'

    else:
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)

        chat = ChatBot(
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

        aux = obtener_nombre_usuario()
        name = aux['name']
        stop_words = ['N:', 'N-', 'M:']

        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", " + name + ', "' + str(text_input) + '"'
            )

            response_text = chat.get_response(text_input)
            print('Message from user ID {} - {}'.format(user_id, text_input))

            contador = 0
            for i in range(len(stop_words)):
                if str(text_input).find(stop_words[i]) == -1:
                    contador += 1

            if contador == len(stop_words):
                bot.send_text_message(user_id, str(response_text))

            if (str(response_text).lower()).find("menú") != -1:
                menu = mostrar_menu()
                bot.send_text_message(user_id, menu)

            elif (str(response_text).lower()).find("listando") != -1:  # Acá corro la opción 1
                combo = ver_posts()
                posts = combo[1]
                posts = "".join(posts)
                bot.send_text_message(user_id, posts)

            elif (str(response_text).lower()).find("existentes") != -1:
                if (str(response_text).lower()).find("actualizar") != -1:  # Acá corro la opción 3
                    combo = ver_posts()
                    posts = combo[1] #Listado de posteos
                    posts = "".join(posts)
                    bot.send_text_message(user_id, posts)
                    requisito = 'Indique el número de post que desea actualizar con el siguiente formato: "N-(número de post) + (mensaje)" Ej: N-5 Actualización'
                    bot.send_text_message(user_id, requisito)

                else:  # Acá corro la opción 2
                    combo = ver_posts()
                    posts = combo[1]
                    posts = "".join(posts)
                    bot.send_text_message(user_id, posts)
                    requisito = 'Indique el número de post al que desea darle like con el siguiente formato: "N:(número de post)" Sin espacio. Ej: N:4'
                    bot.send_text_message(user_id, requisito)

            elif (str(response_text).lower()).find("subamos") != -1: #Opción 4
                requisito = 'Ingresá el mensaje del posteo de la siguiente forma "M:(mensaje)" Sin espacio. Ej M:Mensaje actualización'
                bot.send_text_message(user_id, requisito)

            elif str(text_input).find("M:") != -1:
                eleccion = str(text_input)
                respuesta = subir_posteo(eleccion)
                bot.send_text_message(user_id, respuesta)

            elif str(text_input).find("N:") != -1:
                eleccion = str(text_input)
                respuesta = dar_like_posteo(eleccion)
                bot.send_text_message(user_id, respuesta)

            elif str(text_input).find("N-") != -1:
                eleccion = str(text_input)
                respuesta = actualizar_posteo(eleccion)
                bot.send_text_message(user_id, respuesta)

            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", Crux, " + '"' + str(response_text) + '"'
            )

        return '200'


def log(message):
    """
    PRE: "message" debe ser un string.

    POST: Creación del archivo log si no existiese,
        agrega la línea "message".
    """

    with open("archivo.log", "a") as ptroArchivo:
        ptroArchivo.write(message + "\n")


if __name__ == "__main__":
    app.run(debug=True)

 
