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
#%%
import os
#os.environ["GOOGLE_API_KEY"] = "%$##%&%$"
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#load_dotenv()
#genai.configure(api_key=os.getenv(os.environ["GOOGLE_API_KEY"]))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

#%%
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    chunks=text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
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
    return chain

def user_input(user_question):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    #new_db=FAISS.load_local("faiss_index",embeddings)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs=new_db.similarity_search(user_question)
    #chain=get_conversational_chain()
    # response=chain({"input_documents":docs,"question": user_question}
                   #, return_only_outputs=True)
    # Combine the relevant texts from retrieved docs
    context = "\n".join([doc.page_content for doc in docs])
    model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001")
    chain = get_conversational_chain()
    # messages = [HumanMessage(content="Hello, how are you?")]

    #response = model.generate(messages=[messages])
    # Pass both context and question explicitly
    response = chain.run(context=context, question=user_question)

    #print(response)
    #generated_text = response.generations[0][0].text
    #print(generated_text)
    #st.write("Reply: ", response["text"])
    st.write(response)

def main():
    st.set_page_config("Chat with Multiple PDF")
    st.header("Chat with PDF using Gemini")

    user_question=st.text_input("Ask a question from the PDF Files")
    if user_question:
        user_input(user_question)
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and click on the Submit & Process", type=["pdf"],
                                    accept_multiple_files=True)

        if st.button("Submit & Process"):
            raw_text=get_pdf_text(pdf_docs)
            text_chunk=get_text_chunks(raw_text)
            get_vector_store(text_chunk)
            st.success("Done")

if __name__ == "__main__":
    main()
