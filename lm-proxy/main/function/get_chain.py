from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from .get_retriever import get_retriever
from langchain_core.runnables.base import Runnable
from langchain_core.vectorstores.base import VectorStoreRetriever


def get_chain() -> Runnable:
    modelo = ChatOllama(model='llama3.1:8b')
    template_intro: str = 'Responda em português do Brasil e responda baseado somente no contexto.'
    template_context: str = 'CONTEXT: {context}'
    template_question: str = 'QUESTION: {input}'
    template: str = template_intro + template_context + template_question
    prompt = ChatPromptTemplate.from_template(template)
    general_structure = create_stuff_documents_chain(modelo, prompt)
    retriever: VectorStoreRetriever = get_retriever()

    return create_retrieval_chain(retriever, general_structure)
