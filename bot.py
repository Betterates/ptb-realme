import logging
import os

import telegram
from telegram.ext import Updater, CommandHandler

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    private(update, "Hello, human 🤖"
                    "\nI will guide you through finding a solution."
                    "\n\n<i>If you face any issues with this bot, contact @pentexnyx</i>")


def help(update, context):
    """Send a message when the command /help is issued."""
    html(update.message, "<u>Commands</u>"
                         "\n\n<b>/help</b>"
                         "\nDisplay this menu"
                         "\n\n<b>/admins</b>"
                         " \nShow the support group\'s staff"
                         "\n\n<b>/experts</b>"
                         "\nList experts for different segments"
                         "\n\n<b>/gcam</b>"
                         "\nLatest Gcam release and configurations")


def admins(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Group's staff</u>"
                          "\n\n<b>Organization</b>"
                          "\n@aakaah00001"
                          "\n@Prashant_Choudhary"
                          "\n@PacificPC"
                          "\n\n<b>Moderators</b>"
                          "\n@pentexnyx"
                          "\n@Abhishek2376")


def experts(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Community experts</u>"
                          "\n\n<b>Software issues</b>"
                          "\n@Abhishek2376"
                          "\n@Dhairya3391"
                          "\n@pentexnyx"
                          "\n\n<b>Hardware issues</b>"
                          "\n- no expert yet -"
                          "\n\n<b>Updates and apps</b>"
                          "\n@Abhishek2376"
                          "\n@Dhairya3391"
                          "\n\n<b>Phone recommendations</b>"
                          "\n@Abhishek2376"
                          "\n@pentexnyx"
                          "\n\n<b>Flashing</b>"
                          "\n- no expert yet -"
                          "\n\n<b>Android development</b>"
                          "\n@pentexnyx"
                          "\n\n<b>Realme ecosystem</b>"
                          "\n- no expert yet -")


def gcam(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Google Camera</u>"
                          "\n\n<b>Latest Release</b>"
                          "\n<a href='https://t.me/realme_support/47467'>Urnyx05-v2.4</a>"
                          "\n\n<b>Configurations</b>")


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def html(message, text):
    message.reply_text(text=text, parse_mode=telegram.ParseMode.HTML)


# def markdown(message, text):
# message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def private(message, text):
    # if message.chat_id > 0:
    html(message, text)
    # else:
    message.reply_text("I'm shy. Please talk to me alone."
                       "\n@realme_community_support_bot")


def group(message, text):
    if message.chat_id == -1001374176745:
        html(message, text)
    else:
        message.reply_text("Please join the group:"
                           "\n@realme_support")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("admins", admins))
    dp.add_handler(CommandHandler("gcam", gcam))
    dp.add_handler(CommandHandler("experts", experts))

    # on noncommand i.e message - echo the message on Telegram
    #   dp.add_handler(MessageHandler(Filters.text, echo)) yyyyyyyyyyyyyy

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://pxnx-tg-bot-test.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
