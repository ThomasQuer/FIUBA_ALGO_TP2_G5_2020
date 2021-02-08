# FIUBA_ALGO_TP2_G5_2020
Trabajo práctico número 2 de algoritmos y progrmaciòn, grupo 05, segundo cuatrimestre 2020

# Webhook branch
Se necesita tener integrado Flask:

 Create an environment
Create a project folder and a venv folder within: $ mkdir myproject $ cd myproject $ python3 -m venv venv

On Windows: $ py -3 -m venv venv

Activate the environment Before you work on your project, activate the corresponding environment: $ . venv/bin/activate

On Windows:

venv\Scripts\activate Your shell prompt will change to show the name of the activated environment.

Install Flask Within the activated environment, use the following command to install Flask: $ pip install Flask

De Documentación de Flask

Se necesita descargar ngrok, seguir instrucciones siguiente enlace. https://ngrok.com/download
Una vez descargado y descomprimido ir al cmd y buscar la carpeta en la que se descargó, mantener abierto. Ejecutar webhook.py Ir al link que aparece en la terminal: “Running on http:….” Volver al cmd y correr el siguiente comando:

$ ngrok http 5000 –bind-tls=true

Copiar el link “Forwarding https:…..” Acceder al mismo. Los dos links deberían mostrar “400” El link con terminación .ngrok.io será nuestro ‘Callback URL’ en Facebook developers. ‘Verify Token’ es el token generado para la página de Crux. EAAPQlFICfVYBAJXtdLr7vc8gGNQ2VNKqRa50sk53MCfNFgYN2D3d9lAM2Y5Kxg79mlYHUg8fotiQBfv1yF54PtMhM0ZBTeKjZBzpZBHhGtXdi30ptMcAI4ilR6WJ7uiB7nQeuosbene2lbwXC8bNnb8ZBWwWSd8fz7p6WCxIYiOD9IaiPyyy
