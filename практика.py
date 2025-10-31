import telebot
import schedule
import time
import random

# 🔹 Вставь свои данные
TOKEN = "8479549337:AAHT5Kn7OvBqYrF61rVLNyG8ZYtsAOGFRYk"
CHAT_ID = "2139926213"

bot = telebot.TeleBot(TOKEN)

# 🌞 Утренняя практика
def morning_practice():
    bot.send_message(CHAT_ID, "🌞 Доброе утро.\nСделай вдох, почувствуй тело. Сегодня — возможность быть заново.")
    image_url = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80"
    bot.send_photo(CHAT_ID, image_url, caption="🧘‍♂ Асана для пробуждения: Сурья Намаскар (Приветствие Солнцу).")

# 🌙 Вечерняя практика
def evening_relax():
    bot.send_message(CHAT_ID, "🌙 День завершается.\nПозволь уму раствориться в тишине. Всё хорошо.")
    audio_url = "https://cdn.pixabay.com/download/audio/2022/03/01/audio_1b3a6e1e6a.mp3"
    bot.send_audio(CHAT_ID, audio_url, caption="🎧 Небольшая аудио-медитация перед сном.")

# 🌤 Воскресное послание
sunday_messages = [
    "🌤 Воскресенье.\n\nСегодня не нужно искать путь — он уже под ногами.\nПозволь миру дышать через тебя. Просто будь.",
    "🌾 День покоя.\n\nТы — не делающий. Всё совершается само.\nСлушай, как жизнь звучит без усилий.",
    "🌸 Сегодня можно ничего не менять.\nНи в себе, ни в мире.\nПросто смотри — и увидишь совершенство простоты.",
    "🍃 Воскресный ветер шепчет: «Ты уже дома.»\nНикуда не спеши.\nКаждый миг — вечность в движении.",
    "🌙 Пусть этот день будет как дыхание: без цели, без спешки, без края.\nПросто осознавание — без формы и слов."
]

def sunday_message():
    msg = random.choice(sunday_messages)
    bot.send_message(CHAT_ID, msg)

    image_url = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1200&q=80"
    bot.send_photo(CHAT_ID, image_url, caption="🌲 Утро в лесу. Всё тихо, всё живо.")

    audio_url = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_05f4f84b9e.mp3"
    bot.send_audio(CHAT_ID, audio_url, caption="🍃 Звуки леса. Пусть утро течёт мягко.")

# 🕒 Расписание
schedule.every().day.at("06:10").do(morning_practice)
schedule.every().day.at("22:45").do(evening_relax)
schedule.every().sunday.at("10:00").do(sunday_message)

bot.send_message(CHAT_ID, "✨ Бот запущен и готов напоминать о практике!")

# 🔁 Цикл выполнения
while True:
    schedule.run_pending()
    time.sleep(30)