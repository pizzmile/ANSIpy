from .code import _ANSICode, RESET

_COLORS = {
    # 16 Color
    "BLACK": "\x1b[30m",  # Foreground
    "RED": "\x1b[31m",
    "GREEN": "\x1b[32m",
    "YELLOW": "\x1b[33m",
    "BLUE": "\x1b[34m",
    "MAGENTA": "\x1b[35m",
    "CYAN": "\x1b[36m",
    "WHITE": "\x1b[37m",
    "DEFAULT": "\x1b[39m",

    "BLACK_BRIGHT": "\x1b[30;1m",
    "RED_BRIGHT": "\x1b[31;1m",
    "GREEN_BRIGHT": "\x1b[32;1m",
    "YELLOW_BRIGHT": "\x1b[33;1m",
    "BLUE_BRIGHT": "\x1b[34;1m",
    "MAGENTA_BRIGHT": "\x1b[35;1m",
    "CYAN_BRIGHT": "\x1b[36;1m",
    "WHITE_BRIGHT": "\x1b[37;1m",

    "BLACK_AIXTERM_BRIGHT": "\x1b[90m",
    "RED_AIXTERM_BRIGHT": "\x1b[91m",
    "GREEN_AIXTERM_BRIGHT": "\x1b[92m",
    "YELLOW_AIXTERM_BRIGHT": "\x1b[93m",
    "BLUE_AIXTERM_BRIGHT": "\x1b[94m",
    "MAGENTA_AIXTERM_BRIGHT": "\x1b[95m",
    "CYAN_AIXTERM_BRIGHT": "\x1b[96m",
    "WHITE_AIXTERM_BRIGHT": "\x1b[97m",

    "BLACK_BACKGROUND": "\x1b[40m",  # Background
    "RED_BACKGROUND": "\x1b[41m",
    "GREEN_BACKGROUND": "\x1b[42m",
    "YELLOW_BACKGROUND": "\x1b[43m",
    "BLUE_BACKGROUND": "\x1b[44m",
    "MAGENTA_BACKGROUND": "\x1b[45m",
    "CYAN_BACKGROUND": "\x1b[46m",
    "WHITE_BACKGROUND": "\x1b[47m",
    "DEFAULT_BACKGROUND": "\x1b[49m",

    "BLACK_BACKGROUND_BRIGHT": "\x1b[40;1m",
    "RED_BACKGROUND_BRIGHT": "\x1b[41;1m",
    "GREEN_BACKGROUND_BRIGHT": "\x1b[42;1m",
    "YELLOW_BACKGROUND_BRIGHT": "\x1b[43;1m",
    "BLUE_BACKGROUND_BRIGHT": "\x1b[44;1m",
    "MAGENTA_BACKGROUND_BRIGHT": "\x1b[45;1m",
    "CYAN_BACKGROUND_BRIGHT": "\x1b[46;1m",
    "WHITE_BACKGROUND_BRIGHT": "\x1b[47;1m",

    "BLACK_BACKGROUND_AIXTERM_BRIGHT": "\x1b[100m",
    "RED_BACKGROUND_AIXTERM_BRIGHT": "\x1b[101m",
    "GREEN_BACKGROUND_AIXTERM_BRIGHT": "\x1b[102m",
    "YELLOW_BACKGROUND_AIXTERM_BRIGHT": "\x1b[103m",
    "BLUE_BACKGROUND_AIXTERM_BRIGHT": "\x1b[104m",
    "MAGENTA_BACKGROUND_AIXTERM_BRIGHT": "\x1b[105m",
    "CYAN_BACKGROUND_AIXTERM_BRIGHT": "\x1b[106m",
    "WHITE_BACKGROUND_AIXTERM_BRIGHT": "\x1b[107m",

    # 256 Color
    "FOREGROUND_256": "\x1b[38;5;{code}m",
    "BACKGROUND_256": "\x1b[48;5;{code}m",

    # RGB Color
    "FOREGROUND_RGB": "\x1b[38;2;{r};{g};{b}m",
    "BACKGROUND_RGB": "\x1b[48;2;{r};{g};{b}m",
}


class _ANSIColor(_ANSICode):

    def __init__(self, code: str):
        super(_ANSIColor, self).__init__(code)

    def apply(self, string: str, reset_after: bool = True) -> str:
        if reset_after:
            return super(_ANSIColor, self).apply(string + RESET)
        else:
            return super(_ANSIColor, self).apply(string)


class ANSIColorRGB(_ANSIColor):
    red: int
    green: int
    blue: int

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, background: bool = False, hex_code: str = None):
        # Use RGB direct values if they are valid
        if red < 0 or red > 255:
            raise ValueError("'r' must lies within 0 and 255 (included)")
        if green < 0 or green > 255:
            raise ValueError("'g' must lies within 0 and 255 (included)")
        if blue < 0 or blue > 255:
            raise ValueError("'b' must lies within 0 and 255 (included)")
        r, g, b = red, green, blue

        # Use hex_code if it is given and valid
        if hex_code is not None:
            try:
                h = hex_code.lstrip('#')
                r, g, b = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            except Exception as e:
                print(e)
                raise (ValueError("'hex_code' in wrong format (required 'hex_code'=#CODE)"))

        # Store values in object
        self.red = r
        self.green = g
        self.blue = b

        # Build object
        super(ANSIColorRGB, self).__init__(_COLORS['BACKGROUND_RGB' if background else 'FOREGROUND_RGB'].format(r=r, g=g, b=b))

    def __str__(self):
        return self._code.format(r=self.red, g=self.green, b=self.blue)


