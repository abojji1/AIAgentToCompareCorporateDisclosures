import faiss
import numpy as np
import pickle
class FaissStore:
    def __init__(self, dim: int, index_path: str = None):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadatas = []
        self.index_path = index_path
    def add(self, vectors, metadatas):
        arr = np.array(vectors).astype('float32')
        self.index.add(arr)
        self.metadatas.extend(metadatas)
    def search(self, query_vector, top_k=5):
        q = np.array([query_vector]).astype('float32')
        D, I = self.index.search(q, top_k)
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < 0:
                continue
            results.append({'score': float(dist), 'metadata': self.metadatas[idx], 'index': int(idx)})
        return results
