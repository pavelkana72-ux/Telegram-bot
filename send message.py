import requests

# 🔹 Вставь сюда свои данные
TOKEN = "7261655963:AAFi7UzY9zb4uPW-Qx05KoSo0qUYlNZ9jnc"
CHAT_ID ="2139926213"

MESSAGE = "🌞 Привет! Это тест от твоего Телеграм-бота Практика Равновесия."

# 🔹 Отправляем сообщение
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": MESSAGE}

response = requests.get(url, params=params)
print("Статус:", response.status_code)
print("Ответ:", response.text)