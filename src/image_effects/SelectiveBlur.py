from wand.image import Image as WandImage

from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function


#  TODO What is this actually doing?


class SelectiveBlur:
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
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 1000.0, "default": 0.0, "step": 0.25},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSelectiveBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "Selective Blur Image Effect"

    def processSelectiveBlur(
        self, IMAGE, Radius, Sigma, Threshold, Color_Channel, Grayscale
    ):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.selective_blur,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            threshold=Threshold,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
