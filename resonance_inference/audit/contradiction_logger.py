"""矛盾记录器: 记录检测到的矛盾对及其位置——矛盾动力论的审计实现"""
from typing import List, Dict


class ContradictionLogger:
    def __init__(self):
        self.contradictions: List[Dict] = []

    def log(self, step: int, sent1: str, sent2: str, strength: float):
        self.contradictions.append({
            "step": step,
            "sentence1": sent1[:100],
            "sentence2": sent2[:100],
            "strength": strength
        })

    def export(self) -> List[Dict]:
        return self.contradictions
