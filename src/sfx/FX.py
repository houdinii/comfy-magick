import torch
from ..utilities import wand_to_pil, getEmptyResults
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


# http://www.imagemagick.org/script/fx.php
class FX:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE", ),
                "FX_Filter": ("STRING", {"default": '(hue > 0.9 || hue < 0.1) ? u : lightness'}),
            },
            "optional": {
                "NOTES": ("STRING", {"default": "httpd://www.imagemagick.org/script/fx.php"})
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processFX"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "FX Effect"

    def processFX(self, IMAGE, FX_Filter, NOTES):
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
                with wand_img.fx(FX_Filter) as filtered_img:
                    result_b = wand_to_pil(filtered_img)
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
