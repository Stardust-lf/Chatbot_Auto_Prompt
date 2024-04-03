from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from core.character import TechSupportStageAnalyzerChain, HealthAdvisorChain, EducationCounselorChain

current_role = None  # Global variable to store the current role

KEY = 'xxx'

def chatbot_response(user_input, current_role = 'TechSupport'):
    # Initialize components
    loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
    docs = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=KEY)

    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)

    # Select the appropriate chain based on the current role
    if current_role == 'TechSupport':
        llm = TechSupportStageAnalyzerChain.from_llm(llm=OpenAI(openai_api_key = KEY))
    elif current_role == 'HealthAdvisor':
        llm = HealthAdvisorChain.from_llm(llm=OpenAI(openai_api_key = KEY))
    elif current_role == 'EducationCounselor':
        llm = EducationCounselorChain.from_llm(llm=OpenAI(openai_api_key = KEY))
    else:
        raise ValueError(f"Invalid role: {current_role}")

    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Get chatbot response
    response = retrieval_chain.invoke({"input": user_input})
    answer = response["answer"]
    return answer

user_input = "how can langsmith help with testing?"
response = chatbot_response(user_input)
print(response)
