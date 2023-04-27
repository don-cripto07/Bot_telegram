from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler, ConversationHandler

import logging, time, re

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.

START_ONE = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	"""Send a message when the command /start is issued."""
	user = update.effective_user
	teclado= [
        [
            InlineKeyboardButton("Transaction Issue", callback_data= 'one'),
            InlineKeyboardButton("Doubts", callback_data= 'two'),
        ]    
    ]
	reply_markup = InlineKeyboardMarkup(teclado)
	await update.message.reply_text("Hello !"'\n' "Welcome to Trocador Support."'\n'"Please inform if you need help about one of your transactions or any doubt about the service\n", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def transaction (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text ("Please inform transaction ID of your request")

async def doubts (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await print ("Please Please wait a moment")
	
async def verificar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	query = update.callback_query
	await query.answer()
	print (query.data)
	print(type(query.data))
	print(type(update.callback_query))

def main() -> None:
	
	with open ("token.txt") as token:
		token2 = token.read() 
	application = Application.builder().token(token2).build()

	"""application.add_handler(CommandHandler("start", start))"""
	application.add_handler(CommandHandler("help", help_command))
	conv_handler = ConversationHandler(
		entry_points=[CommandHandler("start", start)],
        states= {START_ONE :[
					CallbackQueryHandler(transaction, pattern= 'one'),
					CallbackQueryHandler(doubts, pattern= 'two')

					
            ]},
        fallbacks=[CommandHandler("start", start)],
    )
	
	
	application.add_handler(conv_handler)
	application.add_handler(CallbackQueryHandler(verificar))
	print ('Rodando')
    # Run the bot until the user presses Ctrl-C
	application.run_polling()


if __name__ == "__main__":
    main()
