import PIL
import torch
import PIL.Image
import numpy as np
import tempfile

import wand.image
from wand.image import Image

from .utilities import wand_to_pil, calculate_aspect_ratio


def crop_by_aspect_ratio(image, ratio: str, gravity: str = None):
    batch_size, old_height, old_width, channels = image.shape
    new_width, new_height = calculate_aspect_ratio(ratio, old_width, old_height)

    result = torch.zeros(
        batch_size,
        new_height,
        new_width,
        channels,
        dtype=image.dtype,
        device=image.device,
    )

    for b in range(batch_size):
        img_b = image[b] * 255.0
        img_b = PIL.Image.fromarray(
            img_b.numpy().astype("uint8"), "RGB"
        )
        with tempfile.NamedTemporaryFile(suffix=".png", dir=".", delete=False) as tmp:
            img_b.save(tmp.name, format="png")
            with Image(filename=tmp.name) as wand_img:
                if gravity in wand.image.GRAVITY_TYPES:
                    wand_img.crop(width=new_width, height=new_height, gravity=gravity)
                else:
                    wand_img.crop(width=new_width, height=new_height)
                result_b = wand_to_pil(wand_img)
        result_b = torch.tensor(np.array(result_b)) / 255.0
        result[b] = result_b
    return result


class CropByAspectRatio:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "aspect_ratio": (
                    [
                        "1:1",
                        "2:1",
                        "16:9",
                        "3:2",
                        "4:3",
                        "1:2",
                        "9:16",
                        "2:3",
                        "3:4",
                    ],
                ),
                "gravity": (
                    [
                        "center",
                        "north",
                        "north_west",
                        "north_east",
                        "south",
                        "south_west",
                        "south_east",
                        "east",
                        "west",
                    ],
                ),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processCropByAspectRatio"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick"

    def processCropByAspectRatio(self, image, aspect_ratio, gravity):
        result = crop_by_aspect_ratio(image, aspect_ratio, gravity=gravity)
        return (result,)
