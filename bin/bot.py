from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import logging


class Bot:
    def __init__(self, Name):
        self.Name = Name

    Name = ChatBot("Bot")

    def train(self):
        self.Name.set_trainer(ListTrainer)
        self.Name.train(['Data'])

    def test(self):
        message = input('Your message:\n')
        response = self.Name.get_response(message)
        print(response)




