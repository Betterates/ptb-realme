import logging
import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ'
GROUP = -1001374176745  # -1001327617858

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hey :)\nI'm under construction.")


def admins(update, context):
    delay_group(update, context,
                "<u>Group's staff</u>"
                "\n\n<b>Organization</b>"
                "\n@aakaah00001"
                "\n@Prashant_Choudhary"
                "\n@PacificPC"
                "\n\n<b>Moderators</b>"
                "\n@pentexnyx"
                "\n@Abhishek2376")


def ask(update, context):
    delay_group(update, context, "<u>How to ask</u>"
                                 "\n\n<b>1. Formulate the question</b>"
                                 "\nMake sure to include:"
                                 "\n· The device you use"
                                 "\n· The latest software installed"
                                 "\n· What you want to do"
                                 "\n· What you have tried already"
                                 "\n· Why you want to do that"
                                 "\n· What benefits you expected"
                                 "\n· The output you got"
                                 "\n\n<b>2. Wait for a response</b>"
                                 "\nGive the community 48h to answer your question. The needed expert might not be "
                                 "available all the time, so receiving an answer might take a bit. "
                                 "\n\n<b>3. No answer yet</b>"
                                 "\nUse /experts and tag the experts, whose segment fits your issue."
                                 "\nIf you didn't receive an answer after a week, use /form and fill out "
                                 "the "
                                 "linked form. "
                                 "\n\nThese suggestions enable us to provide you with better answers "
                                 "quicker and "
                                 "will keep this chat more focused.")


def help(update, context):
    delay_group(update, context,
                "<u>Commands</u>"
                "\n\n<b>/help</b>"
                "\nDisplay this message"
                "\n\n<b>/admins</b>"
                "\nShow this group\'s staff"
                "\n\n<b>/rules</b>"
                "\nShow this group\'s rules"
                "\n\n<b>/experts</b>"
                "\nList experts for different segments"
                "\n\n<b>/gcam</b>"
                "\nLatest GCam release and configurations"
                "\n\n<b>/sdmaid</b>"
                "\nLatest release of the best cleaner out there"
                "\n\n<b>/android11</b>"
                "\nOfficial roadmap for the Early Access of RealmeUI 2.0"
                "\n\n<b>/ask</b>"
                "\nHow to ask questions properly"
                "\n\nContact @pentexnyx if you face any issues with me 🤖"
                "\n<code>version 0.8</code>")


def experts(update, context):
    delay_group(update, context, "<u>Community experts</u>"
                                 "\n\n<b>Software issues</b>"
                                 "\n@Abhishek2376"
                                 "\n@Dhairya3391"
                                 "\n@pentexnyx"
                                 "\n\n<b>Hardware issues</b>"
                                 "\n@Abhishek2376"
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
    delay_group(update, context,
                "<u>Google Camera</u>"
                "\n\n<b>Latest Release</b>"
                "\n· <a href='https://t.me/realme_support/47467'>Urnyx05-v2.4</a>"
                "\n\nUrnyx05's releases work well on most Realme devices. Take a look at @googlecameraport for other "
                "releases. "
                "\n\n\n<b>Configurations</b>"
                "\n· <a href='https://t.me/realme_support/20129'>new-natural</a>"
                "\n· <a href='https://t.me/realme_support/20127'>X2 Pro terev</a>"
                "\n\nTo enable these configurations, place them in <b>Internal Storage > GCam > Configs7</b>. "
                "\n\nThen go to your GCam and press on the bottom left (next to the camera switch button) a few "
                "times. A dialog should appear where your can select the desired configuration. "
                "\n\nFeel free to fiddle around with LibPatcher (in GCam's settings) a little to "
                "shape the image output so that it fits your needs.")


def sdmaid(update, context):
    delay_group(update, context,
                "<u>SD Maid</u>"
                "\n\n<b>Latest Release</b>"
                "\n· <a href='https://t.me/realme_support/52321'>Pro-v5.0.1</a>"
                "\n\nThis is an excellent cleaning app, which also takes care of databases, duplicates, caches etc. "
                "and enables you to freeze the apps you don't need.")


def rules(update, context):
    delay_group(update, context,
                "<u>Group's rules</u>"
                "\n\n<b>1. Language</b>"
                "\nPlease use English or Hindi as an alternative."
                "\n\n<b>2. Links</b>"
                "\nSending links is not permitted."
                "\n\n<b>3. Forwarding</b>"
                "\nForwarding messages from other channels is not permitted"
                "\n\n<b>4. Respect</b>"
                "\nWe're all one big community. Don't be rude."
                "\n\n<b>5. Spam</b>"
                "\nAvoid sending stuff multiple times. Flooding the chat won't give you more attention."
                "\n\n<b>6. Files</b>"
                "\nAvoid sending files over 50Mb, if not ultimately needed."
                "\n\n<b>7. Advertisements</b>"
                "\nSelf-promotion is not permitted."
                "\n\n<b>8. Content</b>"
                "\nGore, porn and anything alike is absolutely prohibited.")


def form(update, context):
    delay_group(update, context,
                "If your issue is not resolved by the community after a week, you can also contact the developers."
                "\n\nPlease don't abuse this possibility, so that Realme developers can focus on developing."
                "\n\nAccess form 📝"
                "\n\nhttps://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2"
                "-VGJasy8VU_BLsFA/viewform")


def android11(update, context):
    delay_group(update, context,
                "<u>Realme UI 2.0</u>"
                "\n\n<a href='https://static.c.realme.com/IN/wm-thread/1323470129358438400.jpg'>Official Roadmap</a>"
                "\n\n<b>Early Access</b>"
                "\nThe timeline is for the first wave of early access rollout only. The version for the corresponding "
                "model will be released within the above mentioned month in batches, not at the beginning of the "
                "month."
                "\n\n<b>Stable release</b>"
                "\nWill be pushed to all users over a period of time, minimum 2 months after early access."
                "\n\nRelax and wait what happens 😎")


def delay_group(update, context, text):
    # update.message.delete() # REQUIRES ADMIN!!!

    if update.message.chat_id == -1001374176745:
        reply_message: telegram.Message = context.bot.send_message(chat_id=update.message.chat_id, text=text,
                                                                   parse_mode=telegram.ParseMode.HTML)
    else:
        reply_message: telegram.Message = update.message.reply_text(
            "Command can only be used in the community support group.",
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(text="Join »", url="https://t.me/realme_support")))

    context.job_queue.run_once(delete, 300, context=update.message.chat_id, name=str(reply_message.message_id))


def delete(context):
    context.bot.delete_message(chat_id=context.job.context, message_id=context.job.name)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("admins", admins))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("gcam", gcam))
    dp.add_handler(CommandHandler("sdmaid", sdmaid))
    dp.add_handler(CommandHandler("experts", experts))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("ask", ask))
    dp.add_handler(CommandHandler("android11", android11))
    dp.add_handler(CommandHandler("form", form))

    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://pxnx-tg-bot-test.herokuapp.com/' + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
