# This node will take in an IMAGE object, which is a tensor of shape [B, H, W, C] and output a custom object
# that contains an array of all the images in Wand format, where len = B and channels is always RGB. (For now, anyway.
# I might make conversion nodes, but they will always have to go back to RGB for comfy itself.)

import PIL
import PIL.Image
import io

from wand.image import Image


class ComfyImageToWand:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("WAND_IMAGES",)
    FUNCTION = "processComfyImageToWand"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/Utilities"

    def processComfyImageToWand(self, images):
        batch, height, width, channels = images.shape
        results = []
        for b in range(batch):
            img_b = images[b] * 255.0
            img_b = PIL.Image.fromarray(img_b.numpy().astype("uint8"), "RGB")
            blob = io.BytesIO()
            img_b.save(blob, format="PNG")
            blob.seek(0)
            with Image(blob=blob.getvalue()) as wand_img:
                results.append(Image(image=wand_img))  # Clone the wand image to ensure it stays valid
            blob.close()
        return results,
