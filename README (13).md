
# IntelliDoc- Your PDF Assistant _Powered by AI_.
## Abstract
_**IntelliDoc**_ is a smart document assistant that helps you quickly find answers from any `PDF` file you upload. You can ask questions about the document, and _**IntelliDoc**_  uses  `AI models` to give you instant, accurate answers based on its content. It also provides easy-to-understand summaries. With a user-friendly interface, _**IntelliDoc**_ makes working with documents faster and more efficient, whether for school, work, or personal use. 

![intelli1](https://github.com/user-attachments/assets/23ce8136-3b1b-490b-b0f5-0636cdfc8f8e)

## Features 
* **PDF Upload and Parsing** : Extract and process text from uploaded PDF documents for seamless interactions.
* **Automatic Summarization** : Generate structured summaries with titles, introductions, key points, and conclusions.
* **Intelligent Querying** :  Provide interactive answers based on the most relevant document sections.
* **Dynamic Conversations** : Maintain conversation context with `buffer memory` for smooth, context-aware interactions.


## Workflow
This project uses **Retrieval-Augmented Generation (RAG)** to process documents, extract meaningful chunks, create embeddings, and generate responses to user queries.
![Screenshot 2025-01-01 104310](https://github.com/user-attachments/assets/b5e7dad1-3020-41b2-9b2f-e5684d7d9aa7)


1- **PDF Upload :** 
* User uploads a PDF document via the app's interface.
* The system reads and processes the file using `PdfReader`.

2- **Text Extraction :** 
* The text from the PDF is extracted and prepared for further processing.
* If the PDF contains multiple pages, the text is grouped by page.

3- **Text Chunking :**
* The extracted text is divided into manageable chunks using `LangChain`'s `RecursiveCharacterTextSplitter`  with overlapping sections for better context retention .
* Overlapping ensures smooth transitions and avoids breaking the logical flow between sections.

4- **Embedding Creation :** 
* Each chunk is converted into a vector representation using **open source** Embedding Model from `Hugging Face`.

5- **Vector Store Management :** 
* `FAISS` is used to store and index these embeddings efficiently.
* When a user queries the system, the vector store retrieves the most relevant chunks by performing a **similarity search**.

    ![similarity-search-overview2](https://github.com/user-attachments/assets/7d0ab9ed-3cab-4a99-9478-c7da1d0a0531)

6- **Summarization :**
* A summary of the uploaded document is generated automatically using an LLM.
* The summary provides an overview with _Title_, _Introduction_, _Key Points_ and _Conclusion_.

    ```python
    combine_custom_prompt="""
    Generate a summary of the following text the includes the following elements:
    * A title that accurately reflects the content of the text.
    * An introduction paragraph that provides an overview of the topic.
    * Bullet points that list the key points of the text.
    * A conclusion paragraph that summarizes the main points of the text.
    Text: "{text}"
    """
    ```
7- **Query Handling :**
* User inputs a question related to the uploaded PDF.
* The query is embedded and matched against the stored vectors to find the most relevant chunks.
* The LLM generates a response based on the retrieved chunks, ensuring contextually accurate and coherent answers.

8- **Conversational Interaction :**
* The system maintains context across multiple user queries using a **conversational retrieval chain** with **memory**.
* Users can refine their queries or ask follow-up questions seamlessly.


## Key Components and Dependencies
### Dependencies
1- **LangChain :** 
* Core framework for text chunking, embeddings, retrieval, summarization, and managing conversational chains via buffer memory.

2- **FAISS :** 
* Provides vectorized storage and retrieval functionality for embeddings.

3- **HuggingFace :**  
* For creating embeddings and utilizing pre-trained language models.

4- **Streamlit:** 
* Framework for building an interactive, user-friendly interface.
### Pre-trained Models:
1- **Alibaba-NLP/gte-base-en-v1.5** open source model for embeddings.

2- **facebook/bart-large-cnn** open source model for summarization task.

3- **Gemini-1.5 Pro** model for conversational task. 

## Demo
![Screenshot 2024-12-31 221634](https://github.com/user-attachments/assets/21cb5008-f8a9-45a7-9e5a-45e32a774903)

![intelij2](https://github.com/user-attachments/assets/cd429761-2428-4983-aa22-8144000d5957)

![intelij3](https://github.com/user-attachments/assets/6c1e70c0-652a-4fb8-8874-f75e00c5dce5)

## Future Improvements
### Towards Multimodal RAG Integration
To enhance IntelliDoc's functionality, the project can evolve to include **Multimodal Retrieval-Augmented Generation (RAG)**. This enhancement will enable the system to process and extract information not just from text but also from **tables**, **images**, and other **document elements**.
## Author

- [@hibasofyan](https://github.com/hibaaaaaaaaaaa)




