import translators as ts
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Type a word or a short phrase, and this bot will translate it to English, if possible ;)')


def echo(update, context):
    """Echo the user message."""
    st = update.message.text
    q=ts.google(st, professional_field='general', to_language = 'es')
    '''try:
        s = wikipedia.search(st)
        if len(s) == 0:
            q = 'Try again, no such page found'
        else:
            q = (wikipedia.summary(s[0], sentences= 2, auto_suggest = False) )
    except wikipedia.exceptions.DisambiguationError as e:
        q = wikipedia.summary(e.options[0], auto_suggest = False, sentences = 2)
    except wikipedia.exceptions.PageError as e2:
        q = 'No such page found, try again, maybe with a different name?'
    except wikipedia.exceptions.WikipediaException:
        q =('Not a valid input, please try again with a valid input')
'''

    update.message.reply_text(q)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater('YOUR BOT\'S ACCESS KEY', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
