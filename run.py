import telebot 
import os
from constants import API_Key
from telebot import types

bot = telebot.TeleBot(API_Key)

@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    username = message.from_user.username
    fullname = message.from_user.full_name
    urid = message.chat.id
    bot.reply_to(message , f"""salam {name}
    Har matni vasam beferesti barat baresh migardonam :)
    
    #Your Full name : {fullname}
    #Your username : @{username}
    #Your ID : {urid}""")
    
    bot.send_message(message.chat.id , "khobe baham ashena shodim :) be nazar adam khobi miyay")
    bot.send_message(message.chat.id , "Rasti man taze be donya omadam")
    bot.send_message(message.chat.id , "ghol midam behtar besham :D")

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message , message.text)
    

bot.polling()