from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json


class Bot:
    chatbot = ChatBot("ilya")

    def train():
        chatbot.set_trainer(ListTrainer)
        chatbot.train(TrainnigDataJson['Data'])

    def test():
        message = input('Your message:\n')
        response = chatbot.get_response(message);
        print(response); 

class Data(Bot):
    json_path = open("data.json","r")
    TrainnigDataJson = json.loads(json_path)

    message = input('Your message:\n')
    response = chatbot.get_response(message);
    print(response); 

Bot.test()