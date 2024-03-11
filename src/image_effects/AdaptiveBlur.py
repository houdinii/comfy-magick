from ..utilities import (
    COLOR_CHANNELS_LIST, process_comfy_magick_function,
)
from wand.image import Image as WandImage


class AdaptiveBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processAdaptiveBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "Adaptive Blur Image Effect"

    def processAdaptiveBlur(self, IMAGE, Radius, Color_Channel, Sigma):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.adaptive_blur,
            IMAGE=IMAGE,
            sigma=Sigma,
            radius=Radius,
            channel=Color_Channel
        )
        return (result,)
