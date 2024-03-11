from ..utilities import process_comfy_magick_function
from wand.image import Image as WandImage


class Edge:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 0.0, "step": 0.1},
                ),
                "Grayscale": (["True", "False"], {"default": "True"}),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processEdge"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "ComfyMagick - Edge Image Effect"

    def processEdge(self, IMAGE, Radius, Grayscale):
        result = process_comfy_magick_function(
            FUNCTION=WandImage.edge, IMAGE=IMAGE, radius=Radius, GRAY=Grayscale
        )
        return (result,)
