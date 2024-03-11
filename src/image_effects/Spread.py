from wand.image import Image as WandImage

from ..utilities import PIXEL_INTERPOLATE_METHODS_LIST, process_comfy_magick_function


class Spread:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 8.0, "step": 0.1},
                ),
                "Interpolate_Method": (PIXEL_INTERPOLATE_METHODS_LIST,),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSpread"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Spread Image Effect"

    def processSpread(self, IMAGE, Radius, Interpolate_Method, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.spread,
            IMAGE=IMAGE,
            radius=Radius,
            method=Interpolate_Method,
            GRAY=Grayscale,
        )
        return (result,)
