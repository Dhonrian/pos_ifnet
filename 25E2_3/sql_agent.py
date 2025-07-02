import os
from dotenv import load_dotenv
from langchain.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("chave não encontrada.")


def create_and_populate_db():
    db = SQLDatabase.from_uri("sqlite:///test.db")

    db.run("""
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
    """)

    db.run("""
    CREATE TABLE processos (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        form_data TEXT,
        FOREIGN KEY(user_id) REFERENCES usuarios(id)
    )
    """)

    db.run("""
    INSERT INTO usuarios (id, nome) VALUES 
    (1, 'Leo'), (2, 'Mario'), (3, 'João'), (4, 'Will'), (5, 'Matheus')
    """)

    db.run("""
    INSERT INTO processos (id, user_id, form_data) VALUES 
    (1, 1, '{"inscricao": "001.004", "bairro": "Centro", "responsavel_tecnico": "Eduardo"}'),
    (2, 2, '{"inscricao": "002.005", "bairro": "Jardim", "responsavel_tecnico": "Eduardo"}'),
    (3, 3, '{"inscricao": "003.006", "bairro": "Vila", "responsavel_tecnico": "Eduardo"}'),
    (4, 4, '{"inscricao": "004.007", "bairro": "Praia", "responsavel_tecnico": "Fernanda"}'),
    (5, 5, '{"inscricao": "005.008", "bairro": "Montanha", "responsavel_tecnico": "Roberto"}')
    """)

    db.run("""
    INSERT INTO processos (id, user_id, form_data) VALUES 
    (6, 1, '{"inscricao": "006.009", "bairro": "Centro", "responsavel_tecnico": "Eduardo"}'),
    (7, 2, '{"inscricao": "007.010", "bairro": "Jardim", "responsavel_tecnico": "Ana"}'),
    (8, 3, '{"inscricao": "008.011", "bairro": "Vila", "responsavel_tecnico": "Carlos"}'),
    (9, 4, '{"inscricao": "009.012", "bairro": "Praia", "responsavel_tecnico": "Fernanda"}'),
    (10, 5, '{"inscricao": "010.013", "bairro": "Montanha", "responsavel_tecnico": "Roberto"}')
    """)

    return db


chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
    google_api_key=API_KEY,
    system_message="Responda sempre em português de forma clara e objetiva.")


if not os.path.exists("test.db"):
    db = create_and_populate_db()
else:
    db = SQLDatabase.from_uri("sqlite:///test.db")


agent = create_sql_agent(
    llm=chat_model,
    db=db,
    verbose=True
)

def get_sql_answer(question: str):
    try:
        response = agent.invoke(question)
        if isinstance(response, str) and not response.strip():
            return "Não foi possível obter uma resposta da consulta."
        return response
    except Exception as e:
        return f"Erro ao processar a consulta: {str(e)}"
    
