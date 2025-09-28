import numpy as np
from src.my_agent.vectorstore import FaissStore

def test_faiss_add_search_tmp(tmp_path):
    dim = 8
    store = FaissStore(dim=dim)
    vectors = np.random.rand(5, dim).astype('float32').tolist()
    metas = [{'id': i} for i in range(5)]
    store.add(vectors, metas)
    q = vectors[0]
    results = store.search(q, top_k=3)
    assert len(results) >= 1
    assert results[0]['metadata']['id'] == 0
