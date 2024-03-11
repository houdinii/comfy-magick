from ..utilities import (
    COLOR_CHANNELS_LIST,
    process_comfy_magick_function,
)
from wand.image import Image as WandImage


class AdaptiveBlur:
    """
    Adaptively blurs the image by decreasing Gaussian as the operator approaches detected edges.

    Parameters:
    radius (numbers.Real) – size of gaussian aperture.
    sigma (numbers.Real) – Standard deviation of the gaussian filter.
    channel (basestring) – Apply the blur effect on a specific channel. See CHANNELS.
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
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processAdaptiveBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "ComfyMagick - Adaptive Blur Image Effect"

    def processAdaptiveBlur(self, IMAGE, Radius, Color_Channel, Sigma, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.adaptive_blur,
            IMAGE=IMAGE,
            sigma=Sigma,
            radius=Radius,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
