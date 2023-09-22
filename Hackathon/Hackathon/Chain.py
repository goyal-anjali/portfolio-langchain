from langchain.chat_models import AzureChatOpenAI

from langchain.chains import RetrievalQA
from langchain.llms import OpenAIChat
from langchain.chains import LLMChain

def createRetrivalChain(llm, retriever):
    return RetrievalQA.from_chain_type(llm, chain_type='stuff', retriever=retriever)

def createLLMChain(llm, chat_prompt):
    return LLMChain(llm=llm, prompt=chat_prompt)