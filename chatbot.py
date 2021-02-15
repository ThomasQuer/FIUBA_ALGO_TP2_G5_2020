import os
import time

import json
from flask import Flask, request
from bot import Bot

from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters

from TP2_G5 import ver_ultimos_posts, obtener_nombre_usuario

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

        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", " + name + ', "' + str(text_input) + '"'
            )

            if (str(text_input)).find("post") != -1:
                response_text = ver_ultimos_posts()
                print('Message from user ID {} - {}'.format(user_id, text_input))
                bot.send_text_message(user_id, str(response_text))

            # Acá se irían agregando las opciones para el llamado a funciones
            
            else:
                response_text = chat.get_response(text_input)
                print('Message from user ID {} - {}'.format(user_id, text_input))
                bot.send_text_message(user_id, str(response_text))

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

 
