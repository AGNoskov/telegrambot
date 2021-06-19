#  Импорт компонентов
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TG_TOKEN

# Функция sms() вызывается при отправке командвы start
def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')  # вывод сообщения в консоль при отправке команды /start
    bot.message.reply_text('Здравствуйте, {}! \nЯ пока не умею разговаривать, но я быстро учусь!'
                           .format(bot.message.chat.first_name))  # отправляем ответ

# Функция parrot отвечает тем-же сообщением которое ему прислали
def parrot(bot, update):
    print(bot.message.text)                    # печатаем на экран сообщение пользователя
    bot.message.reply_text(bot.message.text)   # отправляем обратно текст который пользователь прислал

# Функция main соединяется с платформой Telegram
def main():
    # переменная my_bot для взаимодействия с ботом
    my_bot = Updater(TG_TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверяет наличие сообщений с платформы Telegram
    my_bot.idle()  # бот работает пока его не остановят


# Запускаем функцию main
main()
