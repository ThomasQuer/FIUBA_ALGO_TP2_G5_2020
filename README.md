# Crux Bot
Crux es un asistente para las redes sociales de Facebook e Instagram.
Para consultar al asistente Crux desde la terminal debe ejecutarse Crux.py.
Las consultas a través de Messenger deben realizarse ejecutando chatbot.py y por medio del canal de mensajes en la página de facebook 'Crux Bot Página'. En el caso de realizar la consulta por esta vía al ejecutar chatbot.py es necesario se genere un túnel activo para la conexión entre el localhost y la aplicación.

A continuación se detallan los archivos presentados:

# training_data
Contiene los archivos que chatbot_training.py necesitará para completar el aprendizaje.

# Crux.py (Salida en terminal)
Crea al chatbot 'Crux', su aprendizaje es mediante archivos extensión .txt ubicados en la carpeta 'training_data'. La conversación realizada con el usuario se almacena en un archivo extensión .log con fecha y horario integrado. Muestra menú de opciones al empezar, luego responde a las entradas realizadas a través del teclado por el usuario.

# chatbot_training.py
Se encarga de la creación y aprendizaje de 'Crux', debe ser el primero en ejecutarse.

# TP2_G5.py
Contiene los token de acceso de Facebook API y las funciones que interactuan con Facebook e Instagram.

# Justificación.txt
Respecto a lo solicitado en el trabajo práctico se agregan justificaciones de lo alcanzado en las funciones y las limitaciones encontradas.

# bot.py
Crea la clase que le permitirá a la función webhook, mediante el acceso a través de la api, recibir el mensaje del usuario y enviar la respuesta.

# chatbot.py (Salida a través de messenger)
Llama a chatbot 'Crux' e importa a bot.py para hacer uso de su clase.

  La función webhook: 
  Se encarga de recibir, procesar y enviar el mensaje respuesta.
  
  La función log:
  Almacena la conversación entre el bot y el usuario.
 
 # archivo.txt
Muestra el historial de la conversación establecida con el asistente.

# funciones_fb.py
Contiene los token de acceso de Facebook API y las funciones que interactuan con Facebook e Instagram modificados de manera tal que puedan ser utilizados en la salida por Messenger.

# Paquetes necesarios para lograr salida a través de messenger
 Se necesita tener integrado Flask:

 Create an environment
  Create a project folder and a venv folder within: $ mkdir myproject $ cd myproject $ python3 -m venv venv

On Windows: $ py -3 -m venv venv
  Activate the environment Before you work on your project, activate the corresponding environment: $ . venv/bin/activate
  
  venv\Scripts\activate Your shell prompt will change to show the name of the activated environment.
  
  Install Flask Within the activated environment, use the following command to install Flask: $ pip install Flask

"De Documentación de Flask"

 Se necesita descargar ngrok:
 
  Seguir instrucciones siguiente enlace. https://ngrok.com/download
Es necesario la creación de una cuenta, así también como la conexión de la misma a través del cmd. Sin ella el link expirará pasadas dos horas de la creación. 
Una vez descargado y descomprimido ir al cmd y buscar la carpeta en la que fue descomprimida, mantener abierto. 
Ejecutar chatbot.py
Ir al link que aparece en la terminal: “Running on http:….” Volver al cmd y correr el siguiente comando:

  $ ngrok http 5000 –bind-tls=true    (copiar el comando en forma manual)

Copiar el link “Forwarding https:…..” Acceder al mismo.
Los dos links deberían mostrar “400” 
El link con terminación .ngrok.io será nuestro ‘Callback URL’ en Facebook developers. ‘Verify Token’ será 'cruxbot'.

  Problema encontrado: El link que ngrok otorga caduca una vez cerrada la terminal cmd. Al volver a abrirla y ejecutar chatboy.py se deberá volver a generar otro link ngrok (Volviendo a correr el comando ingresado arriba) que tendrá que ser modificado en la configuración de messenger en developers.facebook 'URL devolución de llamada'. De lo contrario chatbot.py no podrá devolver el mensaje respuesta al usuario.
  
# Bibliografía y Referencias
Tutorial de uso de Facebook Graph API: https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999
modulo python-facebook-api: https://pypi.org/project/python-facebook-api/
https://medium.com/analytics-vidhya/facebook-graph-api-python-3c8bab8a5a2a
https://www.geeksforgeeks.org/facebook-api-set-2/?ref=rp
tokens https://developers.facebook.com/docs/pages/access-tokens/
alternativa de encontrar id https://www.labnol.org/internet/find-facebook-page-id-profile/6909/
posteo de foto https://stackoverflow.com/questions/34393982/upload-image-to-facebook-using-the-python-api#
