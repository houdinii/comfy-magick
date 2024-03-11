from wand.image import Image as WandImage

from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function


class Solarize:
    """
    Simulates extreme overexposure.

    Parameters:
    threshold (numbers.Real) – between 0.0 and quantum_range.
    channel (basestring) – Optional color channel to target. See CHANNELS
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "step": 0.05, "default": 1.0},
                ),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSolarize"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Solarize Effect"

    def processSolarize(self, IMAGE, Threshold, Color_Channel, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.solarize,
            IMAGE=IMAGE,
            threshold=Threshold,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
