from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from qa_agent import get_answer
from sql_agent import get_sql_answer
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=API_KEY
)

rag_tool = Tool.from_function(
    name="wiki",
    func=lambda question: get_answer(question),
    description="Use esta ferramenta para responder perguntas sobre a wiki, funcionalidades e sobre os sistemas NÃO deve ser usada para consultas ao banco de dados ou descobrir nome de tabelas."
)

sql_tool = Tool.from_function(
    name="sql",
    func=lambda question: get_sql_answer(question),
    description="Use esta ferramenta para responder perguntas sobre dados, relatórios ou formulários de processos."
)

tools = [rag_tool, sql_tool]

multi_tool_agent = initialize_agent(
    tools=tools,
    llm=chat_model,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def get_agent_answer(question: str):
    result = multi_tool_agent.invoke({"input": question})

    resposta_final = result["output"]
    source_docs = []

    for tool, out in result.get("intermediate_steps", []):
        if tool.name == "wiki" and isinstance(out, dict):
            source_docs = out.get("source_documents", [])

    return {
        "result": resposta_final,
        "source_documents": source_docs
    }