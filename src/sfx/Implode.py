import torch
from ..utilities import wand_to_pil, getEmptyResults, PIXEL_INTERPOLATE_METHODS_LIST
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Amount": (
                    "FLOAT",
                    {"min": 0.0, "max": 1.0, "step": 0.05, "default": 0.0},
                ),
                "Pixel_Interpolate_Method": (PIXEL_INTERPOLATE_METHODS_LIST,),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processImplode"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Implode Effect"

    def processImplode(self, IMAGE, Amount, Pixel_Interpolate_Method):
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
                wand_img.implode(amount=Amount, method=Pixel_Interpolate_Method)
                result_b = wand_to_pil(wand_img)
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
