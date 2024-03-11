from ..utilities import (
    process_comfy_magick_function,
)
from wand.image import Image as WandImage


class Despeckle:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Grayscale": (["True", "False"], {"default": "False"}),
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processDespeckle"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Despeckle Image Effect"

    def processDespeckle(self, IMAGE, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.despeckle, IMAGE=IMAGE, GRAY=Grayscale
        )
        return (result,)
