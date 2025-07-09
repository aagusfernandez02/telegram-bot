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