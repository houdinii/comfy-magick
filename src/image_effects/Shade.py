from wand.image import Image as WandImage

from ..utilities import (
    process_comfy_magick_function,
)


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Azimuth": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 2.0, "step": 0.1},
                ),
                "Elevation": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "True"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processShade"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Shade Image Effect"

    def processShade(self, IMAGE, Azimuth, Elevation, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.shade,
            IMAGE=IMAGE,
            azimuth=Azimuth,
            elevation=Elevation,
            GRAY=Grayscale,
        )
        return (result,)
