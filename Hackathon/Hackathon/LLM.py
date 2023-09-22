from langchain.chat_models import AzureChatOpenAI

def createLLM(modelname):
    llm = AzureChatOpenAI(deployment_name=modelname, temperature=0.7)
    return llm