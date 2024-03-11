from wand.image import Image as WandImage
from ..utilities import COLOR_CHANNELS_LIST, process_comfy_magick_function

#  TODO What is this actually doing? It's the formula using quantum range that is tripping me up.


class SelectiveBlur:
    """
    selective_blur(radius=0.0, sigma=0.0, threshold=0.0, channel=None)
    Blur an image within a given threshold.

    For best effects, use a value between 10% and 50% of quantum_range

    from wand.image import Image

    with Image(filename='photo.jpg') as img:
        # Apply 8x3 blur with a 10% threshold
        img.selective_blur(8.0, 3.0, 0.1 * img.quantum_range)

    Parameters:
    radius (numbers.Real) – Size of gaussian aperture.
    sigma (numbers.Real) – Standard deviation of gaussian operator.
    threshold (numbers.Real) – Only pixels within contrast threshold are effected. Value should be between 0.0
        and quantum_range.
    channel (basestring) – Optional color channel to target. See CHANNELS
    """

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
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 1000.0, "default": 0.0, "step": 0.25},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processSelectiveBlur"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects/Blur"
    TITLE = "ComfyMagick - Selective Blur Image Effect"

    def processSelectiveBlur(
        self, IMAGE, Radius, Sigma, Threshold, Color_Channel, Grayscale
    ):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.selective_blur,
            IMAGE=IMAGE,
            radius=Radius,
            sigma=Sigma,
            threshold=Threshold,
            channel=Color_Channel,
            GRAY=Grayscale,
        )
        return (result,)
