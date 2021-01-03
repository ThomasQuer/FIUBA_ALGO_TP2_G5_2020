from chatterbot import ChatBot

"""
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot("Crux")

trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish")
"""

"""
Con lo de arriba entrenamos al chatbot con los paquetes de conversations, greetings y trivia.
Una sola vez para que lo aprenda, luego lo obviamos.
Abajo formamos el modelo de conversación con el usuario.
"""

from chatterbot.trainers import ListTrainer

chat = ChatBot("Crux")

## charla = ["Acá va el modelo de charla para el asistente"]

trainer = ListTrainer(chat)
##trainer.train(charla)

while True: #Hasta que se me ocurra una forma de no usarlo.
    peticion = input(">>> ")
    respuesta = chat.get_response(peticion)
    print("Bot: ",str(respuesta))

    