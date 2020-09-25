import os
from log_helper import set_logger
import traceback
import html
import json
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters
from moe_fill import sign_moe

log = set_logger("telegram-bot")
CHAT_ID = int(os.environ['CHAT_ID'])
DEV_CHAT_ID = int(os.environ['DEV_CHAT_ID'])


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"chat id = {update.message.chat_id}")
    update.message.reply_text("Welcome to Kinderbot, this bot will sign covid health certificates for you.")


def error_handler(update: Update, context: CallbackContext):
    log.error(msg="Exception while handling an update:", exc_info=context.error)

    # format error to send back to telegram
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb = ''.join(tb_list)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False))}</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb)}</pre>"
    )
    context.bot.send_message(chat_id=DEV_CHAT_ID, text=message, parse_mode=ParseMode.HTML)


def sign(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action="upload_photo")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=sign_moe())


def main():
    updater = Updater(token=os.environ['TELEGRAM_TOKEN'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('sign', sign, filters=Filters.chat(CHAT_ID)))
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
