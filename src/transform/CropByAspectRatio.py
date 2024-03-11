import torch
import wand.image
from ..utilities import (
    calculate_aspect_ratio,
    wand_to_pil,
    getEmptyResults,
    GRAVITY_LIST,
    ASPECT_RATIO_LIST,
)
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np

# TODO: Implement native functions


class CropByAspectRatio:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "aspect_ratio": (ASPECT_RATIO_LIST,),
                "gravity": (GRAVITY_LIST,),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processCropByAspectRatio"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick"
    TITLE = "ComfyMagick - Crop By Aspect Ratio"

    def processCropByAspectRatio(self, IMAGE, aspect_ratio, gravity):
        batch, height, width, channels = IMAGE.shape
        new_width, new_height = calculate_aspect_ratio(aspect_ratio, width, height)

        result = getEmptyResults(
            batch=batch, height=new_height, width=new_width, color_channels=channels
        )

        for b in range(batch):
            result_b = None
            img_b = IMAGE[b] * 255.0
            img_b = PILImage.fromarray(img_b.numpy().astype("uint8"), "RGB")
            blob = io.BytesIO()
            img_b.save(blob, format="PNG")
            blob.seek(0)

            with WandImage(blob=blob.getvalue()) as wand_img:

                if gravity in wand.image.GRAVITY_TYPES:
                    wand_img.crop(width=new_width, height=new_height, gravity=gravity)
                else:
                    wand_img.crop(width=new_width, height=new_height)

                result_b = wand_to_pil(wand_img)
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
