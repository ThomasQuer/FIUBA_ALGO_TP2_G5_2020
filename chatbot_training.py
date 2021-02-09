import os

from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot import filters
from chatterbot.trainers import ListTrainer


chat = ChatBot(
    'Crux',
    read_only=True,
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

directory = 'training_data'

# Entrenamiento del bot.

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(
            '\n Chatbot training with '+os.path.join(directory, filename) +
            ' file'
        )
        training_data = (
            open(os.path.join(directory, filename)).read().splitlines()
        )
        trainer = ListTrainer(chat)
        trainer.train(training_data)
        
