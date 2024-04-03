# Requires:
# pip install langchain docarray tiktoken
import os
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from core.utils import txt_to_string


os.environ["OPENAI_API_KEY"] = 'xxx'

def get_answer_with_char(question, char_prompt, sorce_dir):
    model = ChatOpenAI(model="gpt-3.5-turbo-0125")

    vectorstore = DocArrayInMemorySearch.from_texts(
        [txt_to_string(sorce_dir)],
        embedding=OpenAIEmbeddings(),
    )
    retriever = vectorstore.as_retriever()
    template = char_prompt + """Answer the question based only on the following context:
    {context}, in Simplified Chinese
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    output_parser = StrOutputParser()

    setup_and_retrieval = RunnableParallel(
        {
         "context": retriever,
         "question": RunnablePassthrough()}
    )
    chain = setup_and_retrieval | prompt | model | output_parser
    return chain.invoke(question)
