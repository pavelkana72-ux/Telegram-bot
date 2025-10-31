import telebot
import schedule
import time
import threading
import requests

# 🔹 Твой токен от BotFather
TOKEN = "ВАШ_ТОКЕН_СЮДА"

# 🔹 ID чата (можно свой)
CHAT_ID = ВАШ_CHAT_ID

bot = telebot.TeleBot(TOKEN)

# 🔹 Ссылки на аудио и картинки
MORNING_IMAGE = "https://cdn.pixabay.com/photo/2017/01/20/00/30/yoga-1994667_1280.jpg"
EVENING_IMAGE = "https://cdn.pixabay.com/photo/2016/11/29/03/53/meditation-1868477_1280.jpg"
FOREST_AUDIO = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# 🔹 Утренняя практика
def morning_practice():
    text = (
        "🌞 Доброе утро!\n\n"
        "🧘 Сегодняшняя настройка: 'Осознанное дыхание'.\n"
        "Сделай 10 мягких вдохов, чувствуя, как просыпается тело.\n\n"
        "💬 Асана: Сурья Намаскар — Приветствие Солнцу."
    )
    bot.send_message(CHAT_ID, text)
    bot.send_photo(CHAT_ID, MORNING_IMAGE)

# 🔹 Вечерняя медитация
def evening_practice():
    text = (
        "🌙 Спокойная ясность\n\n"
        "Сядь удобно. Почувствуй, как всё стихает.\n"
        "Позволь дыханию замедлиться.\n\n"
        "✨ Практика: Наблюдение за дыханием перед сном."
    )
    bot.send_message(CHAT_ID, text)
    bot.send_photo(CHAT_ID, EVENING_IMAGE)
    bot.send_audio(CHAT_ID, FOREST_AUDIO)

# 🔹 Воскресное пробуждение (10:00)
def sunday_forest():
    text = (
        "🌿 Доброе воскресное утро!\n\n"
        "Сегодня — мягкая прогулка по внутреннему лесу.\n"
        "Слушай, дыши, будь.\n\n"
        "🕊️ Практика: 15 минут тишины с природой."
    )
    bot.send_message(CHAT_ID, text)
    bot.send_audio(CHAT_ID, FOREST_AUDIO)

# 🔹 Расписание
schedule.every().day.at("06:10").do(morning_practice)
schedule.every().day.at("22:45").do(evening_practice)
schedule.every().sunday.at("10:00").do(sunday_forest)

# 🔹 Поток для расписания
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(30)

threading.Thread(target=run_schedule).start()

# 🔹 Обработка сообщений
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🧘 Привет! Я помогу тебе практиковать йогу и медитацию каждый день.")

bot.polling(none_stop=True)