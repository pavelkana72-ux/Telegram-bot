import telebot
import schedule
import time
import random
import threading
from flask import Flask

# 🔹 Твои данные
TOKEN = "8479549337:AAHT5Kn7OvBqYrF61rVLNyG8ZYtsAOGFRYk"
CHAT_ID = "2139926213"

bot = telebot.TeleBot(TOKEN)

# 🌞 Утренняя практика
def morning_practice():
    try:
        bot.send_message(CHAT_ID, "🌞 Доброе утро.\nСделай вдох, почувствуй тело. Сегодня — возможность быть заново.")
        image_url = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80"
        bot.send_photo(CHAT_ID, image_url, caption="🧘‍♂ Асана для пробуждения: Сурья Намаскар (Приветствие Солнцу).")
    except Exception as e:
        print("Ошибка утренней практики:", e)

# 🌙 Вечерняя практика
def evening_relax():
    try:
        bot.send_message(CHAT_ID, "🌙 День завершается.\nПозволь уму раствориться в тишине. Всё хорошо.")
        audio_url = "https://cdn.pixabay.com/download/audio/2022/03/01/audio_1b3a6e1e6a.mp3"
        bot.send_audio(CHAT_ID, audio_url, caption="🎧 Небольшая аудио-медитация перед сном.")
    except Exception as e:
        print("Ошибка вечерней практики:", e)

# 🌅 Ключ дня
def key_of_the_day():
    try:
        bot.send_message(CHAT_ID,
            "🌅 Ключ дня.\nЗакрой глаза. Почувствуй дыхание.\nСпроси себя: «Что живое во мне сегодня?»\nПервое слово, чувство или образ — и есть ключ дня.")
        image_url = "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1200&q=80"
        bot.send_photo(CHAT_ID, image_url, caption="✨ Пусть это будет твоим направлением сегодня.")
    except Exception as e:
        print("Ошибка ключа дня:", e)

# 🌤 Воскресное послание
sunday_messages = [
    "🌤 Воскресенье.\nСегодня не нужно искать путь — он уже под ногами.\nПозволь миру дышать через тебя. Просто будь.",
    "🌾 День покоя.\nТы — не делающий. Всё совершается само.\nСлушай, как жизнь звучит без усилий.",
    "🌸 Сегодня можно ничего не менять.\nНи в себе, ни в мире.\nПросто смотри — и увидишь совершенство простоты.",
    "🍃 Воскресный ветер шепчет: «Ты уже дома.»\nНикуда не спеши.\nКаждый миг — вечность в движении.",
    "🌙 Пусть этот день будет как дыхание: без цели, без спешки, без края.\nПросто осознавание — без формы и слов."
]

def sunday_message():
    try:
        msg = random.choice(sunday_messages)
        bot.send_message(CHAT_ID, msg)
        image_url = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1200&q=80"
        bot.send_photo(CHAT_ID, image_url, caption="🌲 Утро в лесу. Всё тихо, всё живо.")
        audio_url = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_05f4f84b9e.mp3"
        bot.send_audio(CHAT_ID, audio_url, caption="🍃 Звуки леса. Пусть утро течёт мягко.")
    except Exception as e:
        print("Ошибка воскресного послания:", e)

# 🕒 Расписание
schedule.every().day.at("06:10").do(morning_practice)
schedule.every().day.at("07:30").do(key_of_the_day)
schedule.every().day.at("22:45").do(evening_relax)
schedule.every().sunday.at("10:00").do(sunday_message)

# 🔁 Планировщик в отдельном потоке
def run_schedule():
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            print("Ошибка расписания:", e)
        time.sleep(30)

threading.Thread(target=run_schedule, daemon=True).start()

# 🌐 Flask-сервер для Render (чтобы не засыпал)
app = Flask(__name__)

@app.route("/")
def home():
    return "🧘‍♂ Meditation bot is alive."

# 🔔 Стартовое сообщение
try:
    bot.send_message(CHAT_ID, "✨ Бот запущен и готов напоминать о практике!")
except:
    print("Не удалось отправить стартовое сообщение (возможно, ограничение Telegram).")

# 🚀 Запуск Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)