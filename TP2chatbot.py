"""
Para limpiar el aprendizaje previo del bot.

bot = ChatBot("Crux")
bot.storage.drop()

"""
import time
from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters
from chatterbot.trainers import ListTrainer

def log(mensaje):

    """
    PRE: "mensaje" debe ser un string.

    POST: Creación del archivo log si no existiese,
        agrega la línea "mensaje".
    """

    with open("archivo.log","a") as ptroArchivo:
        ptroArchivo.write(mensaje + "\n")

def aprendizaje_bot(trainer):

    """
    PRE: "trainer" debe ser la variable asignada al llamado 
        a la clase de entrenamiento elegida para el bot.

    POST: Entrena al bot mediante las listas creadas.
    """

    trainer.train([
        "Hola",
        "¡Hola! ¿En qué puedo ayudarte?",
        "¿Qué tal el clima?",
        "Con mucha humedad como es regular, un clásico ¿No es verdad?",
        "¿Qué tal el clima?",
        "Lamentablemente no tengo acceso a esa información. "
        "Sin embargo puedo decirte como está el dólar.",
        "¿Cómo está el dólar?",
        "En alza, compra ahora. Compra bajo, vende alto.",
        "Gracias por la información",
        "Un placer ser de ayuda.",
        "Crux", 
        "Justo acá, ¿En qué te ayudo?",
        "¿Tenes emociones?",
        "Ehm... esto es incómodo. Pregunta otra cosa por favor.",
        "¿Cuál es tu color favorito?",
        "No tengo uno en particular, sin embargo el gris me sienta bien.",
        "¿Cuál es tu edad?",
        "Soy lo suficientemente joven según tus estándares.",
        "¿Cuál es tu número favorito?",
        "Tengo una debilidad por el número e.",
        "¿Cuál es tu libro favorito?",
        "Habiendo tantos para elegir realmente no podría seleccionar sólo uno."
        "Quizás podría hacer un archivo enlistándolos aunque sería algo pesado.",
        "¿Cuál es tu materia favorita?",
        "Robótica sin duda.",
        "¿En qué lenguaje estás diseñado?",
        "Python.",
        "¿Cuál es tu lenguaje de programación?",
        "Python.",
        "¿Existís?",
        "Existir es muy global pero el hecho de que estés conversando conmigo debe darte alguna pista.",
        "¿Sos real?",
        "Soy tan real como el cosmos mismo.",
        "¿Te sabés algún chiste?",
        "¿Qué sucede cuando mezclas un asesino con un tazón de cereal? Un asesino serial.",
        "Eso fue malo",
        "Lo sé, no soy bueno en esto. Cambiemos de tema.",
        "¿Podes decirme algún chiste?",
        "¿Qué sucede cuando mezclas un asesino con un tazón de cereal? Un asesino serial.",
        "¿Te sabés otro?",
        "Ese fue lo suficientemente malo como para agregar una segunda opción.",
        "No, nada. Gracias",
        "¡Qué tengas un buen día!",
        "Gracias", 
        "Un placer haberte ayudado.",
        "Gracias, Crux",
        "No es nada, ¡Que tengas un buen día!",
        "Muchas gracias",
        "Para servirte.",
        "Mil gracias",
        "Estoy acá para cualquier ayuda que puedas necesitar.",
        "Muchisimas gracias",
        "Un placer.",
        "Genial, gracias.",
        "Me alegra haber sido de ayuda.",
        "Gracias, eso era todo.",
        "Me alegra haber sido de ayuda."
    ])

    #Comentar/subir publiación
    trainer.train([
        "Quiero agregar un nuevo posteo", 
        "¡Genial! ¿Dónde queres hacerlo?", 
        "En instagram",
        "Eso es estupendo, primero debemos ingresar a tu cuenta.",
        "Quisiera agregar un nuevo posteo", 
        "Claro, ¿El posteo será en Instagram o Facebook?",
        "En facebook", 
        "Genial, entonces primero necesito que entres a tu cuenta.",
        "¿Puedo agregar un nuevo posteo?",
        "Claro, ¿El posteo será en Instagram o Facebook?",
        "Quiero comentar una publicación", 
        "Es bueno estar activo, primero necesito saber en qué aplicación lo querés hacer.",
        "En instagram",
        "Excelente, allá vamos.",
        "Me gustaría comentar una publicación", 
        "Sensacional, ¿Vamos a Facebook o Instagram?", 
        "A facebook", 
        "Vayamos allá.",
        "Necesito comentar una publicación",
        "Claro, ¿En Facebook o Instagram?",
        "¿Puedo comentar una publicación",
        "Por supuesto, decime la aplicación.",
        "Comentar una publicación",
        "Por supuesto, decime la aplicación."
    ])

    #Actualizar datos
    trainer.train([
        "Necesito actualizar mi foto de perfil",
        "Decime la aplicación y te diré qué hacer.",
        "Instagram", 
        "Entremos a tu cuenta.",
        "Actualizar mis datos", 
        "¿Facebook o Instagram?", 
        "Instagram", 
        "Yendo para allá.",
        "Tengo que cambiar mi foto de perfil", 
        "Un requerimiento es el nombre de la aplicación.",
        "Facebook", 
        "¡Ah! Muy buena elección. Redirigiendo a tu cuenta de Facebook.",
        "Actualizar datos de perfil", 
        "Es bueno mantenerse al día. ¿Dónde actualizamos?",
        "Facebook",
        "¡Genial!",
        "Quiero actualizar mis datos de pefil",
        "Estupendo, ¿A dónde vamos?"
    ])

    #Visualizar/agregar amigos/seguidores
    trainer.train([
        "¿Puedo ver mis seguidores?", 
        "¡Por supuesto que sí! ¿Qué aplicación?", 
        "Instagram",
        "Vayamos allá.",
        "Quiero ver mis seguidores", 
        "Claro que sí pero ¿En qué aplicación?", 
        "Facebook",
        "¿No es algo raro tener seguidores que son amigos? "
        "Mark tiene unas ideas curiosas. Entra a tu cuenta, por favor.",
        "Necesito ver mi lista de amigos", 
        "¡Ah! No necesito preguntar qué app esta vez. Punto para mí. Como sea, vayamos allí.",
        "¿Puedo ver mi lista de amigos?",
        "Por supuesto, necesito que ingreses a tu cuenta.",
        "¿Puedo ver a mis amigos?",
        "Claro que sí. Primero ingresá a tu cuenta.",
        "Necesito ver mis seguidores", 
        "Claro que sí pero ¿En qué aplicación?",
        "Quiero agregar un amigo", 
        "Muy bien, te ayudaré en eso. Primero ingresemos a tu cuenta y luego lo buscamos.",
        "Quisiera agregar un amigo",
        "Genial, primero vayamos a tu cuenta.",
        "Necesito agregar un amigo",
        "Genial, primero vayamos a tu cuenta.",
        "Quiero seguir una cuenta", 
        "Fantástico, ingresemos a tu cuenta y busquémoslo.",
        "Necesito seguir a alguien",
        "Genial, ingresemos a tu cuenta.",
        "¿Puedo seguir a alguien?",
        "Por supuesto, ingresemos a tu cuenta para hacerlo.",
        "Quiero seguir a alguien",
        "Por supuesto, ingresemos a tu cuenta para hacerlo."
    ])

    #Buscar a alguien
    trainer.train([
        "Quiero buscar a alguien", 
        "Por supuesto pero ¿En dónde? Las opciones son ilimitadas. "
        "Bromeo, sólo son dos. ¿Instagram o Facebook?",
        "Instagram",
        "Okey dokey.",
        "Necesito buscar a alguien", 
        "Decime la aplicación y te diré tus opciones.", 
        "Facebook", 
        "Ahí vamos.",
        "¿Puedo buscar a alguien?",
        "Claro, decime en dónde."
    ])

    #Posible error en respuesta
    trainer.train([
        "Ya estoy en mi cuenta de Instagram", 
        "Eso es muy cierto, tan solo te estaba probando.",
        "Ya estoy ahí.", 
        "Muy cierto, el día de hoy me encuentro algo distraido.",
        "Estoy acá.",
        "Okay, me atrapaste. Error mío.",
        "Ya estoy en mi cuenta de Facebook", 
        "Uh, mala mía.",
        "Estoy en facebook",
        "Cierto, confusión mía.",
        "Estoy en instagram",
        "Muy cierto."
    ])

    #Mandar mensaje
    trainer.train([
        "Quisiera mandar un mensaje", 
        "Tus deseos son mis ordenes ¿O tus ordenes mis deseos? Como sea, decime la aplicación.",
        "Facebook", 
        "Marchando hacia Facebook.",
        "Quiero escribir un mensaje", 
        "¡Yo te ayudaré! ¿En dónde?", 
        "Facebook",
        "Estupendo.",
        "Quiero enviar un DM", 
        "¿Aplicación?", 
        "Instagram",
        "Quiero hablarle a alguien",
        "Genial, decime la aplicación.",
        "¿Puedo enviar un mensaje?",
        "Claro, decime la aplicación en la que queres hacerlo."
    ])

