import tiktoken
ENC = tiktoken.get_encoding('cl100k_base')

def chunk_text_token_aware(text: str, max_tokens: int = 800, overlap: int = 50):
    tokens = ENC.encode(text)
    chunks = []
    start = 0
    N = len(tokens)
    while start < N:
        end = min(N, start + max_tokens)
        chunk_tokens = tokens[start:end]
        chunk_text = ENC.decode(chunk_tokens)
        chunks.append({'text': chunk_text, 'start_token': start, 'end_token': end})
        start = end - overlap
    return chunks
