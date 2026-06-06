"""
Resonance Inference v2.0
基于晶脉哲学(关系本体论、矛盾动力论、谐振调谐论、实践介入论)的LLM实时推理控制器

核心函数: H = λᵤ·U + λᴅ·D - λₐ·A
温度动力学: dτ/dt = -α·(dH/dt)/τ + β·(d²H/dt²) - γ·τ
"""

from .controllers.realtime_controller import RealtimeHarmonicController
from .engine import HarmonicEngine, MetaResonanceController
from .estimators import SemanticUCalculator, EvolutionaryDCalculator, ConstructiveACalculator
from .theory import HarmonicDynamics, PhaseTransitionDetector
from .audit import AuditLogger

__version__ = "2.0.0"
__author__ = "李广好 (luoxuejian000)"
__all__ = [
    "RealtimeHarmonicController", "HarmonicEngine", "MetaResonanceController",
    "SemanticUCalculator", "EvolutionaryDCalculator", "ConstructiveACalculator",
    "HarmonicDynamics", "PhaseTransitionDetector", "AuditLogger"
]
