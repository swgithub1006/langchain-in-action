"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""

# pip install python-dotenv
from dotenv import load_dotenv  # 用于加载环境变量

load_dotenv()  # 加载 .env 文件中的环境变量

# import os
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
# from langchain.llms import OpenAI
from langchain_openai import OpenAI

# llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", max_tokens=200)
# text = llm("请给我写一句情人节红玫瑰的中文宣传语")
text = llm.invoke("请给我写一句情人节红玫瑰的中文宣传语,10个字以内")

print(text)