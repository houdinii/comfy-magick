from wand.image import Image as WandImage

from ..utilities import (
    COLOR_CHANNELS_LIST,
    NOISE_TYPE_LIST,
    process_comfy_magick_function,
)


class AddNoise:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Noise_Type": (NOISE_TYPE_LIST,),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Attenuate": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.0, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processAddNoise"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Add Noise Effect"

    def processAddNoise(self, IMAGE, Noise_Type, Color_Channel, Attenuate, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.noise,
            IMAGE=IMAGE,
            attenuate=Attenuate,
            noise_type=Noise_Type,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
