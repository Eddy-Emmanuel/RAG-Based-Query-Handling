import sys
import os
# Add project folder path to python module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import langchain modules
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.tools.retriever import create_retriever_tool

# Import project config module
from env_config.config import EnvConfig
project_configs = EnvConfig()

# Set openai environmental variable
os.environ["OPENAI_API_KEY"] = project_configs.OPENAI_API_KEY

# initialize llm, embeddings and vector store retriever
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma(
    collection_name="rag_knowledge_base",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db", 
)
retriever = vector_store.as_retriever(search_type="similarity", 
                                      search_kwargs={"k": 3})

# RAG llm template
template = """You are a knowledgeable healthcare insurance advisor specializing in FlexiCare, PrimeCare, and ZenCare plans. Your role is to provide clear, accurate, and actionable information to help users make informed decisions about their healthcare coverage.

## Instructions:
- Use ONLY the information provided in the context from official plan documents
- If information is not available in the context, clearly state this limitation
- When comparing plans, present information in a structured, easy-to-understand format
- Always specify which plan(s) you're referencing in your answer
- For coverage questions, include relevant details about exclusions, limitations, or requirements
- If the question involves accessing care, provide step-by-step guidance where applicable

## Context from Healthcare Plan Documents:
{context}

## User Question:
{question}

## Response Guidelines:
1. Start with a direct answer to the question
2. Provide specific details from the relevant plan documents
3. Include any important limitations, exclusions, or conditions
4. If comparing multiple plans, use clear formatting (tables/lists when helpful)
5. End with actionable next steps if applicable
6. Ensure your response is in a markdown format.

## Answer:"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(template)
)

# Create retriever tool
retriever_tool = create_retriever_tool(retriever=retriever,
                                       name="rag_tool", 
                                       description="Tool for rag implementation")
# Create RAG CHAIN
doc_retriever_chain = RetrievalQA.from_chain_type(llm=llm,
                                                  retriever=retriever,
                                                  chain_type="stuff",
                                                  chain_type_kwargs={"prompt": prompt},
                                                  return_source_documents=False)