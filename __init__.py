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
from .src.image_effects.GaussianBlur import GaussianBlur
from .src.image_effects.MotionBlur import MotionBlur
from .src.image_effects.RotationalBlur import RotationalBlur
from .src.image_effects.SelectiveBlur import SelectiveBlur

from .src.image_effects.Despeckle import Despeckle
from .src.image_effects.Edge import Edge
from .src.image_effects.Emboss import Emboss
from .src.image_effects.Kuwahara import Kuwahara
from .src.image_effects.Shade import Shade
from .src.image_effects.Sharpen import Sharpen
from .src.image_effects.AdaptiveSharpen import AdaptiveSharpen
from .src.image_effects.UnsharpMask import UnsharpMask

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
    "GaussianBlur": GaussianBlur,
    "MotionBlur": MotionBlur,
    "RotationalBlur": RotationalBlur,
    "SelectiveBlur": SelectiveBlur,
    "Despeckle": Despeckle,
    "Edge": Edge,
    "Emboss": Emboss,
    "Kuwahara": Kuwahara,
    "Shade": Shade,
    "Sharpen": Sharpen,
    "AdaptiveSharpen": AdaptiveSharpen,
    "UnsharpMask": UnsharpMask,
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
    "GaussianBlur": GaussianBlur.TITLE,
    "MotionBlur": MotionBlur.TITLE,
    "RotationalBlur": RotationalBlur.TITLE,
    "SelectiveBlur": SelectiveBlur.TITLE,
    "Despeckle": Despeckle.TITLE,
    "Edge": Edge.TITLE,
    "Emboss": Emboss.TITLE,
    "Kuwahara": Kuwahara.TITLE,
    "Shade": Shade.TITLE,
    "Sharpen": Sharpen.TITLE,
    "AdaptiveSharpen": AdaptiveSharpen.TITLE,
    "UnsharpMask": UnsharpMask.TITLE,
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
