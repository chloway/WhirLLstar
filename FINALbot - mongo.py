import telebot
import time
from threading import Timer
import pprint
from pymongo import MongoClient
import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

#mongodb
client = MongoClient("mongodb+srv://whirlly:whirlly@whirllstar-nuw33.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('whirllstar_db')
records = db.laundry_machines
    
bot_token = '834489955:AAF3ACEdIZfs3AV9bgKZbRNYZL3AXLpDuew'

chat_id = -404764664 #(get the chat_id of the grp chat)

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
    user_id = message.from_user.id
    if s['washer1'] == "available":
        s['washer1'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "washer1"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "washer1 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(270, washer1reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "washer1",
            'user' : user_id
            }).count() > 0):            
            s['washer1'] = "available"
            #remove user_id from database
            records.update_one({'name' : "washer1"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "washer1 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.")   

#update washer2
@bot.message_handler(commands=['washer2'])
def washer2(message):
    if s['washer2'] == "available":
        s['washer2'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "washer2"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "washer2 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, washer2reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "washer2",
            'user' : user_id
            }).count() > 0):
            s['washer2'] = "available"
            #remove user_id from database
            records.update_one({'name' : "washer2"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "washer2 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.") 

#update washer3
@bot.message_handler(commands=['washer3'])
def washer3(message): 
    if s['washer3'] == "available":
        s['washer3'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "washer3"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "washer3 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, washer3reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "washer3",
            'user' : user_id
            }).count() > 0):
            s['washer3'] = "available"
            #remove user_id from database
            records.update_one({'name' : "washer3"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "washer3 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.") 
    
#update washer4
@bot.message_handler(commands=['washer4'])
def washer4(message):
    if s['washer4'] == "available":
        s['washer4'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "washer4"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "washer4 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, washer4reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "washer4",
            'user' : user_id
            }).count() > 0):
            s['washer4'] = "available"
            #remove user_id from database
            records.update_one({'name' : "washer4"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "washer4 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.")
    
#update washer5
@bot.message_handler(commands=['washer5'])
def washer5(message):
    if s['washer5'] == "available":
        s['washer5'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "washer5"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "washer5 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, washer5reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "washer5",
            'user' : user_id
            }).count() > 0):
            s['washer5'] = "available"
            #remove user_id from database
            records.update_one({'name' : "washer5"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "washer5 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.")
    
#update dryer1
@bot.message_handler(commands=['dryer1'])
def dryer1(message):
    if s['dryer1'] == "available":
        s['dryer1'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "dryer1"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "dryer1 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, dryer1reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "dryer1",
            'user' : user_id
            }).count() > 0):
            s['dryer1'] = "available"
            #remove user_id from database
            records.update_one({'name' : "dryer1"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "dryer1 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.")

#update dryer2
@bot.message_handler(commands=['dryer2'])
def dryer2(message):
    if s['dryer2'] == "available":
        s['dryer2'] = "in-use"
        #update database with user_id
        records.update_one({'name' : "dryer2"}, {'$set' : {'user' : user_id}})
        bot.reply_to(message, "dryer2 is now 'in-use'. thank you for updating, alerting you in 45 minutes.")
        r = Timer(2700, dryer2reply)
        r.start()
    else:
        #check if the same user is updating
        if (records.find({
            'name' : "dryer2",
            'user' : user_id
            }).count() > 0):
            s['dryer2'] = "available"
            #remove user_id from database
            records.update_one({'name' : "dryer2"}, {'$set' : {'user' : 0}})
            bot.reply_to(message, "dryer2 is now 'available'. thank you for updating.")
        else:
            bot.reply_to(message, "sorry, you are not authorised to update.")

#view the dictionary
@bot.message_handler(commands=['view'])
def view(message):
    ss = pp.pformat(s)
    bot.reply_to(message, ss)

#handles any wrong input
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "incorrect input (look at /help)")

    
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
        time.sleep(5)
