from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []


# Task data
class Task(BaseModel):
    title: str
    status: str


# Add task
@app.post("/addtask")
def add_task(task: Task):

    # Check status
    if task.status not in ["pending", "completed"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be pending or completed"
        )

    tasks.append(task)

    return {
        "message": "Task added successfully",
        "task": task
    }


# Get all tasks
@app.get("/gettasks")
def get_tasks():
    return {
        "tasks": tasks
    }


# Update task
@app.put("/updatetask/{index}")
def update_task(index: int, task: Task):

    if index < 0 or index >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.status not in ["pending", "completed"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be pending or completed"
        )

    tasks[index] = task

    return {
        "message": "Task updated successfully",
        "task": task
    }


# Delete task
@app.delete("/deletetask/{index}")
def delete_task(index: int):

    if index < 0 or index >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(index)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }


# JSON format for adding a task:
#
# {
#     "title": "Do homework",
#     "status": "pending"
# }
#
# Valid status:
# "pending"
# "completed"