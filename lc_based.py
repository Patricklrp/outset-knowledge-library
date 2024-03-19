import os
import ai_api

import text_operation as TO

from langchain_community.vectorstores import Chroma

# 环境变量设置
os.environ["http_proxy"] = "http://localhost:15732"
os.environ["https_proxy"] = "http://localhost:15732"

# 读取知识库所有文本文件
directory_path = '/home/liu/Documents/曲阜文博资源'  # 读取文件夹顶层路径

# gpt基本设置
chain = ai_api.gpt_settings()

# 获取文本文件
write_path = "all.txt"
file_list,text =  TO.list_files(directory_path,write_path)

# 构建向量知识库
db = ai_api.make_vec_lib(write_path,1000)

def main():
    while(True):
        query = input("请输入问题：")
        if query == "exit":
            exit()
        docs = db.similarity_search(query=query, k=3)
        information = docs[0].page_content
        input_gpt = (f'''
        资料：
        [{information}]
        问题：[{query}]
        请根据以上资料回答问题, 并指出引用了资料的哪句话。
        ''')
        print(chain.invoke({"input": input_gpt}))
        # print(information)

if __name__ == "__main__":
    main()
