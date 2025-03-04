from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# path settings
DATA_PATH = r'data'
CHROMA_PATH = r'chroma_db'

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name='about_django')


def fill_db():
    loader = PyPDFDirectoryLoader(DATA_PATH)
    raw_documents = loader.load()

    # Splitting documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(raw_documents)

    documents = []
    metadata = []
    ids = []

    for i, chunk in enumerate(chunks):
        documents.append(chunk.page_content)
        ids.append(f'ID{i}')
        metadata.append(chunk.metadata)

    # save collections
    collection.upsert(
        documents=documents,
        metadatas=metadata,
        ids=ids,
    )
