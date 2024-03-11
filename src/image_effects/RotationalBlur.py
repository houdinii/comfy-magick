from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function
from wand.image import Image as WandImage


class RotationalBlur:
    """
    Blur an image in a radius around the center of an image.

    Warning
    Requires ImageMagick-6.8.8 or greater.

    Parameters:
    angle (numbers.Real) – Degrees of rotation to blur with.
    channel (basestring) – Optional channel to apply the effect against. See CHANNELS for a list of possible values.

    Raises:
    WandLibraryVersionError – If system’s version of ImageMagick does not support this method.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Angle": (
                    "FLOAT",
                    {"min": 0.0, "max": 360.0, "default": 0.0, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processRotationalBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "ComfyMagick - Rotational Blur Image Effect"

    def processRotationalBlur(self, IMAGE, Angle, Color_Channel, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.rotational_blur,
            IMAGE=IMAGE,
            angle=Angle,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
