from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Tint:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Color": ("STRING", {"default": "rgb(10%, 0%, 20%)"}),
                "Alpha": ("STRING", {"default": ""}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processTint"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Tint Effect"

    def processTint(self, IMAGE, Color, Alpha, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.tint,
            IMAGE=IMAGE,
            color=Color,
            alpha=Alpha,
            GRAY=Grayscale,
        )
        return (result,)
