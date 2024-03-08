import numpy as np
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
