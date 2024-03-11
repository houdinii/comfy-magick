from wand.image import Image as WandImage

from ..utilities import process_comfy_magick_function


class WaveletDenoise:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Threshold": (
                    "FLOAT",
                    {"min": 0.0, "max": 500.0, "step": 0.1, "default": 0.0},
                ),
                "Softness": (
                    "FLOAT",
                    {"min": 0.0, "max": 500.0, "step": 0.1, "default": 0.0},
                ),
                "Grayscale": (["True", "False"], {"default": "False"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processWaveletDenoise"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "WaveletDenoise Effect"

    def processWaveletDenoise(self, IMAGE, Threshold, Softness, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.wavelet_denoise,
            IMAGE=IMAGE,
            threshold=Threshold,
            softness=Softness,
            GRAY=Grayscale,
        )
        return (result,)
