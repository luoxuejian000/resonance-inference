"""
谐振动力学: 从晶脉哲学公理到微分方程

公理映射:
- 矛盾动力论: dH/dt驱动τ演化——矛盾是系统演化的能量源
- 谐振调谐论: 系统趋向H最大化——朝向更高和谐度自组织
- 实践介入论: 相位检测(探索/利用/顿悟)——每次介入都改变场域

动力学方程:
    dτ/dt = -α·(dH/dt)/τ + β·(d²H/dt²) - γ·τ

物理意义:
    - 第一项(谐振项): H上升→降温(利用)，H下降→升温(探索)
    - 第二项(惯性项): H加速上升预示顿悟，提前调节温度
    - 第三项(衰减项): 温度自然趋向稳态，防止极端化
"""

import math
from typing import List
from dataclasses import dataclass


@dataclass
class HarmonicState:
    """谐振状态: 描述系统在语义空间的动力学状态"""
    step: int
    H: float          # 和谐度 H = λᵤU + λᴅD - λₐA
    tau: float        # 温度 τ: 探索/利用的平衡参数
    dH_dt: float      # 和谐度一阶导数(变化速度)
    d2H_dt2: float    # 和谐度二阶导数(加速度)——顿悟信号
    phase: str        # explore | exploit | insight
    U: float          # 统一性
    D: float          # 发展性
    A: float          # 对抗性


class HarmonicDynamics:
    """
    谐振动力学控制器
    
    田新民的沙漠之树: 温度τ如同装沙塑料袋——不改变沙漠的物理属性，
    而是重新组织"温差-水汽-根系"之间的关系拓扑，将矛盾转化为动力。
    """

    def __init__(
        self,
        alpha: float = 0.1,      # 谐振系数——dH/dt对τ的影响强度
        beta: float = 0.05,      # 惯性系数——d²H/dt²对τ的影响强度
        gamma: float = 0.01,     # 衰减系数——τ自然回归速率
        tau_min: float = 0.1,    # 最低温度——最大利用状态
        tau_max: float = 2.0,    # 最高温度——最大探索状态
        insight_threshold: float = 0.05,  # 顿悟阈值
    ):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.insight_threshold = insight_threshold
        self.history: List[HarmonicState] = []

    def harmony_function(
        self, U: float, D: float, A: float,
        lambda_u: float, lambda_d: float, lambda_a: float
    ) -> float:
        """和谐度函数: H = λᵤ·U + λᴅ·D - λₐ·A"""
        return lambda_u * U + lambda_d * D - lambda_a * A

    def temperature_update(
        self, tau_prev: float, dH_dt: float, d2H_dt2: float
    ) -> float:
        """
        温度更新: 乘性形式，保证数值稳定性
        
        从连续方程 dτ/dt = -α·(dH/dt)/τ + β·(d²H/dt²) - γ·τ
        推导对数增量: d(ln τ) = -α·(dH/dt)/τ² + β·(d²H/dt²)/τ - γ
        """
        if tau_prev <= 0:
            tau_prev = 0.5

        d_ln_tau = -self.alpha * dH_dt / (tau_prev * tau_prev + 1e-8)
        d_ln_tau += self.beta * d2H_dt2 / (tau_prev + 1e-8)
        d_ln_tau -= self.gamma

        new_tau = tau_prev * math.exp(d_ln_tau)
        return max(self.tau_min, min(self.tau_max, new_tau))

    def detect_phase(self, d2H_dt2: float, tau: float) -> str:
        """
        相位检测: 对应实践介入论——系统状态的自我感知
        
        - insight: H加速上升超过阈值——顿悟相变
        - explore: 高温状态——扩大搜索范围
        - exploit: 低温状态——精细利用
        """
        if d2H_dt2 > self.insight_threshold:
            return "insight"
        if tau > 1.2:
            return "explore"
        return "exploit"

    def evolve_step(
        self, U: float, D: float, A: float,
        tau_prev: float, dH_prev: float, dH_prev2: float,
        lambda_u: float, lambda_d: float, lambda_a: float,
        step: int,
    ) -> tuple:
        """
        单步演化: 计算H→更新τ→检测相位→记录状态
        
        返回: (HarmonicState, 新的dH用于下步, 新的d2H用于下步)
        """
        H = self.harmony_function(U, D, A, lambda_u, lambda_d, lambda_a)
        
        dH_dt = H - dH_prev if step > 0 else 0.0
        d2H_dt2 = dH_dt - dH_prev2 if step > 1 else 0.0

        tau = self.temperature_update(tau_prev, dH_dt, d2H_dt2)
        phase = self.detect_phase(d2H_dt2, tau)

        state = HarmonicState(
            step=step, H=H, tau=tau,
            dH_dt=dH_dt, d2H_dt2=d2H_dt2,
            phase=phase, U=U, D=D, A=A,
        )
        self.history.append(state)
        return state, dH_dt, d2H_dt2
