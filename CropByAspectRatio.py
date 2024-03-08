import wand.image
from .utilities import calculate_aspect_ratio


class CropByAspectRatio:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "WAND_IMAGES": ("WAND_IMAGES",),
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
    RETURN_TYPES = ("WAND_IMAGES",)
    FUNCTION = "processCropByAspectRatio"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "ComfyMagick"

    def processCropByAspectRatio(self, WAND_IMAGES, aspect_ratio, gravity):
        old_width, old_height = WAND_IMAGES[0].size
        new_width, new_height = calculate_aspect_ratio(aspect_ratio, old_width, old_height)

        for i in range(len(WAND_IMAGES)):
            if gravity in wand.image.GRAVITY_TYPES:
                WAND_IMAGES[i].crop(width=new_width, height=new_height, gravity=gravity)
            else:
                WAND_IMAGES[i].crop(width=new_width, height=new_height)
        return (WAND_IMAGES,)
