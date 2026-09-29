from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Temporary storage
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Walk the dog", "completed": True}
]


# Data model
class Task(BaseModel):
    title: str
    completed: bool


@app.post("/addtask")
def create_task(task: Task):

    new_id = len(tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)

    return {
        "message": "Task added successfully",
        "title": task.title
    }



@app.get("/gettasks")
def get_tasks():

    return {
        "tasks": tasks
    }