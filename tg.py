from datetime import datetime, timedelta

import telebot
import requests
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler

token_bot = '8804374991:AAFn0ebwEd3aHRP92prnVniOh2hzA7-bT9Q'
bot = telebot.TeleBot(token_bot)

scheduler = BackgroundScheduler()
scheduler.start()
dranked = 0
normal = 2100
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! я бот для напоминания о воде. Чтобы посмотреть список команд, напиши /help')

@bot.message_handler(commands=['help'])
def help_message(message):
    commands = [
        "/start - запуск бота",
        "/help - список команд",
        "/status - статус напоминаний",
        "/drank - отметить, что выпил воду",    
        "/setremind - установить напоминание о воде ",
    ]
    bot.send_message(message.chat.id, "\n".join(commands))

@bot.message_handler(commands=['drank'])
def drank_message(message):
    try:
        amount = int(message.text.split()[1])
        global dranked  
        dranked += amount
        bot.reply_to(message, f"Записал {amount} мл воды. Всего: {dranked} мл.")
    except:
        bot.reply_to(message, "Используй формат: /drank 250")

@bot.message_handler(commands=['status'])
def status_message(message):
    bot.send_message(message.chat.id, 
        f"Ты уже выпил {dranked} мл воды 💧\n"
        f"Осталось: {normal - dranked} мл до нормы ({normal} мл)")



@bot.message_handler(commands=['setremind'])
def set_remind(message):
    try:
        minutes = int(message.text.split()[1])  # пример: /setremind 30
        run_time = datetime.now() + timedelta(minutes=minutes)
        scheduler.add_job(
            func=lambda: bot.send_message(message.chat.id, "Напоминание: пора выпить воды!"),
            trigger="date",
            run_date=run_time
        )
        bot.send_message(message.chat.id, f"Окей, напомню через {minutes} минут!")
    except:
        bot.send_message(message.chat.id, "Используй формат: /setremind 30")


bot.infinity_polling()