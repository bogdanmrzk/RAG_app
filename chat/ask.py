import chromadb
import ollama
from .fill_db import fill_db

DATA_PATH = r'data'
CHROMA_PATH = r'chroma_db'

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name='about_django')

fill_db()

def rag_ask(query: str):

    """

    You can ask model about Django Framework.
    Result will be generated based on input files in /data folder.

    :param query: user query to search
    :return: chunk of message
    """

    results = collection.query(
        query_texts=[query],
        n_results=1,
    )

    system_prompt = f"""
    You are a Django assistant. 
    You are strictly prohibited from using your own knowledge. 
    If the answer is not in the provided data, respond with: "I don't know." 

    The data:
    {str(results['documents'])}
    """

    # giving response from ollama
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        stream=True,
    )

    for message in response:
        yield message['message']['content']
