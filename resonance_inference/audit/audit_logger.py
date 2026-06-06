"""
审计日志: 记录每一步的谐振指标

实践介入论: 每一次推理都是对语义场域的介入，
审计日志是介入痕迹的透明化记录。
"""

import json
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class StepAudit:
    step: int
    U: float
    D: float
    A: float
    H: float
    tau: float
    token_ids_snippet: List[int]
    timestamp: float
    phase_transition: bool = False


class AuditLogger:
    def __init__(self):
        self.session: List[StepAudit] = []
        self.metadata: Dict[str, Any] = {}

    def new_session(self, metadata: Optional[Dict] = None):
        self.session.clear()
        self.metadata = metadata or {}
        self.metadata["start_time"] = time.time()

    def log_step(self, step: int, U: float, D: float, A: float, H: float, tau: float, input_ids: List[int]):
        self.session.append(StepAudit(step, U, D, A, H, tau, input_ids[-20:], time.time()))

    def mark_phase_transition(self, step: int, H: float):
        if self.session and self.session[-1].step == step:
            self.session[-1].phase_transition = True

    def export_json(self, filepath: str):
        data = {"metadata": self.metadata, "steps": [asdict(s) for s in self.session]}
        Path(filepath).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def get_summary(self) -> dict:
        if not self.session:
            return {"error": "empty"}
        H_vals = [s.H for s in self.session]
        return {
            "steps": len(self.session),
            "mean_H": sum(H_vals) / len(H_vals),
            "final_tau": self.session[-1].tau,
            "phase_transitions": sum(1 for s in self.session if s.phase_transition)
        }
