# 📘 Tarefa: APIs REST com FastAPI

## 🎯 Objetivo

Aprender a construir APIs REST usando o framework FastAPI, praticando criação de endpoints, validação de dados com Pydantic e operações CRUD básicas.

## 📝 Tarefas

### 🛠️ API de Lista de Tarefas

#### Descrição
Crie uma API REST para gerenciar uma lista de tarefas (to-do list) com operações básicas de criação, leitura, atualização e exclusão (CRUD).

#### Requisitos
Programa concluído deve:

- Criar um endpoint GET `/tasks` que retorna todas as tarefas em formato JSON.
- Criar um endpoint POST `/tasks` que adiciona uma nova tarefa (recebe título e descrição).
- Criar um endpoint GET `/tasks/{task_id}` que retorna uma tarefa específica pelo ID.
- Criar um endpoint PUT `/tasks/{task_id}` que atualiza uma tarefa existente.
- Criar um endpoint DELETE `/tasks/{task_id}` que remove uma tarefa.
- Usar modelos Pydantic para validar os dados de entrada (título obrigatório, descrição opcional).
- Armazenar tarefas em memória usando um dicionário Python (não precisa banco de dados).


### 🛠️ Documentação e Testes

#### Descrição
Explore a documentação automática do FastAPI e teste todos os endpoints criados usando a interface Swagger UI.

#### Requisitos
Programa concluído deve:

- Executar a aplicação com `uvicorn main:app --reload`.
- Acessar a documentação automática em `http://localhost:8000/docs`.
- Testar cada endpoint usando a interface Swagger UI (criar, listar, atualizar e deletar tarefas).
- Adicionar descrições aos endpoints usando o parâmetro `description` nas rotas.
- Verificar que os códigos de status HTTP estão corretos (200 para sucesso, 404 para não encontrado, 201 para criação).
