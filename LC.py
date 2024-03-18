import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["http_proxy"] = "http://localhost:15732"
os.environ["https_proxy"] = "http://localhost:15732"

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
# 读取知识库所有文本文件
directory_path = '/home/liu/Documents/曲阜文博资源'  # 读取文件夹顶层路径

# 调用GPT基本设置
# combine into prompts
# basic settings and varieties
llm = ChatOpenAI()
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "你现在是一个介绍曲阜文旅的导游"),
    ("user", "{input}")
])
chain = prompt | llm | output_parser

def list_files(directory):
    """
    递归列出指定目录及其子目录下的所有文件名
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
file_list =  list_files(directory_path)
text = ""
for file_name in file_list:
    text += ("\n" + file_name + ":")
    with open(file_name, 'r') as file:
        text += file.read()
    text += "\n ''' \n"

with open("all.txt", 'w') as file:
    file.write(text)

raw_documents = TextLoader('all.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = Chroma.from_documents(documents, OpenAIEmbeddings())

while(True):
    query = input("请输入问题：")
    if query == "exit":
        exit()
    docs = db.similarity_search(query=query, k=3)
    information = docs[0].page_content
    # input_gpt = (f'''
    # 资料：
    # [{information}]
    # 问题：[{query}]
    # 请根据以上资料回答问题, 并指出引用了资料的哪句话。
    # ''')
    # print(chain.invoke({"input": input_gpt}))
    print(information)

