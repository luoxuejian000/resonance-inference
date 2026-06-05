"""
相变检测: CUSUM算法识别H的突变(顿悟时刻)

矛盾动力论: 顿悟是矛盾累积到临界值的相变释放
谐振调谐论: 相变后系统进入新的有序态
"""

from typing import List, Optional


class PhaseTransitionDetector:
    """
    CUSUM累积和检测器
    
    当H持续高于基线时，累积和增加；超过阈值时发出相变警报。
    """

    def __init__(
        self, threshold: float = 0.5, drift: float = 0.02, min_interval: int = 5
    ):
        self.threshold = threshold
        self.drift = drift
        self.min_interval = min_interval
        self.cumsum = 0.0
        self.last_alert_step: Optional[int] = None
        self.alert_history: List[int] = []

    def update(self, H: float, step: int) -> bool:
        """更新累积和，返回是否检测到相变"""
        if self.last_alert_step and step - self.last_alert_step < self.min_interval:
            return False

        self.cumsum = max(0.0, self.cumsum + H - self.drift)
        if self.cumsum > self.threshold:
            self.alert_history.append(step)
            self.last_alert_step = step
            self.cumsum = 0.0
            return True
        return False

    def reset(self):
        self.cumsum = 0.0
        self.last_alert_step = None

    def get_stats(self) -> dict:
        return {"num_alerts": len(self.alert_history), "alert_steps": self.alert_history.copy()}
