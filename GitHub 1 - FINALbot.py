import telebot
import time
from threading import Timer
import pprint
    
bot_token = 'TOKEN'

chat_id = 'ID' #(get the chat_id of the grp chat)

pp = pprint.PrettyPrinter()
s = {'washer1' : "available", 'washer2' : "available", 'washer3' : "available", 'washer4' : "available", 'washer5' : "available", 'dryer1' : "available", 'dryer2' : "available"}

bot = telebot.TeleBot(token = bot_token)

    
def washer1reply():
    bot.send_message(chat_id, "washer1 is done, please collect your clothes soon")
    

def washer2reply():
    bot.send_message(chat_id, "washer2 is done, please collect your clothes soon")
  
def washer3reply():
    bot.send_message(chat_id, "washer3 is done, please collect your clothes soon")
 

def washer4reply():
    bot.send_message(chat_id, "washer4 is done, please collect your clothes soon")


def washer5reply():
    bot.send_message(chat_id, "washer5 is done, please collect your clothes soon")


def dryer1reply():
    bot.send_message(chat_id, "dryer1 is done, please collect your clothes soon")
    

def dryer2reply():
    bot.send_message(chat_id, "dryer2 is done, please collect your clothes soon")
  
    
#welcome msg
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'wassup homie')


#help msg
@bot.message_handler(commands=['help'])
def send_msg(message):
    bot.reply_to(message, 'use the command /view to view the status of the machines and use the commands for the machine you want to update')


#update washer1
@bot.message_handler(commands=['washer1'])
def washer1(message):
    if s['washer1'] == "available":
        s['washer1'] = "in-use"
        bot.reply_to(message, "washer1 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, washer1reply)
        r.start()
    else:
        s['washer1'] = "available"
        bot.reply_to(message, "washer1 is now 'available', thank you for updating")
   

#update washer2
@bot.message_handler(commands=['washer2'])
def washer2(message):
    if s['washer2'] == "available":
        s['washer2'] = "in-use"
        bot.reply_to(message, "washer2 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, washer2reply)
        r.start()
    else:
        s['washer2'] = "available"
        bot.reply_to(message, "washer2 is now 'available', thank you for updating")

#update washer3
@bot.message_handler(commands=['washer3'])
def washer3(message): 
    if s['washer3'] == "available":
        s['washer3'] = "in-use"
        bot.reply_to(message, "washer3 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, washer3reply)
        r.start()
    else:
        s['washer3'] = "available"
        bot.reply_to(message, "washer3 is now 'available', thank you for updating")
    
#update washer4
@bot.message_handler(commands=['washer4'])
def washer4(message):
    if s['washer4'] == "available":
        s['washer4'] = "in-use"
        bot.reply_to(message, "washer4 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, washer4reply)
        r.start()
    else:
        s['washer4'] = "available"
        bot.reply_to(message, "washer4 is now 'available', thank you for updating")
    

#update washer5
@bot.message_handler(commands=['washer5'])
def washer5(message):
    if s['washer5'] == "available":
        s['washer5'] = "in-use"
        bot.reply_to(message, "washer5 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, washer5reply)
        r.start()
    else:
        s['washer5'] = "available"
        bot.reply_to(message, "washer5 is now 'available', thank you for updating")
    
    
#update dryer1
@bot.message_handler(commands=['dryer1'])
def dryer1(message):
    if s['dryer1'] == "available":
        s['dryer1'] = "in-use"
        bot.reply_to(message, "dryer1 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, dryer1reply)
        r.start()
    else:
        s['dryer1'] = "available"
        bot.reply_to(message, "dryer1 is now 'available', thank you for updating")
    

#update dryer2
@bot.message_handler(commands=['dryer2'])
def dryer2(message):
    if s['dryer2'] == "available":
        s['dryer2'] = "in-use"
        bot.reply_to(message, "dryer2 is now 'in-use', thank you for updating, alerting you in 45 minutes")
        r = Timer(2700, dryer2reply)
        r.start()
    else:
        s['dryer2'] = "available"
        bot.reply_to(message, "dryer2 is now 'available', thank you for updating")
    

#view the dictionary
@bot.message_handler(commands=['view'])
def view(message):
    ss = pp.pformat(s)
    bot.reply_to(message, ss)

#handles any wrong input
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Incorrect input (Look at /help)")

    
while True:
    bot.polling()
