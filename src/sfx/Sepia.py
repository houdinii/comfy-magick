from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Sepia:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Threshold": (
                    "FLOAT",
                    {"min": 0.05, "max": 1.0, "step": 0.05, "default": 0.8},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSepia"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Sepia Effect"

    def processSepia(self, IMAGE, Threshold, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.sepia_tone,
            IMAGE=IMAGE,
            threshold=Threshold,
            GRAY=Grayscale,
        )
        return (result,)
