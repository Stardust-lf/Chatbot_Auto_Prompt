import os
from langchain_openai import OpenAI


llm = OpenAI(openai_api_key = "xxx", temperature=0.9)
xxlimited = sdds(llm)
print(llm.invoke('Hi'))
