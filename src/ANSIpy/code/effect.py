from .code import _ANSICode


_EFFECTS = {
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


class _ANSIEffect(_ANSICode):
    reset: str

    def __init__(self, code: str, reset: str):
        super(_ANSIEffect, self).__init__(code)
        self.reset = reset

    def apply(self, string: str, reset_after: bool = True) -> str:
        if reset_after:
            return super(_ANSIEffect, self).apply(string + self.reset)
        else:
            return super(_ANSIEffect, self).apply(string)


# Effect
BOLD = _ANSIEffect(code=_EFFECTS['BOLD'], reset=_EFFECTS['BOLD_RESET'])
FAINT = _ANSIEffect(code=_EFFECTS['FAINT'], reset=_EFFECTS['FAINT_RESET'])
ITALIC = _ANSIEffect(code=_EFFECTS['ITALIC'], reset=_EFFECTS['ITALIC_RESET'])
UNDERLINE = _ANSIEffect(code=_EFFECTS['UNDERLINE'], reset=_EFFECTS['UNDERLINE_RESET'])
BLINKING = _ANSIEffect(code=_EFFECTS['BLINKING'], reset=_EFFECTS['BLINKING_RESET'])
INVERSE = _ANSIEffect(code=_EFFECTS['INVERSE'], reset=_EFFECTS['INVERSE_RESET'])
HIDDEN = _ANSIEffect(code=_EFFECTS['HIDDEN'], reset=_EFFECTS['HIDDEN_RESET'])
STRIKETHROUGH = _ANSIEffect(code=_EFFECTS['STRIKETHROUGH'], reset=_EFFECTS['STRIKETHROUGH_RESET'])
