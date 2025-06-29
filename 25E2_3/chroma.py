from langchain.vectorstores import Chroma

def create_chroma_db(documents, persist_directory: str):
    """
    Create a Chroma vector store from the provided documents.

    Args:
        documents (list): A list of documents to be indexed.
        persist_directory (str): The directory where the Chroma database will be stored.

    Returns:
        Chroma: An instance of the Chroma vector store.
    """
    db = Chroma.from_documents(
        documents,
        persist_directory=persist_directory
    )
    db.persist()
    return db

def load_chroma_db(persist_directory: str):
    """
    Load a Chroma vector store from the specified directory.

    Args:
        persist_directory (str): The directory where the Chroma database is stored.

    Returns:
        Chroma: An instance of the Chroma vector store.
    """
    return Chroma(persist_directory=persist_directory)