from wand.image import Image as WandImage

from ..utilities import (
    process_comfy_magick_function,
)

# TODO "Defaults values of zero will have ImageMagick attempt to auto-select suitable values."


class Sharpen:
    """
    Applies a gaussian effect to enhance the sharpness of an image.

    Note
    For best results, ensure radius is larger than sigma.
    Defaults values of zero will have ImageMagick attempt to auto-select suitable values.

    Parameters:
    radius (numbers.Real) – size of gaussian aperture.
    sigma (numbers.Real) – Standard deviation of the gaussian filter.
    channel (basestring) – Optional color channel to target. See CHANNELS.
    """

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
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSharpen"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Sharpen Image Effect"

    def processSharpen(self, IMAGE, Radius, Sigma, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.sharpen,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            GRAY=Grayscale,
        )
        return (result,)
