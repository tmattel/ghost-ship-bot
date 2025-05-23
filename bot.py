# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(token)
some_api = some_api_lib.connect(some_api_token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Wallet', 'Buy Postage')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Settings', 'Support')

ReplyKeyboardMarkup = keyboard1.resize_keyboard, keyboard2.resize_keyboard  = True, True
