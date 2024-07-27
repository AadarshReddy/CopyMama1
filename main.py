from telegram.ext import Updater, CommandHandler

TOKEN = '7423032401:AAHP3yAaGLSLCnXIY-uINVvG-tpog0ZGnoU'

def start(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(f'Your chat ID is: {603004587}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
