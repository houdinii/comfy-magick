from .src.transform.CropByAspectRatio import CropByAspectRatio

from .src.sfx.BlueShift import BlueShift
from .src.sfx.Charcoal import Charcoal
from .src.sfx.AddNoise import AddNoise
from .src.sfx.Colorize import Colorize
from .src.sfx.FX import FX
from .src.sfx.Implode import Implode
from .src.sfx.Sepia import Sepia
from .src.sfx.Sketch import Sketch
from .src.sfx.Stereogram import Stereogram

NODE_CLASS_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio,
    "BlueShift": BlueShift,
    "Charcoal": Charcoal,
    "AddNoise": AddNoise,
    "Colorize": Colorize,
    "FX": FX,
    "Implode": Implode,
    "Sepia": Sepia,
    "Sketch": Sketch,
    "Stereogram": Stereogram,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CropByAspectRatio": CropByAspectRatio.TITLE,
    "BlueShift": BlueShift.TITLE,
    "Charcoal": Charcoal.TITLE,
    "AddNoise": AddNoise.TITLE,
    "Colorize": Colorize.TITLE,
    "FX": FX.TITLE,
    "Implode": Implode.TITLE,
    "Sepia": Sepia.TITLE,
    "Sketch": Sketch.TITLE,
    "Stereogram": Stereogram.TITLE,
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
