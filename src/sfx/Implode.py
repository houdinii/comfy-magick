import torch
from ..utilities import wand_to_pil, getEmptyResults, PIXEL_INTERPOLATE_METHODS_LIST, process_comfy_magick_function
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Amount": (
                    "FLOAT",
                    {"min": 0.0, "max": 1.0, "step": 0.05, "default": 0.0},
                ),
                "Pixel_Interpolate_Method": (PIXEL_INTERPOLATE_METHODS_LIST,),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processImplode"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Implode Effect"

    def processImplode(self, IMAGE, Amount, Pixel_Interpolate_Method, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.implode,
            IMAGE=IMAGE,
            amount=Amount,
            method=Pixel_Interpolate_Method,
            GRAY=Grayscale,
        )
        return (result,)

        # wand_img.implode(amount=Amount, method=Pixel_Interpolate_Method)
