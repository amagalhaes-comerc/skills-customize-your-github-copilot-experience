"""
Starter code para API de Lista de Tarefas com FastAPI

Instruções:
1. Instale as dependências: pip install fastapi uvicorn
2. Execute o servidor: uvicorn main:app --reload
3. Acesse a documentação: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API de Lista de Tarefas")

# Armazenamento em memória
tasks_db = {}
task_counter = 0

# Modelo de dados usando Pydantic
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


@app.get("/")
def read_root():
    """Endpoint raiz - retorna mensagem de boas-vindas"""
    return {"message": "Bem-vindo à API de Lista de Tarefas!"}


# TODO: Implemente os seguintes endpoints:

# 1. GET /tasks - Retorna todas as tarefas
# @app.get("/tasks")
# def get_tasks():
#     pass

# 2. POST /tasks - Cria uma nova tarefa
# @app.post("/tasks", status_code=201)
# def create_task(task: Task):
#     pass

# 3. GET /tasks/{task_id} - Retorna uma tarefa específica
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     pass

# 4. PUT /tasks/{task_id} - Atualiza uma tarefa
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, task_update: TaskUpdate):
#     pass

# 5. DELETE /tasks/{task_id} - Remove uma tarefa
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     pass
