from telegram import Update
from telegram.ext import ContextTypes

from models.Todo import Todo
from models.TodoList import todo_list

class TodoController:

    @staticmethod
    async def add_todo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        command = update.message.text.split()[0]
        title = str(update.message.text.split(command)[1])
        todo = Todo(title)
        todo_list.append(todo)
        await update.message.reply_text("Tarea agregada") 
    
    @staticmethod
    async def list_todos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if( len(todo_list) == 0 ):
            await update.message.reply_text("No hay tareas pendientes")
            return
        
        answer = ""
        for i, todo in enumerate(todo_list):
            answer = answer + f"{i+1} - {'✔️' if todo.is_completed else '❌'} {todo.title}\n"
        
        await update.message.reply_text(answer) 

    @staticmethod
    async def check_todo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        index = int(context.args[0])
        if( index > len(todo_list) or index <= 0 ):
            await update.message.reply_text("ERROR: Tarea inexistente")
            return
        
        todo_list[index-1].set_completed()
        await update.message.reply_text(f"Tarea {index} marcada completada") 
        await TodoController.list_todos(update, context)

    @staticmethod
    async def clear_todos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        todo_list.clear()
        await update.message.reply_text("Tareas borradas")
    