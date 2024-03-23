# 基于langchain的大模型外挂知识库
## 项目依赖
langchain, openai, 科大讯飞语音转文字api相关依赖, libespeak1, pyttsx3等

## 项目简介

- 工具链架构采用langchain，模型为langchain默认模型
- 语音输出采用科大讯飞语音流语音转文字WebAPI
- 结果输出文字转语音采用pyttsx3

## 使用指南
1. 配置gpt密钥于全局环境变量(OPENAI_GPT_KEY)
2. 修改lc_based.py中的http_proxy和https_proxy为相应值（若不清楚可设置为8790）
3. 指定知识库文本目录路径，修改lc_based.py中的directory_path为指定顶层目录
4. 
```python
python lc_based.py
```

5. 待出现recording输出，则说明开始录音，此时可对“导游”进行提问

6. 提问结束，按ctrl+C键结束录音
7. 等待LLM打印与语音输出