from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function
from wand.image import Image as WandImage


class GaussianBlur:
    """
    Blurs the image. We convolve the image with a gaussian operator of the given radius and standard deviation (sigma).
    For reasonable results, the radius should be larger than sigma. Use a radius of 0 and blur() selects a suitable
    radius for you.

    Parameters:
    radius (numbers.Real) – the radius of the blur, in pixels, not counting the center pixel
    sigma (numbers.Real) – the standard deviation of the blur, in pixels
    channel (basestring) – Optional color channel to target. See CHANNELS
    """

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
    TITLE = "ComfyMagick - Gaussian Blur Image Effect"

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
