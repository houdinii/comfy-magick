from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Colorize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Color": ("STRING", {"default": "yellow"}),
                "Alpha": ("STRING", {"default": "rgb(10, 0%, 20%)"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processColorize"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Colorize Effect"

    def processColorize(self, IMAGE, Color, Alpha, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.colorize,
            IMAGE=IMAGE,
            color=Color,
            alpha=Alpha,
            GRAY=Grayscale,
        )
        return (result,)
