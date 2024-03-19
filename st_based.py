'''
基于sentenceTramsformer，手动编码并匹配向量，效果不佳，已停用
'''
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:15732"
os.environ["https_proxy"] = "http://localhost:15732"

txt_api_key = "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"
client = OpenAI(
    # This is the default and can be omitted
    api_key=txt_api_key,
)

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = client.chat.completions.create(
        model = model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content
prompt = f"""
tell me a story
"""
response = get_completion(prompt)
print(response)



# # 导入外部库
# from openai import OpenAI
# from sentence_transformers import SentenceTransformer, util
# import torch.nn as nn
# import os
# import csv
#
# # 环境与变量设置
# os.environ["http_proxy"] = "http://localhost:15732"
# os.environ["https_proxy"] = "http://localhost:15732"
# directory_path = '/home/liu/Documents/code/曲阜文博资源' # 读取文件夹顶层路径
#
# encoding_model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1') # 向量编码模型设置
#
# txt_api_key = "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"
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=txt_api_key,
# )
#
# def get_completion(prompt,model="gpt-3.5-turbo"):
#     messages = [{"role":"user","content":prompt}]
#     response = client.chat.completions.create(
#         model = model,
#         messages=messages,
#         temperature=0,
#     )
#     return response.choices[0].message.content
#
# # 读取知识库所有文本文件
# def list_files(directory):
#     """
#     递归列出指定目录及其子目录下的所有文件名
#     """
#     file_list = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_list.append(os.path.join(root, file))
#     return file_list
# file_list =  list_files(directory_path)
# text_list = []
# for file_name in file_list:
#     with open(file_name, 'r') as file:
#         text_list.append(file.read())
#
# # 将文本列表转化为向量
# corpus_embeddings = encoding_model.encode(text_list)
#
# for i in range(5):
#     # 输入用户文本
#     # print(text_list)
#     question = input("请输入问题：")
#     question_vector = encoding_model.encode(question)
#
#     # 遍历知识库查找最相近部分
#     information = ''
#
#     # util自动匹配函数
#     # hits = util.semantic_search(question_vector,corpus_embeddings,top_k=10)
#     # for hit in hits[0]:
#         # print(text_list[hit['corpus_id']],"Score:{:.4f}".format(hit['score']))
#         # information += text_list[hit['corpus_id']]
#
#     # 余弦相关性
#     # value_dict = {}
#     # for i in range(len(text_list)):
#     #     cos_value = util.cos_sim(question_vector,corpus_embeddings[i])
#     #     value_dict.update({text_list[i]:cos_value})
#     # sorted_items = sorted(value_dict.items(), key=lambda x: x[1], reverse=True)
#     # top_five_keys = [item[0] for item in sorted_items[:5]]
#     # for i in range(5):
#     #     information += top_five_keys[i]
#     #     information += "\n"
#
#     # 欧式距离
#     # value_dict = {}
#     # pdist = nn.PairwiseDistance(p=2)
#     # for i in range(len(text_list)):
#     #     value = pdist(question_vector,corpus_embeddings[i])
#     #     value_dict.update({text_list[i]:value})
#     # sorted_items = sorted(value_dict.items(), key=lambda x: x[1], reverse=False)
#     # top_five_keys = [item[0] for item in sorted_items[:5]]
#     # for i in range(5):
#     #     information += top_five_keys[i]
#     #     information += "\n"
#
#     # TD-IDF
#
#
#     # 合成prompt
#     prompt = f'''
#     参考资料：
#
#     {information}
#
#
#     请参考上方资料回答问题：{question}
#     并指出引用了参考资料的哪句话。
#     '''
#
#     # 输入模型并得到回复
#     response = get_completion(prompt)
#     print(information)
#     print("---------------------------------------")
#     print(response)
