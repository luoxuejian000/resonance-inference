"""
谐振推理引擎 v2.0 - 基于晶脉哲学四重公理的LLM推理控制器


公理映射:
- 关系本体论: 语义统一性U——概念在关系网络中的在场强度

- 矛盾动力论: 建构性对抗A——否定不是破坏，而是新综合的前提

- 谐振调谐论: 和谐度H与温度τ的梯度流——系统自组织优化

- 实践介入论: 全链路审计——每次推理都是对语义场域的介入

"""


from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="resonance-inference",
    version="2.0.0",
    author="李广好 (luoxuejian000)",
    description="基于晶脉哲学与谐振动力学的LLM推理实时控制器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luoxuejian000/resonance-inference",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "scikit-learn>=1.2.0",
        "sentence-transformers>=2.2.0",
    ],
    extras_require={
        "full": ["spacy>=3.5.0"],
        "dev": ["pytest>=7.0", "black", "mypy"],
    },
)
