import torch
from ..utilities import wand_to_pil, getEmptyResults, PIXEL_INTERPOLATE_METHODS_LIST
from PIL import Image as PILImage
from wand.image import Image as WandImage
import io
import numpy as np

# TODO: MAKE THE PHOTO SHIFT AUTOMATIC WITHOUT NEEDING TWO INPUTS!


class Stereogram:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "LEFT_EYE_IMAGE": ("IMAGE",),
                "RIGHT_EYE_IMAGE": ("IMAGE",),
            }
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "processStereogram"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick/SFX"
    TITLE = "Stereogram Effect"

    def processStereogram(self, LEFT_EYE_IMAGE, RIGHT_EYE_IMAGE):
        batch, height, width, channels = LEFT_EYE_IMAGE.shape
        r_batch, r_height, r_width, r_channels = RIGHT_EYE_IMAGE.shape

        if batch != r_batch or height != r_height or width != r_width or channels != r_channels:
            print("darn")
            return (LEFT_EYE_IMAGE, )

        result = getEmptyResults(
            batch=batch, height=height, width=width, color_channels=channels
        )

        for b in range(batch):
            result_b = None
            l_img_b = LEFT_EYE_IMAGE[b] * 255.0
            l_img_b = PILImage.fromarray(l_img_b.numpy().astype("uint8"), "RGB")
            l_blob = io.BytesIO()
            l_img_b.save(l_blob, format="PNG")
            l_blob.seek(0)

            r_img_b = RIGHT_EYE_IMAGE[b] * 255.0
            r_img_b = PILImage.fromarray(r_img_b.numpy().astype("uint8"), "RGB")
            r_blob = io.BytesIO()
            r_img_b.save(r_blob, format="PNG")
            r_blob.seek(0)

            with WandImage(blob=l_blob.getvalue()) as l_wand_img:
                with WandImage(blob=r_blob.getvalue()) as r_wand_img:
                    with WandImage.stereogram(left=l_wand_img, right=r_wand_img) as stereo_img:
                        print("got here")
                        result_b = wand_to_pil(stereo_img)
            result_b = torch.tensor(np.array(result_b)) / 255.0

            try:
                result[b] = result_b
                print(f"result shape: {result.shape}")
            except Exception as e:
                print(f"An error occurred in the {self.FUNCTION} node: {e}")

        return (result,)
