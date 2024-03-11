from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function
from wand.image import Image as WandImage


class GaussianBlur:
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
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processGaussianBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "Gaussian Blur Image Effect"

    def processGaussianBlur(self, IMAGE, Radius, Color_Channel, Sigma, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.gaussian_blur,
            IMAGE=IMAGE,
            GRAY=Grayscale,
            radius=Radius,
            sigma=Sigma,
            channel=Color_Channel,
        )
        return (result,)
