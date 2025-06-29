from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_documents(directory: str):
    """
    Load documents from a specified directory.
    
    Args:
        directory (str): The path to the directory containing documents.
        
    Returns:
        list: A list of loaded documents.
    """
    loader = DirectoryLoader(
        directory,
        glob="**/*.md",
        loader_cls=UnstructuredFileLoader
    )
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100)
    split_documents = text_splitter.split_documents(documents)
    return split_documents
