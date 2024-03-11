from ..utilities import process_comfy_magick_function
from wand.image import Image as WandImage


class Kuwahara:
    """
    Edge preserving noise reduction filter.

    https://en.wikipedia.org/wiki/Kuwahara_filter

    If sigma is not given, the value will be calculated as:
    sigma = radius - 0.5

    To match original algorithm’s behavior, increase radius value by one:
    myImage.kuwahara(myRadius + 1, mySigma)

    Warning
    This class method is only available with ImageMagick 7.0.8-41, or greater.

    Parameters:
    radius (numbers.Real) – Size of the filter aperture.
    sigma (numbers.Real) – Standard deviation of Gaussian filter.

    Raises:
    WandLibraryVersionError – If system’s version of ImageMagick does not support this method.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 2.0, "step": 0.1},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processKuwahara"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Kuwahara Image Effect"

    def processKuwahara(self, IMAGE, Radius, Sigma, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.kuwahara,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            GRAY=Grayscale,
        )
        return (result,)
