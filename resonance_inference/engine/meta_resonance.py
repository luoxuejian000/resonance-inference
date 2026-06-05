"""
元谐振控制器: 根据历史H值动态调整λ权重

谐振调谐论: λ权重不是预设的，而是通过系统反馈自组织优化
"""

import numpy as np
from typing import List
from ..theory.harmonic_dynamics import HarmonicState


class MetaResonanceController:
    def __init__(self, initial_lambdas=(0.4, 0.4, 0.2), lr=0.02):
        self.lambda_u, self.lambda_d, self.lambda_a = initial_lambdas
        self.lr = lr

    def update(self, recent_states: List[HarmonicState]):
        """根据最近状态的U/D/A平均值调整λ权重"""
        if len(recent_states) < 5:
            return

        avg_U = np.mean([s.U for s in recent_states])
        avg_D = np.mean([s.D for s in recent_states])
        avg_A = np.mean([s.A for s in recent_states])

        target_U, target_D, target_A = 0.7, 0.6, 0.25

        self.lambda_u += self.lr * np.clip(target_U - avg_U, -0.1, 0.1)
        self.lambda_d += self.lr * np.clip(target_D - avg_D, -0.1, 0.1)
        self.lambda_a += self.lr * np.clip(avg_A - target_A, -0.1, 0.1)

        total = self.lambda_u + self.lambda_d + self.lambda_a
        if total > 0:
            self.lambda_u = max(0.05, self.lambda_u / total)
            self.lambda_d = max(0.05, self.lambda_d / total)
            self.lambda_a = max(0.05, self.lambda_a / total)
