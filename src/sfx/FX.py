from wand.image import Image as WandImage

from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function


class FX:
    """
    Manipulate each pixel of an image by given expression.
    FX will preserver current wand instance, and return a new instance of Image containing affected pixels.
    Defaults entire image, but can isolate affects to single color channel by passing CHANNELS value to channel parameter.

    See also
    The anatomy of FX expressions can be found at http://www.imagemagick.org/script/fx.php

    Parameters:
    expression (basestring) – The entire FX expression to apply
    channel (CHANNELS) – Optional channel to target.

    Returns:
    A new instance of an image with expression applied

    Return type:
    Image
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "FX_Filter": (
                    "STRING",
                    {"default": "(hue > 0.9 || hue < 0.1) ? u : lightness"},
                ),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            },
            "optional": {
                "NOTES": (
                    "STRING",
                    {"default": "httpd://www.imagemagick.org/script/fx.php"},
                )
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processFX"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "ComfyMagick - FX Effect"

    def processFX(self, IMAGE, FX_Filter, Color_Channel, NOTES, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.fx,
            IMAGE=IMAGE,
            expression=FX_Filter,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
        # with wand_img.fx(FX_Filter, channel=Color_Channel) as filtered_img:
