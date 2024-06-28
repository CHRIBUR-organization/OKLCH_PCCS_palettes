def calc_lightnesses_helper(
    low: float, coefficient_low: int, high: float, coefficient_high: int
) -> float:
    """_summary_

    Parameters
    ----------
    low : float
        _description_
    coefficient_low : int
        _description_
    high : float
        _description_
    coefficient_high : int
        _description_

    Returns
    -------
    float
        _description_

    """
    return sum(sorted([low * coefficient_low, high * coefficient_high])) / (
        coefficient_low + coefficient_high
    )
