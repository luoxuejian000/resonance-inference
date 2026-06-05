"""
建构性对抗计算器(A)——矛盾动力论的工程实现

哲学映射: 否定不是破坏，而是新综合的前提
"""

import re
from typing import List, Tuple, Dict
import numpy as np


class ConstructiveACalculator:
    def __init__(self):
        self.negation_terms = ["但是", "然而", "不过", "却", "可是",
                               "but", "however", "although", "nevertheless"]
        self.synthesis_terms = ["因此", "所以", "于是", "从而",
                                "thus", "therefore", "hence", "consequently"]

    def calculate_antagonism(self, text: str) -> Tuple[float, Dict]:
        """计算建构性对抗 A ∈ [0,1] 及分析细节"""
        sentences = self._split_sentences(text)

        negation_density = self._negation_density(text)
        pairs = self._detect_pairs(sentences)
        constructiveness = self._constructiveness(text, pairs)
        intensity = min(1.0, len(pairs) / max(len(sentences), 1) * 3)

        A = float(np.clip(
            0.4 * negation_density + 0.3 * constructiveness + 0.3 * intensity,
            0.0, 1.0
        ))

        details = {
            "negation_density": negation_density,
            "num_pairs": len(pairs),
            "constructiveness": constructiveness,
            "intensity": intensity,
            "pairs": pairs
        }
        return A, details

    def _split_sentences(self, text: str) -> List[str]:
        sentences = re.split(r'[。!?；;！？\n]+', text)
        return [s.strip() for s in sentences if len(s.strip()) > 5]

    def _negation_density(self, text: str) -> float:
        count = sum(1 for term in self.negation_terms if term in text)
        return min(1.0, count / max(len(text.split()), 1) * 10)

    def _detect_pairs(self, sentences: List[str]) -> List[Tuple[str, str]]:
        pairs = []
        for i in range(len(sentences)-1):
            s1, s2 = sentences[i], sentences[i+1]
            if any(term in s2 for term in self.negation_terms):
                pairs.append((s1, s2))
        return pairs

    def _constructiveness(self, text: str, pairs: List[Tuple[str, str]]) -> float:
        synthesis_count = sum(1 for term in self.synthesis_terms if term in text)
        if len(pairs) == 0:
            return 0.5
        return min(1.0, synthesis_count / len(pairs) + 0.5)
