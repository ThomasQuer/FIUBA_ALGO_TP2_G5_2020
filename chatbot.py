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
from funciones_fb import actualizar_posteo, subir_posteo, listar_amigos
from funciones_fb import actualizar_datos_pagina, comentar_objeto, listar_seguidores, listar_likes


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
        stop_words = ['A:', 'M:', 'N:', 'N-', 'C-']

        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", " + name + ', "' + str(text_input) + '"'
            )

            response_text = chat.get_response(text_input)
            print('Message from user ID {} - {}'.format(user_id, text_input))

            count = 0
            for i in range(len(stop_words)):
                if str(text_input).find(stop_words[i]) == -1:
                    count += 1

            if count == len(stop_words):
                bot.send_text_message(user_id, str(response_text))

            actions(str(text_input), str(response_text), bot, user_id)

            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", Crux, " + '"' + str(response_text) + '"'
            )

        return '200'


def actions(text_input, response_text, bot, user_id):
    """
    PRE:
        text_input y response_text deben ser str, bot es el llamado a la clase Bot
        user_id debe ser un str
    POST:
        Al encontrarse con una palabra clave realiza la acción correspondiente
    """
    question = "¿Puedo ayudarte en algo más?"

    if (response_text.lower()).find("menú") != -1:
        menu = mostrar_menu()
        bot.send_text_message(user_id, menu)

    elif (response_text.lower()).find("existentes") != -1:
        if (response_text.lower()).find("actualizar") != -1:  # Opción 3
            tupla = ver_posts()
            posts = tupla[1]  # Listado de posteos
            posts = "".join(posts)
            bot.send_text_message(user_id, posts)
            requirement = (
                'Indique el número de post que desea actualizar con el siguiente formato: '
                '"N-(número de post) (mensaje)" Ej: N-5 Actualización')
            bot.send_text_message(user_id, requirement)

        else:  # Opción 2
            tupla = ver_posts()
            posts = tupla[1]
            posts = "".join(posts)
            bot.send_text_message(user_id, posts)
            requirement = (
                'Indique el número de post al que desea darle like con el siguiente formato: '
                '"N:(número de post)" Sin espacio. Ej: N:4')
            bot.send_text_message(user_id, requirement)

    elif (response_text.lower()).find("subamos") != -1:  # Opción 4
        requirement = (
            'Ingresá el mensaje del posteo de la siguiente forma "M:(mensaje)" Sin espacio. '
            'Ej M:Posteo nuevo')
        bot.send_text_message(user_id, requirement)

    elif (response_text.lower()).find("datos") != -1:  # Opción 7
        requirement = (
            'Los campos actuales son:\n1.Name\n2.About\n3.Website\n\n'
            'Indique el que desee actualizar con el siguiente formato: '
            '"A:(número de opción) (mensaje)" Ej: A:2 Esta es mi nueva info')
        bot.send_text_message(user_id, requirement)

    elif (response_text.lower()).find("comentar") != -1:  # Opción 8
        tupla = ver_posts()
        posts = tupla[1]
        posts = "".join(posts)
        bot.send_text_message(user_id, posts)
        requirement = (
            'Indique el número de post que desea comentar con el siguiente formato: '
            '"C-(número de post) (mensaje)" Ej: C-2 Nuevo comentario')
        bot.send_text_message(user_id, requirement)

    elif (response_text.lower()).find("listando") != -1:
        if (response_text.lower()).find("seguís") != -1:  # Opción 10
            likes = listar_likes()
            bot.send_text_message(user_id, likes)
            bot.send_text_message(user_id, question)
        
        else:  # Opción 1
            tupla = ver_posts()
            posts = tupla[1]
            posts = "".join(posts)
            bot.send_text_message(user_id, posts)
            bot.send_text_message(user_id, question)

    elif (response_text.lower()).find("amigos") != -1:  # Opción 6
        friends = listar_amigos()
        bot.send_text_message(user_id, friends)
        bot.send_text_message(user_id, question)
    
    elif (response_text.lower()).find("seguidores") != -1:  # Opción 9
        followers = listar_seguidores()
        bot.send_text_message(user_id, followers)
        bot.send_text_message(user_id, question)

    elif text_input.find("A:") != -1:
        result = actualizar_datos_pagina(text_input)
        bot.send_text_message(user_id, result)
        bot.send_text_message(user_id, question)

    elif text_input.find("M:") != -1:
        result = subir_posteo(text_input)
        bot.send_text_message(user_id, result)
        bot.send_text_message(user_id, question)

    elif text_input.find("N:") != -1:
        result = dar_like_posteo(text_input)
        bot.send_text_message(user_id, result)
        bot.send_text_message(user_id, question)

    elif text_input.find("N-") != -1:
        result = actualizar_posteo(text_input)
        bot.send_text_message(user_id, result)
        bot.send_text_message(user_id, question)

    elif text_input.find("C-") != -1:
        result = comentar_objeto(text_input)
        bot.send_text_message(user_id, result)
        bot.send_text_message(user_id, question)


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

