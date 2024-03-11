from wand.image import Image as WandImage

from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function


# http://www.imagemagick.org/script/fx.php
class FX:
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
    TITLE = "FX Effect"

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
