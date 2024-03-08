from .CropByAspectRatio import CropByAspectRatio
from .ComfyImageToWand import ComfyImageToWand
from .WandToComfyImage import WandToComfyImage

NODE_CLASS_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio,
    "ComfyImageToWand": ComfyImageToWand,
    "WandToComfyImage": WandToComfyImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CropByAspectRatio": "Crop By Aspect Ratio",
    "ComfyImageToWand": "Comfy Image To Wand Image",
    "WandToComfyImage": "Wand Image To Comfy Image",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
