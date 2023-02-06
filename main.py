import requests
import telebot

# API key and base URL for the OpenWeatherMap API
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


# Set up the Telegram bot
bot = telebot.TeleBot('your_telegram_bot_token')


# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hi! Send me your location to get the weather.')


# Handle location messages
@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    url = BASE_URL + 'lat=' + str(latitude) + '&lon=' + str(longitude) + '&appid=' + API_KEY
    response = requests.get(url).json()
    temperature = response['main']['temp'] - 273.15
    weather = response['weather'][0]['description']
    bot.reply_to(message, 'The temperature is {:.1f}°C and the weather is {}.'.format(temperature, weather))


# Start the bot
bot.polling()
