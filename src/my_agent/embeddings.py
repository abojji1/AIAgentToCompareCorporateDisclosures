import os
from openai import OpenAI

def embed_texts(texts, model='text-embedding-3-small'):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    resp = client.embeddings.create(model=model, input=texts)
    return [d.embedding for d in resp.data]
