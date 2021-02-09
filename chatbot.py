import os

import json
from flask import Flask, request
from bot import Bot

from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters
from chatterbot.trainers import ListTrainer

PAGE_ACCESS_TOKEN = 'EAAPQlFICfVYBAJXtdLr7vc8gGNQ2VNKqRa50sk53MCfNFgYN2D3d9lAM2Y5Kxg79mlYHUg8fotiQBfv1yF54PtMhM0ZBTeKjZBzpZBHhGtXdi30ptMcAI4ilR6WJ7uiB7nQeuosbene2lbwXC8bNnb8ZBWwWSd8fz7p6WCxIYiOD9IaiPyyy'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
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
            'Crux',
            read_only=True,
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                'chatterbot.logic.BestMatch',
                {
                    'import_path': "chatterbot.logic.BestMatch",
                    "statement_comparison_function": (
                        comparisons.LevenshteinDistance
                    ),
                    "response_selection_method": (
                        response_selection.get_first_response
                    ),
                    "default_response": (
                        "Lo siento, no entendí tu pregunta. ¿Podrías volver a intentarlo?"
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

        directory = 'training_data'

        # Entrenamiento del bot.

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                print('\n Chatbot training with '+os.path.join(directory, filename) + ' file')
                training_data = open(os.path.join(directory, filename)).read().splitlines()
                trainer = ListTrainer(chat)
                trainer.train(training_data)
        
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            response = chat.get_response(text_input)
            response_text = str(response)
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id, response_text)

        return '200'


if __name__ == "__main__":
    app.run(debug=True)
