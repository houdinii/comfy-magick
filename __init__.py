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
from .src.sfx.Solarize import Solarize
from .src.sfx.Swirl import Swirl
from .src.sfx.Tint import Tint
from .src.sfx.Vignette import Vignette
from .src.sfx.WaveletDenoise import WaveletDenoise

from .src.image_effects.Blur import Blur
from .src.image_effects.AdaptiveBlur import AdaptiveBlur

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
    "Solarize": Solarize,
    "Swirl": Swirl,
    "Tint": Tint,
    "Vignette": Vignette,
    "WaveletDenoise": WaveletDenoise,
    "Blur": Blur,
    "AdaptiveBlur": AdaptiveBlur,
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
    "Solarize": Solarize.TITLE,
    "Swirl": Swirl.TITLE,
    "Tint": Tint.TITLE,
    "Vignette": Vignette.TITLE,
    "WaveletDenoise": WaveletDenoise.TITLE,
    "Blur": Blur.TITLE,
    "AdaptiveBlur": AdaptiveBlur.TITLE,
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
