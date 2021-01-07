import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = "1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ"


def start(update: Update, context: CallbackContext):
    delay_group(update, context, "Fancy text")


def delay_group(update: Update, context: CallbackContext, text: str):
    if update.effective_message.reply_to_message:
        update.effective_message.reply_to_message.reply_text(
            text=text,
            parse_mode=ParseMode.HTML)
    else:
        reply_message = context.bot.send_message(
            chat_id=update.message.chat_id,
            text=text,
            parse_mode=ParseMode.HTML)
        context.job_queue.run_once(delete, 30, context=reply_message.chat_id, name=str(reply_message.message_id))

    update.effective_message.delete()


def delete(context: CallbackContext):
    context.bot.delete_message(chat_id=str(context.job.context), message_id=context.job.name)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("test", start))

    PORT = int(os.environ.get('PORT', 5000))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.setWebhook('https://ptb-realme.herokuapp.com/' + TOKEN)

    updater.start_polling()
    updater.idle()
