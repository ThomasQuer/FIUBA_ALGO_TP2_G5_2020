"""
Para limpiar el aprendizaje previo del bot.

bot = ChatBot("Crux")
bot.storage.drop()

"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Crux',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


bot = ChatBot(
    'Crux',
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    logic_adapters = [
        {
            'import_path': "chatterbot.logic.BestMatch",
            "default_response": "Lo siento, no entendí tu pregunta.",
            'maximum_similarity_threshold': 0.90
        }
    ]
)


trainer = ListTrainer(bot)

trainer.train([
    "Hola",
    "¡Hola!, ¿En qué puedo ayudarte?",
    "¿Qué tal el clima?",
    "Con mucha humedad como es regular, un clásico ¿No es verdad?"
    ])

trainer.train([
    "Buenas", 
    "¿Cómo va?, ¿En qué puedo ayudarte?",
    "¿Qué tal el clima?",
    "Lamentablemente no tengo acceso a esa información. "
    "Sin embargo puedo decirte como está el dólar.",
    "¿Cómo está el dólar?",
    "En alza, compra ahora. Compra bajo, vende alto.",
    "Gracias por la información",
    "Un placer ser de ayuda."
    ])

trainer.train([
    "Crux", 
    "Justo acá, ¿En qué te ayudo?"
    ])

trainer.train([
    "Gracias", 
    "Un placer haberte ayudado.",
    "Gracias, Crux",
    "No es nada, ¡Que tengas un buen día!",
    "Muchas gracias"
    "Para servirte."
    ])

trainer.train([
    "Quiero agregar un amigo.", 
    "Muy bien, te ayudaré en eso. Primero ingresemos a tu cuenta y luego lo buscamos."
    ])

trainer.train([
    "Quiero seguir una cuenta.", 
    "Fantástico, ingresemos a tu cuenta y busquémoslo."
    ])

trainer.train([
    "Quiero agregar un nuevo posteo", 
    "¡Genial! ¿Dónde queres hacerlo?", 
    "En Instagram",
    "Eso es estupendo, primero debemos ingresar a tu cuenta de Instagram."
    ])

trainer.train([
    "Quiero comentar una publicación", 
    "Es bueno estar activo, primero necesito saber en qué aplicación lo querés hacer.",
    "En instagram",
    "Excelente, allá vamos."
    ])

trainer.train([
    "Necesito actualizar mi foto de perfil",
    "Decime la aplicación y te diré qué hacer.",
    "Instagram", 
    "Entremos a tu cuenta."
    ])

trainer.train([
    "¿Puedo ver mis seguidores?", 
    "¡Por supuesto que sí! ¿Qué aplicación?", 
    "Instagram",
    "Vayamos allá."
    ])

trainer.train([
    "Quiero buscar a alguien", 
    "Por supuesto pero ¿En dónde? Las opciones son ilimitadas. "
    "Bromeo, sólo son dos. ¿Instagram o Facebook?",
    "Instagram",
    "Okey dokey."
    ])

trainer.train([
    "Ya estoy en mi cuenta de Instagram", 
    "Eso es muy cierto, tan solo te estaba probando."
    "Ya estoy ahí.", 
    "Muy cierto, el día de hoy me encuentro algo distraido.",
    "Estoy acá.",
    "Okay, me atrapaste. Error mío."
    "Ya estoy en mi cuenta de Facebook", 
    "Uh, mala mía."
    ])

trainer.train([
    "Actualizar mis datos", 
    "¿Facebook o Instagram?", 
    "Instagram", 
    "Yendo para allá."
    ])

trainer.train([
    "Quiero enviar un DM", 
    "¿Aplicación?", 
    "Instagram"
    ])

trainer.train([
    "Quiero agregar un nuevo posteo", 
    "Claro, ¿El posteo será en Instagram o Facebook?",
    "Facebook", 
    "Genial, entonces primero necesito que entres a tu cuenta de Facebook."
    ])

trainer.train([
    "Me gustaría comentar una publicación", 
    "Sensacional, ¿Vamos a Facebook o Instagram?", 
    "A Facebook", 
    "Vayamos allá."
    ])

trainer.train([
    "Tengo que cambiar mi foto de perfil", 
    "Un requerimiento es el nombre de la aplicación.",
    "Facebook", 
    "¡Ah! Muy buena elección. Redirigiendo a tu cuenta de Facebook."
    ])

trainer.train([
    "Quiero ver mis seguidores", 
    "Claro que sí pero ¿En qué aplicación?", 
    "Facebook",
    "¿No es algo raro tener seguidores que son amigos? " 
    "Mark tiene unas ideas curiosas. Entra a tu cuenta, por favor."
    ])

trainer.train([
    "Necesito ver mi lista de amigos", 
    "¡Ah! No necesito preguntar qué app esta vez. Punto para mí. Como sea, vayamos allí."
    ])

trainer.train([
    "Quiero buscar a alguien", 
    "Dime la aplicación y te diré tus opciones.", 
    "Facebook", 
    "Ahí vamos."
    ])

trainer.train([
    "Actualizar datos de perfil", 
    "Es bueno mantenerse al día. ¿Dónde actualizamos?",
    "Facebook",
    "¡Genial!"
    ])

trainer.train([
    "Quisiera mandar un mensaje", 
    "Tus deseos son mis ordenes ¿O tus ordenes mis deseos? Como sea, decime la aplicación.",
    "Facebook", 
    "Marchando hacia Facebook."
    ])

trainer.train([
    "Quiero escribir un mensaje", 
    "¡Yo te ayudaré! ¿En dónde?", 
    "Facebook",
    "Estupendo."
    ])

bandera = 1
nombre = input("Ingrese su nombre: ")

while bandera == 1:
    peticion = input(nombre + ": ")
    if peticion != "":
        respuesta = bot.get_response(peticion)
        print("Crux: ",str(respuesta))
    else:
        bandera -= 1
  

    
