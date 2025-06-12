# LLM BASED PDF ANALYSER (LANGCHAIN)
# 📚 Chat with PDF using Gemini (Google Generative AI)

This project allows users to upload multiple PDF files and ask questions about the content inside them. It uses **Google's Gemini model** (via LangChain integration) to provide intelligent, context-aware answers by retrieving relevant content from the uploaded PDFs.

---

## 🚀 Features

- Upload and process multiple PDFs
- Extract and chunk large amounts of text
- Convert text chunks into vector embeddings using **Google Generative AI Embeddings**
- Store and search using **FAISS** vector store
- Ask questions and get accurate responses based on PDF content
- Intuitive **Streamlit** frontend for easy interaction

---

## 🧠 Tech Stack

### 🗂 Backend
- **Python 3.9+**
- **LangChain** – framework for chaining LLM applications together
- **FAISS** – vector similarity search engine for text embeddings
- **PyPDF2** – PDF parsing and text extraction
- **Google Generative AI (Gemini)** – used via `langchain_google_genai`
- **GoogleGenerativeAIEmbeddings** – to convert text into embeddings for similarity search

### 🌐 Frontend
- **Streamlit** – lightweight UI for uploading PDFs and chatting with Gemini

### 📦 Key Libraries

| Library                   | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| `langchain`               | Chain LLM with tools like prompts, retrievers, and embeddings           |
| `langchain_google_genai` | Access Gemini models and embeddings through LangChain                    |
| `PyPDF2`                  | Read and extract text from PDF files                                    |
| `streamlit`               | Build a simple web interface                                            |
| `faiss-cpu`               | Efficient similarity search on embeddings                               |
| `dotenv`                  | Load API keys from `.env` securely                                      |

---

## 🔑 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/pdf-gemini-chat.git
cd pdf-gemini-chat
