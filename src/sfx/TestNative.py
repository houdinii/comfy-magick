import torch
from ..utilities import getEmptyResults, process_comfy_magick_function
from wand.image import Image as WandImage
import numpy as np


def test_function(image, factor):
    print("\n\n")
    print(f"Image (type): {type(image)}")
    print(f"Factor: {factor}")
    print("\n\n")


class TestNative:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "Factor": (
                    "FLOAT",
                    {"min": 0.0, "max": 100.0, "default": 1.5, "step": 0.05},
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processTestNative"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick"
    TITLE = "TestNative"

    def processTestNative(self, IMAGE, Factor):
        process_comfy_magick_function(test_function, image=IMAGE, factor=Factor)

        batch, height, width, channels = IMAGE.shape
        result = getEmptyResults(
            batch=batch, height=height, width=width, color_channels=channels
        )

        for b in range(batch):
            img_b = IMAGE[b] * 255.0
            with WandImage.from_array(img_b.numpy().astype("uint8"), "RGB") as wand_img:
                wand_img.blue_shift(factor=Factor)
                result_b = torch.tensor(np.array(wand_img)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
