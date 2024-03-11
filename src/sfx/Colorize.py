from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Colorize:
    """
    Blends a given fill color over the image. The amount of blend is determined by the color channels given by the alpha argument.

    Parameters:
    color (wand.color.Color) – Color to paint image with.
        alpha (wand.color.Color) – Defines how to blend color.
    """

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
    TITLE = "ComfyMagick - Colorize Effect"

    def processColorize(self, IMAGE, Color, Alpha, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.colorize,
            IMAGE=IMAGE,
            color=Color,
            alpha=Alpha,
            GRAY=Grayscale,
        )
        return (result,)
