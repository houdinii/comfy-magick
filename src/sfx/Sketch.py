from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Sketch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "step": 0.1, "default": 1.0},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 10.0, "step": 0.25, "default": 0.0},
                ),
                "Angle": (
                    "FLOAT",
                    {"min": 0.0, "max": 360.0, "step": 0.5, "default": 0.0},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSketch"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Sketch Effect"

    def processSketch(self, IMAGE, Radius, Sigma, Angle, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.sketch,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            angle=Angle,
            GRAY=Grayscale,
        )
        return (result,)
