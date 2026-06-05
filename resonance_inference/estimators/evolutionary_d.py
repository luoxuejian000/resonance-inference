"""
发展性计算器(D)——谐振调谐论的工程实现

哲学映射: 系统朝向更高和谐度自组织→逻辑流动的熵减趋势
"""

import numpy as np
from typing import List


class EvolutionaryDCalculator:
    def __init__(self, window_size: int = 3):
        self.window_size = window_size

    def calculate_development(self, text_segments: List[str]) -> float:
        """计算发展性 D ∈ [0,1]"""
        if len(text_segments) < 2:
            return 0.5

        continuity = self._semantic_continuity(text_segments)
        entropy_score = self._entropy_trend(text_segments)
        emergence = self._emergence_score(text_segments)

        D = 0.4 * continuity + 0.3 * entropy_score + 0.3 * emergence
        return float(np.clip(D, 0.0, 1.0))

    def _semantic_continuity(self, segments: List[str]) -> float:
        overlaps = []
        for i in range(len(segments)-1):
            w1, w2 = set(segments[i].split()), set(segments[i+1].split())
            if w1 and w2:
                overlaps.append(len(w1 & w2) / len(w1 | w2))
        return np.mean(overlaps) if overlaps else 0.0

    def _entropy_trend(self, segments: List[str]) -> float:
        entropies = []
        for seg in segments:
            words = seg.split()
            if not words:
                entropies.append(0.0)
                continue
            freq = {}
            for w in words:
                freq[w] = freq.get(w, 0) + 1
            probs = np.array(list(freq.values())) / len(words)
            entropies.append(-np.sum(probs * np.log(probs + 1e-8)))
        if len(entropies) < 2:
            return 0.5
        slope = np.polyfit(np.arange(len(entropies)), entropies, 1)[0]
        return float(1.0 - np.clip(slope / 0.5, -1, 1) * 0.5)

    def _emergence_score(self, segments: List[str]) -> float:
        word_sets = [set(s.split()) for s in segments]
        if len(word_sets) < 2:
            return 0.5
        new_ratios, cumulative = [], set()
        for i, ws in enumerate(word_sets):
            new = ws - cumulative
            new_ratios.append(len(new) / (len(ws) + 1e-8))
            cumulative.update(ws)
        return float(1.0 - np.clip(np.std(new_ratios), 0.0, 0.5) / 0.5)
