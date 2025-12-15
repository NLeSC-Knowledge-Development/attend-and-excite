"""
Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models

Official implementation of the SIGGRAPH 2023 paper.
"""

__version__ = "1.0.0"

from .pipeline_attend_and_excite import AttendAndExcitePipeline
from .config import RunConfig

__all__ = [
    "AttendAndExcitePipeline",
    "RunConfig",
]
