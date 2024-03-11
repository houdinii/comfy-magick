import torch
from ..utilities import (
    wand_to_pil,
    getEmptyResults,
    COLOR_CHANNELS_LIST,
    process_comfy_magick_function,
)
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class UnsharpMask:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 8.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 4.0, "step": 0.1},
                ),
                "Amount": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 8.0, "step": 0.1},
                ),
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 4.0, "step": 0.1},
                ),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processUnsharpMask"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Unsharp Mask Image Effect"

    def processUnsharpMask(
        self, IMAGE, Radius, Sigma, Amount, Threshold, Color_Channel, Grayscale
    ):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.unsharp_mask,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            amount=Amount,
            threshold=Threshold,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