class ANSIColor256(_ANSIColor):
    value: int

    def __init__(self, value: int, background: bool = False):
        if value < 0 or value > 255:
            raise ValueError("'code' must lies within 0 and 255 (included)")

        self.value = value

        super(ANSIColor256, self).__init__(_COLORS['BACKGROUND_256' if background else 'FOREGROUND_256'].format(code=value))

    def __str__(self):
        return self._code.format(value=self.value)


BLACK = _ANSIColor(_COLORS['BLACK'])
RED = _ANSIColor(_COLORS['RED'])
GREEN = _ANSIColor(_COLORS['GREEN'])
YELLOW = _ANSIColor(_COLORS['YELLOW'])
BLUE = _ANSIColor(_COLORS['BLUE'])
MAGENTA = _ANSIColor(_COLORS['MAGENTA'])
CYAN = _ANSIColor(_COLORS['CYAN'])
WHITE = _ANSIColor(_COLORS['WHITE'])
DEFAULT = _ANSIColor(_COLORS['DEFAULT'])
BLACK_BRIGHT = _ANSIColor(_COLORS['BLACK_BRIGHT'])
RED_BRIGHT = _ANSIColor(_COLORS['RED_BRIGHT'])
GREEN_BRIGHT = _ANSIColor(_COLORS['GREEN_BRIGHT'])
YELLOW_BRIGHT = _ANSIColor(_COLORS['YELLOW_BRIGHT'])
BLUE_BRIGHT = _ANSIColor(_COLORS['BLUE_BRIGHT'])
MAGENTA_BRIGHT = _ANSIColor(_COLORS['MAGENTA_BRIGHT'])
CYAN_BRIGHT = _ANSIColor(_COLORS['CYAN_BRIGHT'])
WHITE_BRIGHT = _ANSIColor(_COLORS['WHITE_BRIGHT'])
BLACK_AIXTERM_BRIGHT = _ANSIColor(_COLORS['BLACK_AIXTERM_BRIGHT'])
RED_AIXTERM_BRIGHT = _ANSIColor(_COLORS['RED_AIXTERM_BRIGHT'])
GREEN_AIXTERM_BRIGHT = _ANSIColor(_COLORS['GREEN_AIXTERM_BRIGHT'])
YELLOW_AIXTERM_BRIGHT = _ANSIColor(_COLORS['YELLOW_AIXTERM_BRIGHT'])
BLUE_AIXTERM_BRIGHT = _ANSIColor(_COLORS['BLUE_AIXTERM_BRIGHT'])
MAGENTA_AIXTERM_BRIGHT = _ANSIColor(_COLORS['MAGENTA_AIXTERM_BRIGHT'])
CYAN_AIXTERM_BRIGHT = _ANSIColor(_COLORS['CYAN_AIXTERM_BRIGHT'])
WHITE_AIXTERM_BRIGHT = _ANSIColor(_COLORS['WHITE_AIXTERM_BRIGHT'])
BLACK_BACKGROUND = _ANSIColor(_COLORS['BLACK_BACKGROUND'])
RED_BACKGROUND = _ANSIColor(_COLORS['RED_BACKGROUND'])
GREEN_BACKGROUND = _ANSIColor(_COLORS['GREEN_BACKGROUND'])
YELLOW_BACKGROUND = _ANSIColor(_COLORS['YELLOW_BACKGROUND'])
BLUE_BACKGROUND = _ANSIColor(_COLORS['BLUE_BACKGROUND'])
MAGENTA_BACKGROUND = _ANSIColor(_COLORS['MAGENTA_BACKGROUND'])
CYAN_BACKGROUND = _ANSIColor(_COLORS['CYAN_BACKGROUND'])
WHITE_BACKGROUND = _ANSIColor(_COLORS['WHITE_BACKGROUND'])
DEFAULT_BACKGROUND = _ANSIColor(_COLORS['DEFAULT_BACKGROUND'])
BLACK_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['BLACK_BACKGROUND_BRIGHT'])
RED_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['RED_BACKGROUND_BRIGHT'])
GREEN_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['GREEN_BACKGROUND_BRIGHT'])
YELLOW_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['YELLOW_BACKGROUND_BRIGHT'])
BLUE_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['BLUE_BACKGROUND_BRIGHT'])
MAGENTA_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['MAGENTA_BACKGROUND_BRIGHT'])
CYAN_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['CYAN_BACKGROUND_BRIGHT'])
WHITE_BACKGROUND_BRIGHT = _ANSIColor(_COLORS['WHITE_BACKGROUND_BRIGHT'])
BLACK_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['BLACK_BACKGROUND_AIXTERM_BRIGHT'])
RED_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['RED_BACKGROUND_AIXTERM_BRIGHT'])
GREEN_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['GREEN_BACKGROUND_AIXTERM_BRIGHT'])
YELLOW_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['YELLOW_BACKGROUND_AIXTERM_BRIGHT'])
BLUE_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['BLUE_BACKGROUND_AIXTERM_BRIGHT'])
MAGENTA_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['MAGENTA_BACKGROUND_AIXTERM_BRIGHT'])
CYAN_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['CYAN_BACKGROUND_AIXTERM_BRIGHT'])
WHITE_BACKGROUND_AIXTERM_BRIGHT = _ANSIColor(_COLORS['WHITE_BACKGROUND_AIXTERM_BRIGHT'])
