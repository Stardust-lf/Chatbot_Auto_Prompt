from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from charater import TechSupportStageAnalyzerChain, HealthAdvisorChain, EducationCounselorChain

current_role = None  # 全局变量，用于存储当前选择的角色

def choose_role():
    global current_role
    role = input("请选择角色（TechSupport/HealthAdvisor/EducationCounselor），或者输入 'exit' 退出：")
    if role.lower() == 'exit':
        print("Goodbye!")
        exit()
    elif role not in ['TechSupport', 'HealthAdvisor', 'EducationCounselor']:
        print("无效的角色，请重新选择。")
        choose_role()
    else:
        current_role = role

def chatbot_response(user_input):
    global current_role
    if current_role is None:
        choose_role()

    openai_api_key = "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"
    # Initialize components
    loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
    docs = loader.load()
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)

    # 根据当前角色选择相应的链
    if current_role == 'TechSupport':
        llm = TechSupportStageAnalyzerChain.from_llm(embeddings)
    elif current_role == 'HealthAdvisor':
        llm = HealthAdvisorChain.from_llm(embeddings)
    elif current_role == 'EducationCounselor':
        llm = EducationCounselorChain.from_llm(embeddings)

    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # 获取 chatbot 响应
    response = retrieval_chain.invoke({"input": user_input})
    answer = response["answer"]
    return answer

user_input = "how can langsmith help with testing?"
response = chatbot_response(user_input)
print(response)
