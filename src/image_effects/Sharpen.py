import torch
from ..utilities import (
    wand_to_pil,
    getEmptyResults, process_comfy_magick_function,
)
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class Sharpen:
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
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSharpen"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Sharpen Image Effect"

    def processSharpen(self, IMAGE, Radius, Sigma, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.sharpen,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            GRAY=Grayscale,
        )
        return (result,)
