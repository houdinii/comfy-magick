from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class Charcoal:
    """
    Transform an image into a simulated charcoal drawing.

    Parameters:
    radius (numbers.Real) – The size of the Gaussian operator.
    sigma (numbers.Real) – The standard deviation of the Gaussian.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 1.0, "default": 0.5, "step": 0.01},
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processCharcoal"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "ComfyMagick - Charcoal Effect"

    def processCharcoal(self, IMAGE, Radius, Sigma):
        # It's auto grayscale
        result = process_comfy_magick_function(
            FUNCTION=WandImage.charcoal,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
        )
        print(result.shape)

        return (result,)
