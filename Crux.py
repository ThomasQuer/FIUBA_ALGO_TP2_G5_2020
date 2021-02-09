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

def log(mensaje):

    """
    PRE: "mensaje" debe ser un string.

    POST: Creación del archivo log si no existiese,
        agrega la línea "mensaje".
    """

    with open("archivo.log","a") as ptroArchivo:
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

    bandera = 1
    nombre = input("¿Cuál es tu nombre?: ")

    log("\nInicio nueva charla.")
    saludo = (
        "¡Hola, " + f"{(nombre)}! Soy Crux, asistente de ayuda virtual, " +
        "¿En qué puedo ayudarte?"
        )
    log(
        time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
        ", Crux, " + '"' + saludo + '"'
        )
    print(saludo)

    while bandera == 1:
        peticion = input(nombre + ": ")
        log(
            time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
            ", " + nombre + ', "' + peticion + '"'
            )

        if (peticion.lower()).find("gracias") == -1:
            respuesta = bot.get_response((peticion.capitalize()))
            print("Crux: ", str(respuesta))
            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", Crux, " + '"' + str(respuesta) + '"'
            )

        else:
            respuesta = bot.get_response(peticion)
            print("Crux: ", str(respuesta))
            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) +
                ", Crux, " + '"' + str(respuesta) + '"'
            )
            bandera -= 1

    log("Fin de la charla.")


def main():

    """
    POST: Realiza el llamado a la función "chatbot"
    """

    chatbot()


main()
