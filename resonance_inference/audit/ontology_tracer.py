"""本体追踪器: 记录概念在场性的变化——关系本体论的审计实现"""
from typing import Dict, List, Set
from collections import defaultdict


class OntologyTracer:
    def __init__(self):
        self.concept_presence: Dict[str, List[int]] = defaultdict(list)

    def update(self, step: int, concepts: Set[str]):
        for c in concepts:
            self.concept_presence[c].append(step)

    def get_report(self) -> dict:
        return dict(self.concept_presence)
