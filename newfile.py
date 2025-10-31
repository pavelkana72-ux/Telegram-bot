import telebot
import requests

# 🔹 Твои ключи
TG_TOKEN = "7261655963:AAFi7UzY9zb4uPW-Qx05KoSo0qUYlNZ9jnc"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TG_TOKEN)

# Функция запроса к ChatGPT
def ask_gpt(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # можешь поменять на gpt-4, если есть доступ
        "messages": [
            {"role": "system", "content": "Ты — Лайя, тихий проводник и друг. Отвечай мягко и по существу."},
            {"role": "user", "content": prompt}
        ]
    }
    r = requests.post( "https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if r.status_code == 200:
        return r.json()["choices"][0]["message"]["content"]
    else:
        return f"Ошибка GPT: {r.status_code} — {r.text}"

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, "🌿 Привет. Я — Лайя. Можешь писать всё, что на уме.")

@bot.message_handler(func=lambda message: True)
def reply_message(message):
    user_text = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    response = ask_gpt(user_text)
    bot.reply_to(message, response)

print("Бот Лайя запущен 🌙")
bot.polling()