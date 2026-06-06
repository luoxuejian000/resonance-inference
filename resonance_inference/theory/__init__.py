"""
理论核心模块: 谐振动力学与相变检测
基于晶脉哲学四重公理的数学实现
"""
from .harmonic_dynamics import HarmonicDynamics, HarmonicState
from .phase_transition import PhaseTransitionDetector

__all__ = ["HarmonicDynamics", "HarmonicState", "PhaseTransitionDetector"]
