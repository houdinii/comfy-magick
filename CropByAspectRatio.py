import PIL
import torch
import PIL.Image
import numpy as np
import io
import tempfile

import wand.image
from wand.image import Image


def calculate_aspect_ratio(aspect_ratio, width, height):
    aspect_ratio = aspect_ratio.split(":")
    ratio_width = int(aspect_ratio[0])
    ratio_height = int(aspect_ratio[1])

    if width / height > ratio_width / ratio_height:
        new_width = int(height * (ratio_width / ratio_height))
        new_height = height
    else:
        new_width = width
        new_height = int(width * (ratio_height / ratio_width))

    return new_width, new_height


def wand_to_pil(wand_img: Image):
    # It needs to go back to PIL now and then back to tensor
    img_buffer = np.asarray(bytearray(wand_img.make_blob(format="png")), dtype="uint8")
    bytesio = io.BytesIO(bytes(img_buffer))
    pil_img = PIL.Image.open(bytesio)
    return pil_img


def process_function_on_image(image: torch.Tensor, function, *args):
    # Some parts are from EllangoK/ComfyUI-post-processing-nodes
    # namely torch.Tensor -> PIL.Image conversion formula that takes batches into account.

    batch_size, height, width, channels = image.shape
    result = torch.zeros_like(image)

    for b in range(batch_size):
        img_b = image[b] * 255.0
        img_b = PIL.Image.fromarray(
            img_b.numpy().astype("uint8"), "RGB"
        )  # It's now in PIL Form, and needs to be in wand form
        with tempfile.NamedTemporaryFile(suffix=".png", dir=".", delete=False) as tmp:
            img_b.save(tmp.name, format="png")
            with Image(filename=tmp.name) as wand_img:
                result_b = function(wand_img, args)
        result_b = torch.tensor(np.array(result_b)) / 255.0
        result[b] = result_b
    return result


def crop_by_aspect_ratio(image: PIL.Image, ratio: str, gravity: str = None):
    batch_size, old_height, old_width, channels = image.shape
    # size_tensor = list(image.shape)
    print("Got Here")
    print(f"Image Type: {type(image)}")
    print(f"Image Size: {old_width}, {old_height}")

    # ratio = ratio[0]
    print(f"Ratio: {ratio}")

    # old_width, old_height = size_tensor[2], size_tensor[1]
    new_width, new_height = calculate_aspect_ratio(ratio, old_width, old_height)

    # Now, create the 'result' tensor to match the new shape
    result = torch.zeros(
        batch_size,
        new_height,
        new_width,
        channels,
        dtype=image.dtype,
        device=image.device,
    )

    print(f"Old width, height: {old_width}, {old_height}")
    print(f"New width, height: {new_width}, {new_height}")

    for b in range(batch_size):
        img_b = image[b] * 255.0
        img_b = PIL.Image.fromarray(
            img_b.numpy().astype("uint8"), "RGB"
        )  # It's now in PIL Form, and needs to be in wand form
        with tempfile.NamedTemporaryFile(suffix=".png", dir=".", delete=False) as tmp:
            img_b.save(tmp.name, format="png")
            with Image(filename=tmp.name) as wand_img:
                if gravity in wand.image.GRAVITY_TYPES:
                    print("cropping with gravity")
                    wand_img.crop(width=new_width, height=new_height, gravity=gravity)
                    print(f"wand image size: {wand_img.size}")
                else:
                    print("cropping without gravity")
                    wand_img.crop(width=new_width, height=new_height)
                    print(f"wand image size: {wand_img.size}")
                result_b = wand_to_pil(wand_img)
        result_b = torch.tensor(np.array(result_b)) / 255.0
        result[b] = result_b
    return result


aspect_ratios = [
    "custom",
    "1:1 square 512x512",
    "1:1 square 1024x1024",
    "2:3 portrait 512x768",
    "3:4 portrait 512x682",
    "3:2 landscape 768x512",
    "4:3 landscape 682x512",
    "16:9 cinema 910x512",
    "1.85:1 cinema 952x512",
    "2:1 cinema 1024x512",
    "2.39:1 anamorphic 1224x512",
]


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

    @staticmethod
    def processCropByAspectRatio(self, image, aspect_ratio, gravity):
        result = crop_by_aspect_ratio(image, aspect_ratio, gravity=gravity)
        return (result,)
