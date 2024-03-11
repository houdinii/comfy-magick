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
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processDespeckle"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Despeckle Image Effect"

    def processDespeckle(self, IMAGE):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.despeckle, IMAGE=IMAGE
        )
        return (result,)
