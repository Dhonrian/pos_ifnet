from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("chave não encontrada.")


embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-exp-03-07",
    google_api_key=API_KEY)

