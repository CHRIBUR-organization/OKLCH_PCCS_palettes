from constants_for_calc_chroma import ConstantsForCalcChroma

TONE_CHROMA_COEFFICIENT_DICT: dict[str, int] = {
    "p": ConstantsForCalcChroma.CHROMA_COEFFICIENT_LOW,
    "ltg": ConstantsForCalcChroma.CHROMA_COEFFICIENT_LOW,
    "g": ConstantsForCalcChroma.CHROMA_COEFFICIENT_LOW,
    "dkg": ConstantsForCalcChroma.CHROMA_COEFFICIENT_LOW,
    "lt": ConstantsForCalcChroma.CHROMA_COEFFICIENT_MEDIUM,
    "sf": ConstantsForCalcChroma.CHROMA_COEFFICIENT_MEDIUM,
    "d": ConstantsForCalcChroma.CHROMA_COEFFICIENT_MEDIUM,
    "dk": ConstantsForCalcChroma.CHROMA_COEFFICIENT_MEDIUM,
    "b": ConstantsForCalcChroma.CHROMA_COEFFICIENT_HIGH,
    "s": ConstantsForCalcChroma.CHROMA_COEFFICIENT_HIGH,
    "dp": ConstantsForCalcChroma.CHROMA_COEFFICIENT_HIGH,
}
