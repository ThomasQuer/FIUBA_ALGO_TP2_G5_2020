from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat = ChatBot("Crux")


saludos1 = ["Hola","¡Hola!, ¿En qué puedo ayudarte?"]

saludos2 = ["Buenas", "¿Cómo va?, ¿En qué puedo ayudarte?"]

saludos3 = ["Crux", "Justo acá, ¿En qué te ayudo?"]

saludos4 = ["Gracias", "Un placer haberte ayudado."]



solicitar_amistad = ["Quiero agregar un amigo.", "Muy bien, te ayudaré en eso. Primero ingresemos a tu cuenta y luego lo buscamos."]

seguir_usuario = ["Quiero seguir una cuenta.", "Fantástico, ingresemos a tu cuenta y busquémoslo."]

subir_posteo_ig = ["Quiero agregar un nuevo posteo", "¡Genial! ¿Dónde queres hacerlo?", "En Instagram",
    "Eso es estupendo, primero debemos ingresar a tu cuenta de Instagram."]

comentar_ig = ["Quiero comentar una publicación", 
    "Es bueno estar activo, primero necesito saber en qué aplicación lo querés hacer.",
    "En instagram","Excelente, allá vamos."]

foto_perfil_ig = ["Necesito actualizar mi foto de perfil","Decime la aplicación y te diré qué hacer.",
    "Instagram", "Entremos a tu cuenta."]

seguidores_ig = ["¿Puedo ver mis seguidores?", "¡Por supuesto que sí! ¿Qué aplicación?", "Instagram",
    "Vayamos allá."]

buscar_ig = ["Quiero buscar a alguien", 
    "Por supuesto pero ¿En dónde? Las opciones son ilimitadas. Bromeo, sólo son dos. ¿Instagram o Facebook?",
    "Instagram","Okey dokey."]

cuenta_ig = ["Ya estoy en mi cuenta de Instagram", "Eso es muy cierto, tan solo te estaba probando."]

cuenta = ["Ya estoy ahí.", "Muy cierto, el día de hoy me encuentro algo distraido."]

actualizar_ig = ["Actualizar mis datos", "¿Facebook o Instagram?", "Instagram", "Yendo para allá."]

mensaje_ig = ["Quiero enviar un DM", "¿Aplicación?", "Instagram"]



subir_posteo_fb = ["Quiero agregar un nuevo posteo", "Claro, ¿El posteo será en Instagram o Facebook?",
    "Facebook", "Genial, entonces primero necesito que entres a tu cuenta de Facebook."]

comentar_fb = ["Me gustaría comentar una publicación", "Sensacional, ¿Vamos a Facebook o Instagram?", 
    "A Facebook", "Vayamos allá."]

foto_perfil_fb = ["Tengo que cambiar mi foto de perfil", "Un requerimiento es el nombre de la aplicación.",
    "Facebook", "¡Ah! Muy buena elección. Redirigiendo a tu cuenta de Facebook."]

seguidores_fb = ["Quiero ver mis seguidores", "Claro que sí pero ¿En qué aplicación?", "Facebook",
    "¿No es algo raro tener seguidores que son amigos? Mark tiene unas ideas curiosas. Entra a tu cuenta, por favor."]

listar_amigos = ["Necesito ver mi lista de amigos", 
    "¡Ah! No necesito preguntar qué app esta vez. Punto para mí. Como sea, vayamos allí."]

buscar_fb = ["Quiero buscar a alguien", "Dime la aplicación y te diré tus opciones.", "Facebook", "Ahí vamos."]

cuenta_fb = ["Ya estoy en mi cuenta de Facebook", "Uh, mala mía."]

actualizar_fb = ["Actualizar datos de perfil", "Es bueno mantenerse al día. ¿Dónde actualizamos?",
    "Facebook","¡Genial!"]

mensaje_fb = ["Quisiera mandar un mensaje", 
    "Tus deseos son mis ordenes ¿O tus ordenes mis deseos? Como sea, decime la aplicación.",
    "Facebook", "Marchando hacia Facebook."]

mensaje_fb2 = ["Quiero escribir un mensaje", "¡Yo te ayudaré! ¿En dónde?", "Facebook",
    "Estupendo."]


trainer = ListTrainer(chat)

trainer.train(saludos1)
trainer.train(saludos2)
trainer.train(saludos3)
trainer.train(saludos4)

trainer.train(solicitar_amistad)
trainer.train(seguir_usuario)
trainer.train(subir_posteo_ig)
trainer.train(comentar_ig)
trainer.train(foto_perfil_ig)
trainer.train(seguidores_ig)
trainer.train(buscar_ig)
trainer.train(cuenta_ig)
trainer.train(actualizar_ig)
trainer.train(mensaje_ig)
trainer.train(cuenta)

trainer.train(subir_posteo_fb)
trainer.train(comentar_fb)
trainer.train(foto_perfil_fb)
trainer.train(seguidores_fb)
trainer.train(listar_amigos)
trainer.train(buscar_fb)
trainer.train(cuenta_fb)
trainer.train(actualizar_fb)
trainer.train(mensaje_fb)
trainer.train(mensaje_fb2)

while True: # Hasta que se me ocurra una forma de no usarlo. Esto es sólo para verificar
    peticion = input(">>> ")   # que las respuestas correspondan con las entradas.
    respuesta = chat.get_response(peticion)
    print("Bot: ",str(respuesta))
  

    
