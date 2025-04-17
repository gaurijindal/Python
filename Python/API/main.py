from fastapi import FastAPI
from typing import List,Optional
from enum import Enum,IntEnum
from pydantic import BaseModel, Field

api=FastAPI()

#GET, POST, PUT, DELETE

all_todos=[
    {'todo_id':1,'todo_name':'Shopping','todo_description':'Shop for < 500'},
{'todo_id':2,'todo_name':'Class','todo_description':'Class at 6pm'},
{'todo_id':3,'todo_name':'Movie','todo_description':'movie at 12pm'},
{'todo_id':4,'todo_name':'Meet','todo_description':'contact your vendor'},
{'todo_id':5,'todo_name':'Check_deleviry','todo_description':'product delivery'},
]

@api.get('/')
def index():
    return {'Message':"hello world"}

#path parameter-> parameter should be in the path
# localhost:8000/todos/2

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id']==todo_id:
            return {'result':todo}


#Queary parameter
#localhost:8000/todos?first_n=3

@api.get('/todos')
def get_todo(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id=max(todo['todo_id'] for todo in all_todos)+1
    new_todo={
        'todo_id':new_todo_id,
        'todo_name':todo['todo_name'],
        'todo_description':todo['todo_description']
    }
    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}')
def update_todo(todo_id: int,updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id']==todo_id:
            todo['todo_name']=updated_todo['todo_name']
            todo['todo_description']=updated_todo['todo_description']
            return todo
    return "error,not found"

@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id']==todo_id:
            deleted_todo=all_todos.pop(index)
            return deleted_todo
    return "error,not found"


#fastapi dev main.py