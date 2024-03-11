from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class BlueShift:
    """
    Mutes colors of the image by shifting blue values.

    Parameters:
    factor (numbers.Real) – Amount to adjust values.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Factor": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.05},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processBlueShift"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Blue Shift Effect"

    def processBlueShift(self, IMAGE, Factor, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.blue_shift,
            IMAGE=IMAGE,
            factor=Factor,
            GRAY=Grayscale,
        )
        return (result,)
