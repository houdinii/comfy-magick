from wand.image import Image as WandImage

from ..utilities import PIXEL_INTERPOLATE_METHODS_LIST, process_comfy_magick_function


class Swirl:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Degree": (
                    "FLOAT",
                    {"min": 0.0, "max": 360.0, "step": 0.10, "default": 0.0},
                ),
                "Pixel_Interpolate_Method": (PIXEL_INTERPOLATE_METHODS_LIST,),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSwirl"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Swirl Effect"

    def processSwirl(self, IMAGE, Degree, Pixel_Interpolate_Method, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.swirl,
            IMAGE=IMAGE,
            degree=Degree,
            method=Pixel_Interpolate_Method,
            GRAY=Grayscale,
        )
        return (result,)
