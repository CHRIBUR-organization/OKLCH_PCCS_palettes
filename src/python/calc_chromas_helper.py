def calc_chromas_helper(chroma: float, coefficient: int, denominator: int = 9) -> float:
    """_summary_

    Parameters
    ----------
    chroma : float
        _description_
    coefficient : int
        _description_
    denominator : int, optional
        _description_, by default 9

    Returns
    -------
    float
        _description_

    """
    return chroma * coefficient / denominator
