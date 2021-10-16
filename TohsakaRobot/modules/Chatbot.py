#Setting up Chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Train the bot
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")
from TohsakaRobot import TOKEN
#Setting telegram things
# Refer README for more details
import logging
from telegram.ext import CommandHandler,MessageHandler, Filters,Updater
updater = Updater(token=TOKEN)


def byww(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a chat bot")


byww_handler = CommandHandler('byww', byww)
dispatcher.add_handler(byww_handler)

def reply(bot, update):
    userText=update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=str(english_bot.get_response(userText)))

reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)
