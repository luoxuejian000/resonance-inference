"""
实时谐振控制器: 封装生成过程，提供高层API
"""

from typing import Optional, Callable
import torch
from transformers import PreTrainedModel, PreTrainedTokenizer
from ..engine import HarmonicEngine, MetaResonanceController


class RealtimeHarmonicController:
    def __init__(
        self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer,
        lambda_u=0.4, lambda_d=0.4, lambda_a=0.2,
        alpha=0.1, beta=0.05, gamma=0.01, tau0=0.8, use_meta=True
    ):
        self.engine = HarmonicEngine(model, tokenizer, lambda_u, lambda_d, lambda_a, alpha, beta, gamma, tau0)
        self.meta = MetaResonanceController() if use_meta else None
        self.tokenizer = tokenizer

    @torch.no_grad()
    def generate(self, prompt: str, max_new_tokens: int = 200, callback: Optional[Callable] = None) -> str:
        self.engine.reset()
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs.input_ids.to(self.engine.device)
        attention_mask = inputs.attention_mask.to(self.engine.device) if inputs.attention_mask is not None else None

        generated = input_ids
        for step in range(max_new_tokens):
            next_token = self.engine.step(generated, attention_mask, step)
            generated = torch.cat([generated, next_token.unsqueeze(0)], dim=1)
            if attention_mask is not None:
                attention_mask = torch.cat([attention_mask, torch.ones((1, 1), device=self.engine.device)], dim=1)

            if self.meta and step % 30 == 0 and step > 0 and len(self.engine.dynamics.history) >= 5:
                recent = self.engine.dynamics.history[-min(30, len(self.engine.dynamics.history)):]
                self.meta.update(recent)
                self.engine.lambda_u = self.meta.lambda_u
                self.engine.lambda_d = self.meta.lambda_d
                self.engine.lambda_a = self.meta.lambda_a

            if callback:
                callback(step, generated)
            if next_token.item() == self.tokenizer.eos_token_id:
                break

        return self.tokenizer.decode(generated[0], skip_special_tokens=True)

    def export_audit(self, filepath: str):
        self.engine.audit.export_json(filepath)
