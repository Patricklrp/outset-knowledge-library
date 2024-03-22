# 基于langchain的大模型外挂知识库
## 项目依赖
langchain, openai, 科大讯飞语音转文字api相关依赖, libespeak1, pyttsx3等
## 使用指南
1. 配置gpt密钥于全局环境变量(OPENAI_GPT_KEY)
2. 修改lc_based.py中的http_proxy和https_proxy为相应值（若不清楚可设置为8790）
3. 指定知识库文本目录路径，修改lc_based.py中的directory_path为指定顶层目录
4. 
```
python lc_based.py
```