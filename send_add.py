from time import sleep
from telebot import TeleBot
import sqlite3
from config import token

bot = TeleBot(token)

conndb = sqlite3.connect('tgbot.sqlite3', check_same_thread=False)

def get_followers():
    cursor = conndb.cursor()
    cursor.execute('SELECT user_id FROM followers')
    followers =cursor.fetchall()
    return followers

if __name__=='__main__':
    while True:
        followers = get_followers()
        for follower in followers:
            bot.send_message(follower[0], 'Hello world!')
        sleep(1)    
    