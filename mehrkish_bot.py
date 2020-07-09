#!/usr/bin/python3.8.0
# -*- coding:utf-8 -*-
from telegram.ext import Updater, MessageHandler, Filters
from flask import Flask, request
import os
TOKEN = "1074001017:AAFElDP-LJLNP2nxBhmWKOB7n3LHjziDJmk"
updater = Updater(TOKEN)
server = Flask(__name__)

def message_filter(bot, update):

    if update.message.caption != None:
    	if update.message.caption.encode('utf-8').find("#نقل") != -1:
    	    bot.forward_message(chat_id="@reading_campagin_channel", from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    else:
    	if update.message.text.encode('utf-8').find("#نقل") != -1:
    		bot.send_message(chat_id = "@reading_campagin_channel", text = update.message.text)
    	elif update.message.text.encode('utf-8').find("#قرار") != -1:
    	    bot.forward_message(chat_id="@reading_tasks", from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    	    bot.send_message(chat_id = update.message.chat_id, text = "Good luck dear {}!👍🤞".format(update.message.from_user.first_name))


updater.dispatcher.add_handler(MessageHandler(Filters.all, message_filter))

updater.idle()

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://agile-beyond-02613.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
