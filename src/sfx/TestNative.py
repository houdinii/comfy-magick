from ..utilities import process_comfy_magick_function
from wand.image import Image as WandImage


class TestNative:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Factor": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.05},
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processTestNative"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick"
    TITLE = "TestNative"

    def processTestNative(self, IMAGE, Factor):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.blue_shift, IMAGE=IMAGE
        )
        return (result,)
