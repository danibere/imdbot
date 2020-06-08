#!/usr/bin/env python
# coding: utf-8

# In[3]:


TOKEN = '1190834838:AAGKYubjO91SaMTs-8zrNe30BJ3EK9rvWDo'
'@imdb_assistbot'
import telebot
import imdb
import dbworker
import config
ia = imdb.IMDb()
bot = telebot.TeleBot('1190834838:AAGKYubjO91SaMTs-8zrNe30BJ3EK9rvWDo')

   
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! I can help you find the filmography of your favourite actor. Actor or actress (yes, I am a femenist)?')
    dbworker.set_state(message.chat.id, config.States.S_GENDER.value)

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Let's start again. Type actor or actress?")
    dbworker.set_state(message.chat.id, config.States.S_GENDER.value)
    
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_GENDER.value)
def user_entering_gender(message):
    # А вот тут сделаем проверку
    if message.text.lower() == "actor":
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Great! What is his name?")
        dbworker.set_state(message.chat.id, config.States.S_MNAME.value)
        return 
    elif message.text.lower() == "actress":
        bot.send_message(message.chat.id, "Great! What is her name?")
        dbworker.set_state(message.chat.id, config.States.S_FNAME.value)
        return
    else:
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "You are not cooperating! Please, type 'actor' or 'actress'.")
@bot.message_handler(content_types=["text"], func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_MNAME.value)

def user_entering_name(message):
    z = message.text.lower() 
    people = ia.search_person(z)
    code = people[0].personID
    actor_results = ia.get_person_filmography(code)
    for rating in range(10): 
        movie_name = actor_results['data']['filmography'][0]['actor'][rating]
        t = str(movie_name)
        bot.send_message(message.chat.id, str(t))
    bot.send_message(message.chat.id, "press '/reset' to try someone else")
@bot.message_handler(content_types=["text"], func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FNAME.value)
def user_entering_name(message):
    z = message.text.lower() 
    people = ia.search_person(z)
    code = people[0].personID
    actor_results = ia.get_person_filmography(code)
    for rating in range(10): 
        movie_name = actor_results['data']['filmography'][0]['actress'][rating]
        t = str(movie_name)
        bot.send_message(message.chat.id, str(t))
    bot.send_message(message.chat.id, "press '/reset' to try someone else")
        
bot.polling()


# In[ ]:





# In[ ]:




