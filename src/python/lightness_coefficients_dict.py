from constants_for_calc_lightness import ConstantsForCalcLightness
from lightness_coefficients_low_high import LightnessCoefficientsLowHigh
from my_types import TonesThatDetermineLightnessCoefficientsLowHigh

LIGHTNESS_COEFFICIENTS_DICT: dict[
    TonesThatDetermineLightnessCoefficientsLowHigh, LightnessCoefficientsLowHigh
] = {
    ({"b", "dp"}, "s"): LightnessCoefficientsLowHigh(
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_MIDDLE_WEIGHT,
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_MIDDLE_WEIGHT,
    ),
    ({"lt", "dk"}, "d"): LightnessCoefficientsLowHigh(
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_HEAVIER_WEIGHT,
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_LIGHTER_WEIGHT,
    ),
    ({"lt", "dk"}, "sf"): LightnessCoefficientsLowHigh(
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_LIGHTER_WEIGHT,
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_HEAVIER_WEIGHT,
    ),
    ({"p", "dkg"}, "g"): LightnessCoefficientsLowHigh(
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_HEAVY_WEIGHT,
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_LIGHT_WEIGHT,
    ),
    ({"p", "dkg"}, "ltg"): LightnessCoefficientsLowHigh(
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_LIGHT_WEIGHT,
        ConstantsForCalcLightness.LIGHTNESS_COEFFICIENT_HEAVY_WEIGHT,
    ),
}
