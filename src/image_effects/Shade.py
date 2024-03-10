import torch
from ..utilities import (
    wand_to_pil,
    getEmptyResults,
)
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Azimuth": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 2.0, "step": 0.1},
                ),
                "Elevation": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.1},
                ),
                "Gray": (["True", "False"],),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processShade"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Image Effects"
    TITLE = "Shade Image Effect"

    def processShade(self, IMAGE, Azimuth, Elevation, Gray):
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
                if Gray == "True":
                    gray_bool = True
                else:
                    gray_bool = False
                wand_img.shade(azimuth=Azimuth, elevation=Elevation, gray=gray_bool)
                result_b = wand_to_pil(wand_img).convert(mode="RGB")
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
