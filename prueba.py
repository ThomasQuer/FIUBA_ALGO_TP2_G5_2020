# 05-02-21 Funciona
import json
from flask import Flask, request
from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAPQlFICfVYBAJXtdLr7vc8gGNQ2VNKqRa50sk53MCfNFgYN2D3d9lAM2Y5Kxg79mlYHUg8fotiQBfv1yF54PtMhM0ZBTeKjZBzpZBHhGtXdi30ptMcAI4ilR6WJ7uiB7nQeuosbene2lbwXC8bNnb8ZBWwWSd8fz7p6WCxIYiOD9IaiPyyy'

GREETINGS = ['Hi', 'Hey', 'Hello', 'How are you?']

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
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            response_text = "Sorry, I can't undernstand you. I'm still learning."
            if text_input in GREETINGS:
                response_text = "Hello. I'm Crux, nice to meet you."
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id, response_text)

        return '200'


if __name__ == "__main__":
    app.run(debug=True)
