from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


chatbot = ChatBot("ilya")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

message = input('Your message:\n')
response = chatbot.get_response(message);
print(response); 
