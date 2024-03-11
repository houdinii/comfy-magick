from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Sepia:
    """
    Creates a Sepia Tone special effect similar to a darkroom chemical toning.

    Parameters:
    threshold (numbers.Real) – The extent of the toning. Value can be between 0 & quantum_range, or 0 & 1.0. Default value is 0.8 or “80%”.
    """
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
    TITLE = "ComfyMagick - Sepia Effect"

    def processSepia(self, IMAGE, Threshold, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.sepia_tone,
            IMAGE=IMAGE,
            threshold=Threshold,
            GRAY=Grayscale,
        )
        return (result,)
