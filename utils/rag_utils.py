import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_chroma import Chroma
from env_config.config import EnvConfig
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.tools.retriever import create_retriever_tool

project_configs = EnvConfig()
os.environ["OPENAI_API_KEY"] = project_configs.OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    collection_name="rag_knowledge_base",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db", 
)

retriever = vector_store.as_retriever(search_type="similarity", 
                                      search_kwargs={"k": 1})


template = """You are a helpful assistant that provides accurate information about healthcare insurance plans based on the provided documentation.

Use the following context from healthcare plan documents to answer the question:

{context}

Question: {question}

Answer:"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(template)
)

retriever_tool = create_retriever_tool(retriever=retriever,
                                       name="rag_tool", 
                                       description="Tool for rag implementation")

doc_retriever_chain = RetrievalQA.from_chain_type(llm=llm,
                                                  retriever=retriever,
                                                  chain_type="stuff",
                                                  chain_type_kwargs={"prompt": prompt},
                                                  return_source_documents=False)

# print(doc_retriever_chain.invoke({"query":"list all the flexi care benefit available after 11 months"})["result"])