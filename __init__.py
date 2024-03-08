from .src.transform.CropByAspectRatio import CropByAspectRatio
from .src.sfx.BlueShift import BlueShift
from .src.sfx.Charcoal import Charcoal
from .src.sfx.AddNoise import AddNoise
from .src.sfx.Colorize import Colorize
from .src.sfx.FX import FX

NODE_CLASS_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio,
    "BlueShift": BlueShift,
    "Charcoal": Charcoal,
    "AddNoise": AddNoise,
    "Colorize": Colorize,
    "FX": FX,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio.TITLE,
    "BlueShift": BlueShift.TITLE,
    "Charcoal": Charcoal.TITLE,
    "AddNoise": AddNoise.TITLE,
    "Colorize": Colorize.TITLE,
    "FX": FX.TITLE,
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
