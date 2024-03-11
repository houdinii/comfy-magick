import torch
from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function
from wand.image import Image as WandImage


class AdaptiveSharpen:
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
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processAdaptiveSharpen"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Adaptive Sharpen Image Effect"

    def processAdaptiveSharpen(self, IMAGE, Radius, Sigma, Color_Channel, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.adaptive_sharpen,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
