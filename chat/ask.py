import json
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
    You are an assistant. You answer questions about Django.
    You only answer based on info I'm providing to you. You don't use your internal
    knowledge, browsing etc. And you don't make things up.

    If you don't know the answer, just say: "I don't know."

    The data:

    {str(results['documents'])},
    {str(results['metadatas'])}
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

    chunk_id = 0

    for message in response:
        chunk = {
            'chunk_id': f'chunk_id {chunk_id}',
            'response': message['message']['content'],
        }
        chunk_id += 1
        yield json.dumps(chunk) + "\n"

