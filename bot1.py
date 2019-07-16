# import libreries

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#defining name for chatbot and defining trainer
bot=ChatBot('PRANA')
bot.set_trainer(ListTrainer)

#accessing chatterbot carpous
for files in os.listdir('C:/Users/pranamya/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/pranamya/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('You:')
    if message.strip()!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('ChatBot:It was nice talking to you. Bye')
        break
