from ..utilities import process_comfy_magick_function
from wand.image import Image as WandImage


class Emboss:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "True"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processEmboss"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Emboss Image Effect"

    def processEmboss(self, IMAGE, Radius, Sigma, Grayscale):
        result = process_comfy_magick_function(FUNCTION=WandImage.emboss, IMAGE=IMAGE, GRAY=Grayscale)
        return (result,)
