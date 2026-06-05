"""
快速开始: 使用谐振控制器生成文本

晶脉哲学四重公理在此完整落地:
- 关系本体论→U监控概念在场性
- 矛盾动力论→A检测建构性对抗
- 谐振调谐论→τ随dH/dt自适应演化
- 实践介入论→全链路审计透明记录
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
from resonance_inference.controllers.realtime_controller import RealtimeHarmonicController

model_name = "Qwen/Qwen-7B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

controller = RealtimeHarmonicController(
    model, tokenizer,
    lambda_u=0.4, lambda_d=0.4, lambda_a=0.2,
    alpha=0.1, beta=0.05, gamma=0.01, tau0=0.8,
    use_meta=True
)

prompt = "证明: 根号2是无理数。"
result = controller.generate(prompt, max_new_tokens=200)
print("\n=== 生成结果 ===\n", result)
controller.export_audit("audit.json")
print("审计日志已保存至 audit.json")
