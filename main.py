from telegram import Update
from controllers.TodoController import TodoController
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Controllers


# App settings
app = ApplicationBuilder().token('7217581945:AAGJVTkq9MWDlCwsMWktk_G1rGqV7pJbzA8').build()

# Handlers
app.add_handler(CommandHandler("add", TodoController.add_todo))
app.add_handler(CommandHandler("list", TodoController.list_todos)) 

app.run_polling(allowed_updates=Update.ALL_TYPES)


# `hupper -m main.py` (Utilizo 'hupper' para correr la app como demonio para que se actualice con cada cambio)