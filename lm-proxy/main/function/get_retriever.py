from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_retriever() -> VectorStoreRetriever:
    knowledge_dir: str = '../resources/knowledge/'
    loader = DirectoryLoader(knowledge_dir + 'in')
    documents = loader.load()
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=300, add_start_index=True)
    texts = text_splitter.split_documents(documents)
    knowledge_dir_out = knowledge_dir + 'out'
    Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=knowledge_dir_out)
    db = Chroma(persist_directory=knowledge_dir_out, embedding_function=embeddings)

    return db.as_retriever()
