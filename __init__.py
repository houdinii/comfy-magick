from .CropByAspectRatio import CropByAspectRatio
from .BlueShift import BlueShift
from .Charcoal import Charcoal
from .AddNoise import AddNoise

NODE_CLASS_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio,
    "BlueShift": BlueShift,
    "Charcoal": Charcoal,
    "AddNoise": AddNoise,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CropByAspectRatio": "Crop By Aspect Ratio",
    "BlueShift": "Blue Shift Effect",
    "Charcoal": "Charcoal Effect",
    "AddNoise": "Add Noise Effect",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
