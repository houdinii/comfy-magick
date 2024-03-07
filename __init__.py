from .CropByAspectRatio import CropByAspectRatio

NODE_CLASS_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CropByAspectRatio": "Crop By Aspect Ratio",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
