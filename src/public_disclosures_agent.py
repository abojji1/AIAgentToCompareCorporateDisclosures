# compare_filings_agent.py
import os, json, requests
from bs4 import BeautifulSoup
from openai import OpenAI
import faiss
import numpy as np

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)   # uses OpenAI Python client


##Work in progress