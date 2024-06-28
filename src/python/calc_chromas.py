from calc_chromas_helper import calc_chromas_helper
from chroma_coefficients import CHROMA_COEFFICIENTS
from format_chroma import format_chroma


def calc_chromas(chroma: float) -> dict[int, str]:
    """_summary_

    Parameters
    ----------
    chroma : float
        _description_

    Returns
    -------
    dict[int, str]
        _description_

    """

    def calc(coefficient: int, denominator: int = 9) -> float:
        """_summary_

        Parameters
        ----------
        coefficient : int
            _description_
        denominator : int, optional
            _description_, by default 9

        Returns
        -------
        float
            _description_

        """
        return calc_chromas_helper(chroma, coefficient, denominator)

    return {
        chroma_coefficient: format_chroma(calc(chroma_coefficient))
        for chroma_coefficient in CHROMA_COEFFICIENTS
    }
