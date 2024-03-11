from wand.image import Image as WandImage

from ..utilities import (
    PIXEL_INTERPOLATE_METHODS_LIST,
    process_comfy_magick_function,
)


class Implode:
    """
    Creates a “imploding” effect by pulling pixels towards the center of the image.

    Parameters:
    amount (numbers.Real) – Normalized degree of effect between 0.0 & 1.0.
    method (basestring) – Which interpolate method to apply to effected pixels. See PIXEL_INTERPOLATE_METHODS for
    a list of options. Only available with ImageMagick-7.
    """

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
    TITLE = "ComfyMagick - Implode Effect"

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
