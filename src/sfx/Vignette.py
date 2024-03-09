import torch
from ..utilities import wand_to_pil, getEmptyResults, PIXEL_INTERPOLATE_METHODS_LIST, pure_pil_alpha_to_color_v2
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


# TODO: FIND A WAY TO DYNAMICALLY CHANGE MIN AND MAX DEPENDING ON IMAGE INPUT DIMENSIONS!!
# TODO: IT'S ONLY COMING OUT WHITE!! WTF?!?

class Vignette:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Radius": (
                    "FLOAT",
                    {"min": 0.0, "max": 1000.0, "step": 0.1, "default": 1.0},
                ),
                "Sigma": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "step": 0.25, "default": 0.0},
                ),
                "X": (
                    "INT",
                    {"min": -500, "max": 500, "default": 0},
                ),
                "Y": (
                    "INT",
                    {"min": -500, "max": 500, "default": 0},
                ),
                "Red": (
                    "INT",
                    {"min": 0, "max": 255, "default": 0},
                ),
                "Green": (
                    "INT",
                    {"min": 0, "max": 255, "default": 0},
                ),
                "Blue": (
                    "INT",
                    {"min": 0, "max": 255, "default": 0},
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processVignette"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Vignette Effect"

    def processVignette(self, IMAGE, Radius, Sigma, X, Y, Red, Green, Blue):
        batch, height, width, channels = IMAGE.shape
        result = getEmptyResults(
            batch=batch, height=height, width=width, color_channels=channels
        )

        for b in range(batch):
            result_b = None
            img_b = IMAGE[b] * 255.0
            img_b = PILImage.fromarray(img_b.numpy().astype("uint8"), "RGB")
            blob = io.BytesIO()
            img_b.save(blob, format="PNG")
            blob.seek(0)

            with WandImage(blob=blob.getvalue()) as wand_img:
                wand_img.vignette(radius=Radius, sigma=Sigma, x=X, y=Y)
                # We need to add a pure (X,X,X) BG Here and combine it all!!
                result_b = pure_pil_alpha_to_color_v2(wand_to_pil(wand_img), color=(Red, Green, Blue))
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
