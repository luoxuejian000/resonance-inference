"""
谐振引擎: 整合理论、估计器、动力学，提供统一推理接口

晶脉哲学映射:
- 关系本体论: 通过U监控概念在场性
- 矛盾动力论: 通过A检测建构性对抗
- 谐振调谐论: 通过τ的梯度流实现自组织优化
- 实践介入论: 通过审计记录每一次介入
"""

from typing import Optional
import torch
from transformers import PreTrainedModel, PreTrainedTokenizer

from ..theory.harmonic_dynamics import HarmonicDynamics
from ..theory.phase_transition import PhaseTransitionDetector
from ..estimators import SemanticUCalculator, EvolutionaryDCalculator, ConstructiveACalculator
from ..audit import AuditLogger


class HarmonicEngine:
    def __init__(
        self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer,
        lambda_u: float = 0.4, lambda_d: float = 0.4, lambda_a: float = 0.2,
        alpha: float = 0.1, beta: float = 0.05, gamma: float = 0.01, tau0: float = 0.8,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.device = next(model.parameters()).device
        self.lambda_u, self.lambda_d, self.lambda_a = lambda_u, lambda_d, lambda_a

        self.dynamics = HarmonicDynamics(alpha, beta, gamma)
        self.phase_detector = PhaseTransitionDetector()
        self.audit = AuditLogger()

        self.u_calc = SemanticUCalculator()
        self.d_calc = EvolutionaryDCalculator()
        self.a_calc = ConstructiveACalculator()

        self.tau = tau0
        self.prev_dH = 0.0
        self.prev_d2H = 0.0

    @torch.no_grad()
    def step(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, step_index: int = 0) -> torch.Tensor:
        """单步推理: 计算UDA→更新温度→采样token"""
        outputs = self.model(input_ids, attention_mask=attention_mask, use_cache=True)
        logits = outputs.logits

        generated_text = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)

        U = self.u_calc.calculate_unity(generated_text)
        D = self.d_calc.calculate_development([generated_text])
        A, _ = self.a_calc.calculate_antagonism(generated_text)

        state, self.prev_dH, self.prev_d2H = self.dynamics.evolve_step(
            U, D, A, self.tau, self.prev_dH, self.prev_d2H,
            self.lambda_u, self.lambda_d, self.lambda_a, step=step_index
        )
        self.tau = state.tau

        self.audit.log_step(step_index, U, D, A, state.H, self.tau, input_ids[0].cpu().tolist())

        if self.phase_detector.update(state.H, step_index):
            self.audit.mark_phase_transition(step_index, state.H)

        next_logits = logits[0, -1, :] / self.tau
        probs = torch.softmax(next_logits, dim=-1)
        return torch.multinomial(probs, 1)

    def reset(self):
        self.tau = 0.8
        self.prev_dH = 0.0
        self.prev_d2H = 0.0
        self.phase_detector.reset()
        self.audit.new_session()
