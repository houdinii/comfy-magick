# This node will take in an array of Wand Image objects and convert them back into a tensor of shape [B, H, W, C]
import numpy as np
import torch

from .utilities import wand_to_pil


class WandToComfyImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "WAND_IMAGES": ("WAND_IMAGES",),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processWandToComfyImage"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Utilities"

    def processWandToComfyImage(self, WAND_IMAGES):
        batch = len(WAND_IMAGES)
        width, height = WAND_IMAGES[0].size
        channels = 3

        result = torch.zeros(
            batch,
            height,
            width,
            channels,
            dtype=torch.float32)

        for b in range(batch):
            result_b = wand_to_pil(WAND_IMAGES[b])
            result_b = torch.tensor(np.array(result_b)) / 255.0
            result[b] = result_b

        return (result,)
