from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def gpt_settings():
    """gpt基本设置

    Returns:
        chain: gpt调用工具联
    """
    llm = ChatOpenAI()
    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", ""),
        ("user", "{input}")
    ])
    chain = prompt | llm | output_parser
    return chain

def make_vec_lib(text_path,chunk_size=1000):
    """生成嵌入文本向量库

    Args:
        text_path (str): 文本文件路径
        chunk_size (int, optional): 分割单个向量大小. Defaults to 1000.

    Returns:
        db: 向量库
    """
    raw_documents = TextLoader(text_path).load()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)
    db = Chroma.from_documents(documents, OpenAIEmbeddings())
    return db