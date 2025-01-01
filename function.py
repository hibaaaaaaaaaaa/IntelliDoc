from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter, TokenTextSplitter
from langchain_community.vectorstores import FAISS
import torch
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM
from langchain.schema import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_core.runnables import RunnableLambda
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from WrapperClass import *
from langchain import HuggingFaceHub

def get_text(pdf_docs):
    text=""
    #we can have multiple pdfs so we should loop through the docs on by one
    #for pdf in pdf_docs:
    reader=PdfReader(pdf_docs)
        #for each page in each pdf we extract the text as a string
    for page in reader.pages:
            text+=page.extract_text()

    return text

def get_pdf_pages(pdf_file):
    # Read the uploaded PDF file
    reader = PdfReader(pdf_file)
    pages = reader.pages
    
    # Extract the text and return a list of Document objects
    documents = [Document(page_content=page.extract_text()) for page in pages]
    return documents
    

def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "",
    ],
    chunk_size=100,
    chunk_overlap=20,
    length_function=len

    )
    chunks=text_splitter.split_text(text)
    return chunks



def get_vectorstore2(chunks):
    try:
        # Load the model manually with trust_remote_code
        model_name = "Alibaba-NLP/gte-base-en-v1.5"

        # Initialize Hugging Face embeddings using the manually loaded model
        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
             model_kwargs={
                "device": "cpu",
                "trust_remote_code": True  
            }
        )

        # Generate embeddings for the text chunks
        chunk_embeddings = embeddings.embed_documents(chunks)

        # Check if embeddings are generated
        if not chunk_embeddings:
            raise ValueError("No embeddings were generated.")

        # Create the FAISS vector store
        vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
        return vectorstore

    except Exception as e:
        print(f"Error creating vector store: {e}")
        return None
    



def load_llm():
    load_dotenv()
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
        
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, api_key=google_api_key)
    return llm 




def get_summary(docs):
    llm = load_llm()
    
    if llm is None:
        print("Failed to load LLM. Cannot create conversation chain.")
        return None
    

    map_custom_prompt="""
    Summarize the following text in a clear, concise and brief way:
    TEXT: "{text}"
    Brief Summary :
    """
    map_prompt_template=PromptTemplate(
        input_variables=['text'],
        template=map_custom_prompt    )
    
    combine_custom_prompt="""
    Generate a summary of the following text the includes the following elements:
    * A title that accurately reflects the content of the text.
    * An introduction paragraph that provides an overview of the topic.
    * Bullet points that list the key points of the text.
    * A conclusion paragraph that summarizes the main points of the text.
    Text: "{text}"
    """
    combine_prompt_template=PromptTemplate(
        input_variables=['text'],
        template=combine_custom_prompt   
    )

    summary_chain=load_summarize_chain(
        llm=llm,
        chain_type="map_reduce",
        map_prompt=map_prompt_template,
        combine_prompt=combine_prompt_template,
        verbose=False


    )
    #Use a text splitter to divide the documents into manageable chunks
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)
    
    result=summary_chain.invoke(split_docs)
    return result['output_text']
    

def load_llm2():
    load_dotenv()
    HF_api_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    llm=HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",model_kwargs={"temperature":0.3,"max_new_tokens":500},huggingfacehub_api_token=HF_api_key)
    return llm



def get_conversation(vectorstore):
    llm = load_llm()
    
    if llm is None:
        print("Failed to load LLM. Cannot create conversation chain.")
        return None
    

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)


    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return chain



