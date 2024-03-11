from ..utilities import (
    process_comfy_magick_function,
)
from wand.image import Image as WandImage


class Despeckle:
    """
    Applies filter to reduce noise in image.

    dirty = None (bool) Whether the image is changed or not. (NOT USED AT THIS TIME)
    property dispose  (basestring) Controls how the image data is handled during animations. Values are from
        DISPOSE_TYPES list, and can also be set. (NOT USED AT THIS TIME)
    """

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
    TITLE = "ComfyMagick - Despeckle Image Effect"

    def processDespeckle(self, IMAGE, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.despeckle, IMAGE=IMAGE, GRAY=Grayscale
        )
        return (result,)
