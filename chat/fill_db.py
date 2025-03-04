from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# environment settings
DATA_PATH = r'data'
CHROMA_PATH = r'chroma_db'

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name='about_django')

# document loading
def fill_db():
    # Document loading
    loader = PyPDFDirectoryLoader(DATA_PATH)
    raw_documents = loader.load()

    # Splitting documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(raw_documents)

    # Preparing to add data into Chroma DB
    documents = []
    metadata = []
    ids = []

    for i, chunk in enumerate(chunks):
        documents.append(chunk.page_content)
        ids.append(f'ID{i}')
        metadata.append(chunk.metadata)

    # Adding to Chroma DB
    collection.upsert(
        documents=documents,
        metadatas=metadata,
        ids=ids,
    )
    print(f"Database filled with {len(documents)} chunks.")
