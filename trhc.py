import streamlit as st
#%%
from PyPDF2 import PdfReader
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema import HumanMessage
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ["GOOGLE_API_KEY"] = "@$@^%^*^&%"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001")
prompt_template="""
    Answer the question as detail as possible from the provided context, make sure to provide all the details, if the answer is not in the provided context just say, "answer is not available in the context", don't provide the wrong answer
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:"""
#model=ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001",temperature=0.3)
model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001")
prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
#chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
chain = LLMChain(llm=model, prompt=prompt)
messages = [HumanMessage(content="Hello, how are you?")]

response = model.generate(messages=[messages])

#print(response)
generated_text = response.generations[0][0].text
print(generated_text)


# import google.generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# os.environ["GOOGLE_API_KEY"] = ""
# import google.generativeai as genai
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
#
# #genai.configure(api_key="AIzaSyDWv3vfciG83in2oAt2gMTLFcAXI5AcKSI")
#
# model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001")
#
# response = model.generate(messages=[{"role":"user", "content":"Hello, how are you?"}])
#
# print(response)


# import os
# import google.generativeai as genai
#
# # Set your API key string here directly or via environment variable
# os.environ["GOOGLE_API_KEY"] = ""
#
# # Configure the genai client with the API key
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# import google.generativeai as genai
# import os
#
# # Configure with your API key or Application Default Credentials
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#
# models = genai.list_models()
# print("Available models:")
# for model in models:
#     print(model.name)

