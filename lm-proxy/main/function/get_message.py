from langchain_core.runnables.base import Runnable


def get_message(client_input: str, chain: Runnable) -> dict:
    response = chain.invoke({'input': client_input})

    return {
        'text': response['answer']
    }
