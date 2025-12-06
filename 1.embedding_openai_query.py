from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = OpenAIEmbeddings(model = 'text-embedding-3-small', dimentions = 32)

result = embedding.embed_query("How are you today")

print(result)