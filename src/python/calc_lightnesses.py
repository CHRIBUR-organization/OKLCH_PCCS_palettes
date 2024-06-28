from calc_lightnesses_helper import calc_lightnesses_helper
from format_lightness import format_lightness
from lightness_coefficients_dict import LIGHTNESS_COEFFICIENTS_DICT
from my_types import TonesThatDetermineLightnessCoefficientsLowHigh


def calc_lightnesses(
    lightness_low: float, lightness_high: float
) -> dict[TonesThatDetermineLightnessCoefficientsLowHigh, str]:
    """_summary_

    Parameters
    ----------
    lightness_low : float
        _description_
    lightness_high : float
        _description_

    Returns
    -------
    dict[TonesThatDetermineLightnessCoefficientsLowHigh, float]
        _description_

    """

    def calc(coefficient_low: int, coefficient_high: int) -> float:
        """_summary_

        Parameters
        ----------
        coefficient_low : int
            _description_
        coefficient_high : int
            _description_

        Returns
        -------
        float
            _description_

        """
        return calc_lightnesses_helper(
            lightness_low, coefficient_low, lightness_high, coefficient_high
        )

    return {
        item[0]: format_lightness(calc(*(item[1])))
        for item in tuple(LIGHTNESS_COEFFICIENTS_DICT.items())
    }
