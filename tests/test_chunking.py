from src.my_agent.chunking import chunk_text_token_aware

def test_chunking_basic():
    text = "word " * 2000
    chunks = chunk_text_token_aware(text, max_tokens=200, overlap=10)
    assert len(chunks) > 0
    assert all(c['text'].strip() for c in chunks)
