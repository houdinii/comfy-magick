from wand.image import Image as WandImage

from ..utilities import PIXEL_INTERPOLATE_METHODS_LIST, process_comfy_magick_function


class Swirl:
    """
    Swirls pixels around the center of the image. The larger the degree the more pixels will be effected.

    Parameters:
    degree (numbers.Real) – Defines the amount of pixels to be effected. Value between -360.0 and 360.0.
    method (basestring) – Controls interpolation of the effected pixels. Only available for ImageMagick-7. See PIXEL_INTERPOLATE_METHODS.
    """
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
    TITLE = "ComfyMagick - Swirl Effect"

    def processSwirl(self, IMAGE, Degree, Pixel_Interpolate_Method, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.swirl,
            IMAGE=IMAGE,
            degree=Degree,
            method=Pixel_Interpolate_Method,
            GRAY=Grayscale,
        )
        return (result,)
