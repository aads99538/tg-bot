import telebot
import time

TOKEN = '7764076864:AAF-0KuyEufJIS7mC6u1nT2ZwA0YXKuYlhY'
CHANNEL_ID = '-1001746118789'

bot = telebot.TeleBot(TOKEN)

message_id = None

while True:
    dots = '.' * ((time.time() // 1) % 4)  # Обновление точек
    message_text = f'происходит взлом жопы{dots}'
    
    if message_id:
        # Обновляем сообщение
        bot.edit_message_text(message_text, chat_id=CHANNEL_ID, message_id=message_id)
    else:
        # Отправляем первое сообщение
        sent_message = bot.send_message(CHANNEL_ID, message_text)
        message_id = sent_message.message_id

    time.sleep(1)  # Обновление каждую секунду
