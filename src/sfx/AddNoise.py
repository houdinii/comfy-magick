import torch
from ..utilities import (
    wand_to_pil,
    getEmptyResults,
    COLOR_CHANNELS_LIST,
    NOISE_TYPE_LIST,
)
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np


class AddNoise:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Noise_Type": (NOISE_TYPE_LIST,),
                "Color_Channel": (COLOR_CHANNELS_LIST, {"default": "all_channels"}),
                "Attenuate": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.0, "step": 0.1},
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processAddNoise"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Add Noise Effect"

    def processAddNoise(self, IMAGE, Noise_Type, Color_Channel, Attenuate):
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
                wand_img.noise(
                    noise_type=Noise_Type, attenuate=Attenuate, channel=Color_Channel
                )

                result_b = wand_to_pil(wand_img)
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
