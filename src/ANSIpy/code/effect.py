from .code import ANSICode


EFFECT_STRINGS = {
    "BOLD": "\x1b[1m",
    "FAINT": "\x1b[2m",
    "ITALIC": "\x1b[3m",
    "UNDERLINE": "\x1b[4m",
    "BLINKING": "\x1b[5m",
    "INVERSE": "\x1b[7m",
    "HIDDEN": "\x1b[8m",
    "STRIKETHROUGH": "\x1b[9m",
    "BOLD_RESET": "\x1b[22m",
    "FAINT_RESET": "\x1b[22m",
    "ITALIC_RESET": "\x1b[23m",
    "UNDERLINE_RESET": "\x1b[24m",
    "BLINKING_RESET": "\x1b[25m",
    "INVERSE_RESET": "\x1b[27m",
    "HIDDEN_RESET": "\x1b[28m",
    "STRIKETHROUGH_RESET": "\x1b[29m",
}


class ANSIEffect(ANSICode):
    """
    Class to model ANSI codes for effects
    """
    reset: str

    def __init__(self, code: str, reset: str):
        """
        ANSIEffect constructor

        :param str code: the string format of the ANSI code
        :param str reset: the string format of the ANSI specific reset code
        """
        super(ANSIEffect, self).__init__(code)
        self.reset = reset

    def apply(self, string: str, reset_after: bool = True) -> str:
        """
        Apply the effect code to a string

        :param str string: string to be enriched
        :param bool reset_after: if true add a reset code at the end
        :return: the enriched string
        :rtype: str
        """
        if reset_after:
            return super(ANSIEffect, self).apply(string + self.reset)
        else:
            return super(ANSIEffect, self).apply(string)


# Defaults
BOLD = ANSIEffect(code=EFFECT_STRINGS['BOLD'], reset=EFFECT_STRINGS['BOLD_RESET'])
FAINT = ANSIEffect(code=EFFECT_STRINGS['FAINT'], reset=EFFECT_STRINGS['FAINT_RESET'])
ITALIC = ANSIEffect(code=EFFECT_STRINGS['ITALIC'], reset=EFFECT_STRINGS['ITALIC_RESET'])
UNDERLINE = ANSIEffect(code=EFFECT_STRINGS['UNDERLINE'], reset=EFFECT_STRINGS['UNDERLINE_RESET'])
BLINKING = ANSIEffect(code=EFFECT_STRINGS['BLINKING'], reset=EFFECT_STRINGS['BLINKING_RESET'])
INVERSE = ANSIEffect(code=EFFECT_STRINGS['INVERSE'], reset=EFFECT_STRINGS['INVERSE_RESET'])
HIDDEN = ANSIEffect(code=EFFECT_STRINGS['HIDDEN'], reset=EFFECT_STRINGS['HIDDEN_RESET'])
STRIKETHROUGH = ANSIEffect(code=EFFECT_STRINGS['STRIKETHROUGH'], reset=EFFECT_STRINGS['STRIKETHROUGH_RESET'])
