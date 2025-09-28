import os
from src.my_agent.edgar import download_filing_html
from src.my_agent.extractor import extract_sections_from_html
from src.my_agent.chunking import chunk_text_token_aware
from src.my_agent.embeddings import embed_texts
from src.my_agent.vectorstore import FaissStore
from src.my_agent.prompts import SYSTEM_PROMPT, COMPARE_TEMPLATE
from openai import OpenAI

def compare_filings(filing_a: dict, filing_b: dict, section: str = 'MD&A', top_k: int = 3):
    html_a = download_filing_html(filing_a['cik'], filing_a['accession'])
    html_b = download_filing_html(filing_b['cik'], filing_b['accession'])
    sections_a = extract_sections_from_html(html_a)
    sections_b = extract_sections_from_html(html_b)
    text_a = sections_a.get(section, '')
    text_b = sections_b.get(section, '')
    chunks_a = chunk_text_token_aware(text_a)
    chunks_b = chunk_text_token_aware(text_b)
    texts_for_embed = [c['text'] for c in chunks_a + chunks_b]
    vectors = embed_texts(texts_for_embed)
    dim = len(vectors[0])
    store = FaissStore(dim=dim)
    metadatas = []
    for i, c in enumerate(chunks_a):
        metadatas.append({'filing_id': filing_a['id'], 'chunk_id': f'A-{i}', 'section': section})
    for i, c in enumerate(chunks_b):
        metadatas.append({'filing_id': filing_b['id'], 'chunk_id': f'B-{i}', 'section': section})
    store.add(vectors, metadatas)
    selected_a = chunks_a[:top_k]
    selected_b = chunks_b[:top_k]
    chunks_a_text = "\n---\n".join([f"ID:A-{i}\n{c['text'][:2000]}" for i,c in enumerate(selected_a)])
    chunks_b_text = "\n---\n".join([f"ID:B-{i}\n{c['text'][:2000]}" for i,c in enumerate(selected_b)])
    prompt = COMPARE_TEMPLATE.format(section=section, date_a=filing_a.get('date','unknown'), date_b=filing_b.get('date','unknown'), chunks_a=chunks_a_text, chunks_b=chunks_b_text)
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":prompt}], max_tokens=800)
    return response.choices[0].message['content']
