from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function
from wand.image import Image as WandImage


class MotionBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Angle": (
                    "FLOAT",
                    {"min": 0.0, "max": 360.0, "default": 0.0, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processMotionBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "ComfyMagick - Motion Blur Image Effect"

    def processMotionBlur(self, IMAGE, Radius, Sigma, Angle, Color_Channel, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.motion_blur,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            angle=Angle,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
