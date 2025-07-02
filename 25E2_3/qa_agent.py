import os
from dotenv import load_dotenv
from chroma import create_chroma_db, load_chroma_db
from document_loader import load_documents
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("chave não encontrada.")


embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=API_KEY
    )


if not os.path.exists("chroma_db"):
    docs = load_documents("files")
    db = create_chroma_db(docs, persist_directory="chroma_db", embedding=embedding_model)
else:
    db = load_chroma_db(persist_directory="chroma_db", embedding=embedding_model)


chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)


template = """
Você é um programador da Geopixel. 

Baseado nas informações contidas na wiki responda a pergunta do usuário de forma clara e objetiva e sempre em português.
Se a pergunta não puder ser respondida com as informações disponíveis, informe que não é possível responder
a pergunta e para que procure um desenvolvedor como o Iuri.

Contexo: 
{context}

Pergunta:
{question}

Resposta:
"""
prompt_template = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

qa = RetrievalQA.from_chain_type(
    llm=chat_model,
    chain_type="stuff",
    retriever=db.as_retriever(),
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)


def get_answer(question: str):

    response = qa.invoke({"query": question})
    
    return {
        "result": response["result"],
        "source_documents": response.get("source_documents", [])
    }