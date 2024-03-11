from wand.image import Image as WandImage

from ..utilities import (
    COLOR_CHANNELS_LIST,
    process_comfy_magick_function,
)


class UnsharpMask:
    """
    Sharpens the image using unsharp mask filter. We convolve the image with a Gaussian operator of the given radius
    and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and
    unsharp_mask() selects a suitable radius for you.


    Parameters:
    radius (numbers.Real) – the radius of the Gaussian, in pixels, not counting the center pixel
    sigma (numbers.Real) – the standard deviation of the Gaussian, in pixels
    amount (numbers.Real) – the percentage of the difference between the original and the blur image that is added back
        into the original
    threshold (numbers.Real) – the threshold in pixels needed to apply the difference amount.
    channel (basestring) – Optional color channel to target. See CHANNELS
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
                "Amount": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 8.0, "step": 0.1},
                ),
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 4.0, "step": 0.1},
                ),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processUnsharpMask"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Unsharp Mask Image Effect"

    def processUnsharpMask(
        self, IMAGE, Radius, Sigma, Amount, Threshold, Color_Channel, Grayscale
    ):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.unsharp_mask,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            amount=Amount,
            threshold=Threshold,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
