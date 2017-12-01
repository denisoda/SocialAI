from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

class Bot:
    chatbot = ChatBot("ilya", read_only = true)
    
    class Data:
        TrainigDataJson = [
            
        ]
        


        chatbot.set_trainer(ListTrainer)
        chatbot.train(conversation)
        message = input('Your message:\n')
        response = chatbot.get_response(message);
        print(response); 

Bot.Data.
