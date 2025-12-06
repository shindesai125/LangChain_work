from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = OpenAIEmbeddings(model = 'text-embedding-3-small', dimentions = 32)
documents = [" helllo",
             "how",
             "are",
             "you",
             "today?"]
result = embedding.embed_documents(documents)

print(str(result))