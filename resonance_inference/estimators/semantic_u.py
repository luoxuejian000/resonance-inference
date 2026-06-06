"""
统一性计算器(U)——关系本体论的工程实现

哲学映射: 存在即被关系网络定位→概念在语义空间的密度与连续性
"""

from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

try:
    from sentence_transformers import SentenceTransformer
    HAS_EMBEDDER = True
except ImportError:
    HAS_EMBEDDER = False


class SemanticUCalculator:
    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2"):
        self.embedding_model = embedding_model
        self._embedder = None

    @property
    def embedder(self):
        if self._embedder is None and HAS_EMBEDDER:
            self._embedder = SentenceTransformer(self.embedding_model)
        return self._embedder

    def _split_sentences(self, text: str) -> List[str]:
        sentences = re.split(r'[。!?；;！？\n]+', text)
        return [s.strip() for s in sentences if len(s.strip()) > 5]

    def calculate_unity(self, text: str, window_size: int = 3) -> float:
        """计算语义统一性 U ∈ [0,1]"""
        sentences = self._split_sentences(text)
        if len(sentences) < 2:
            return 0.5

        continuity = self._concept_continuity(sentences, window_size)
        consistency = self._semantic_consistency(sentences)

        U = 0.5 * continuity + 0.5 * consistency
        return float(np.clip(U, 0.0, 1.0))

    def _concept_continuity(self, sentences: List[str], window: int) -> float:
        scores = []
        for i in range(len(sentences) - window + 1):
            sets = [set(s.split()) for s in sentences[i:i+window]]
            union = set.union(*sets)
            inter = set.intersection(*sets)
            scores.append(len(inter) / len(union) if union else 0.0)
        return np.mean(scores) if scores else 0.0

    def _semantic_consistency(self, sentences: List[str]) -> float:
        if len(sentences) < 2 or self.embedder is None:
            return 0.5
        embeddings = self.embedder.encode(sentences)
        sims = [cosine_similarity([embeddings[i]], [embeddings[i+1]])[0][0]
                for i in range(len(sentences)-1)]
        return float(np.mean(sims)) if sims else 0.5
