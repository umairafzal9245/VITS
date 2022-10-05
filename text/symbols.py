""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''

from typing import FrozenSet

# _letters_ipa = ""

_pad = '_'


URDU_ALPHABETS: FrozenSet[str] = frozenset("آ أ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ؤ ﺅ ہ ۂ ۃ ھ ء ی ئ ے ۓ".split())

URDU_DIGITS: FrozenSet[str] = frozenset("۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹".split())

URDU_PUNCTUATIONS: FrozenSet[str] = frozenset("؟ ٪ ! ، ’ ‘ ' . / , - ؛ :".split())

URDU_DIACRITICS: FrozenSet[str] = frozenset("\u064e \u064B \u0670 \u0650 \u064F \u064d \u0651 \u0654 \u200c".split())

URDU_EXTRA_CHARACTERS: FrozenSet[str] = frozenset("ﷲ ﷺ  ؓ  ؑ  ؒ  ؐ  ۖ".split())

URDU_ALL_CHARACTERS: FrozenSet[str] = frozenset().union(URDU_ALPHABETS, URDU_DIGITS, URDU_PUNCTUATIONS,  # type: ignore
                                                        URDU_DIACRITICS, URDU_EXTRA_CHARACTERS)  # type: ignore
# Export all symbols:
symbols = [_pad] + list(URDU_ALL_CHARACTERS) 
symbols.append(" ")
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")