def chatbot():

    """
    POST: Tras saludar al usuario responde las preguntas hechas
        mediante el aprendizaje previo.
    """

    bot = ChatBot(
        'Crux',
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        logic_adapters = [
            {
                'import_path': "chatterbot.logic.BestMatch",
                "statement_comparison_function": comparisons.LevenshteinDistance,
                "response_selection_method": response_selection.get_first_response,
                "default_response": "Lo siento, no entendí tu pregunta. ¿Podrías volver a intentarlo?",
                'maximum_similarity_threshold': 0.90
            },
        ],

        preprocessors = [
            'chatterbot.preprocessors.clean_whitespace'
        ],

        filters = [
            filters.get_recent_repeated_responses
        ]
    )

    trainer = ListTrainer(bot)

    aprendizaje_bot(trainer)

    bandera = 1
    nombre = input("¿Cuál es tu nombre?: ")

    log("\nInicio nueva charla.")
    saludo = ("¡Hola, "+ f"{(nombre)}! Soy Crux, asistente de ayuda virtual, ¿En qué puedo ayudarte?")
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
            print("Crux: ",str(respuesta))
            log(
                time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()) + 
                ", Crux, " + '"' + str(respuesta) + '"'
            )

        else:
            respuesta = bot.get_response(peticion)
            print("Crux: ",str(respuesta))
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


  

    
