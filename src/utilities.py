import numpy as np
import torch
from wand.image import Image as WandImage
from PIL import Image as PILImage
import io


def wand_to_pil(wand_img: WandImage):
    # It needs to go back to PIL now and then back to tensor
    img_buffer = np.asarray(bytearray(wand_img.make_blob(format="png")), dtype="uint8")
    bytesio = io.BytesIO(bytes(img_buffer))
    pil_img = PILImage.open(bytesio)
    return pil_img


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


def getEmptyResults(batch, height, width, color_channels=3, dtype=torch.float32):
    return torch.zeros(batch, height, width, color_channels, dtype=dtype)


def pure_pil_alpha_to_color_v2(image, color=(255, 255, 255)):
    """Alpha composite an RGBA Image with a specified color.

    Simpler, faster version than the solutions above.

    Source: http://stackoverflow.com/a/9459208/284318

    Keyword Arguments:
    image -- PIL RGBA Image object
    color -- Tuple r, g, b (default 255, 255, 255)

    """
    image.load()  # needed for split()
    background = PILImage.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    return background


# These lists need to be trimmed and rearranged
COLOR_CHANNELS_LIST = [
    "red",
    "gray",
    "cyan",
    "green",
    "magenta",
    "blue",
    "yellow",
    "alpha",
    "opacity",
    "black",
    "index",
    "composite_channels",
    "all_channels",
    "sync_channels",
    "default_channels",
]

PIXEL_INTERPOLATE_METHODS_LIST = [
    "undefined",
    "average",
    "average9",
    "average16",
    "background",
    "bilinear",
    "blend",
    "catrom",
    "integer",
    "mesh",
    "nearest",
    "spline",
]

NOISE_TYPE_LIST = [
    "gaussian",
    "impulse",
    "laplacian",
    "multiplicative_gaussian",
    "poisson",
    "random",
    "uniform",
]

GRAVITY_LIST = [
    "center",
    "north",
    "north_west",
    "north_east",
    "south",
    "south_west",
    "south_east",
    "east",
    "west",
]

ASPECT_RATIO_LIST = [
    "1:1",
    "2:1",
    "16:9",
    "3:2",
    "4:3",
    "1:2",
    "9:16",
    "2:3",
    "3:4",
]
