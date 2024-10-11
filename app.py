import time
import telegram

# Токен бота
bot_token = '7764076864:AAF-0KuyEufJIS7mC6u1nT2ZwA0YXKu>

# ID канала
channel_id = -1001746118789

# Текст сообщения
message_text = "Происходит взлом жопы"

# Создаем бота
bot = telegram.Bot(token=bot_token)

# Получаем ID последнего сообщения
last_message_id = None

# Функция для обновления точек
def update_dots():
  dots = "."
  while True:
    yield dots
    dots += "."
    if len(dots) > 5:
      dots = "."
    time.sleep(0.1)

# Получаем итератор для обновления точек
dots_iterator = update_dots()

# Бесконечный цикл для отправки сообщений
while True:
  try:
    # Получаем следующую комбинацию точек
    dots = next(dots_iterator)

    # Проверяем, отправлено ли сообщение ранее
    if last_message_id is None:
      # Отправляем сообщение в канал
      last_message = bot.send_message(chat_id=channel_i>
      last_message_id = last_message.message_id

    else:
      # Обновляем сообщение
      bot.edit_message_text(
        chat_id=channel_id,
        message_id=last_message_id,
        text=f"{message_text}{dots}"
      )
