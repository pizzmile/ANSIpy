from .code import ANSICode, RESET

COLOR_STRINGS = {
    # 16 colors
    "FOREGROUND_16": {
        "BLACK": "\x1b[30m",
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
    },
    "BACKGROUND_16": {
        "BLACK": "\x1b[40m",
        "RED": "\x1b[41m",
        "GREEN": "\x1b[42m",
        "YELLOW": "\x1b[43m",
        "BLUE": "\x1b[44m",
        "MAGENTA": "\x1b[45m",
        "CYAN": "\x1b[46m",
        "WHITE": "\x1b[47m",
        "DEFAULT": "\x1b[49m",

        "BLACK_BRIGHT": "\x1b[40;1m",
        "RED_BRIGHT": "\x1b[41;1m",
        "GREEN_BRIGHT": "\x1b[42;1m",
        "YELLOW_BRIGHT": "\x1b[43;1m",
        "BLUE_BRIGHT": "\x1b[44;1m",
        "MAGENTA_BRIGHT": "\x1b[45;1m",
        "CYAN_BRIGHT": "\x1b[46;1m",
        "WHITE_BRIGHT": "\x1b[47;1m",

        "BLACK_AIXTERM_BRIGHT": "\x1b[100m",
        "RED_AIXTERM_BRIGHT": "\x1b[101m",
        "GREEN_AIXTERM_BRIGHT": "\x1b[102m",
        "YELLOW_AIXTERM_BRIGHT": "\x1b[103m",
        "BLUE_AIXTERM_BRIGHT": "\x1b[104m",
        "MAGENTA_AIXTERM_BRIGHT": "\x1b[105m",
        "CYAN_AIXTERM_BRIGHT": "\x1b[106m",
        "WHITE_AIXTERM_BRIGHT": "\x1b[107m",
    },

    # 256 Color
    "FOREGROUND_256": "\x1b[38;5;{code}m",
    "BACKGROUND_256": "\x1b[48;5;{code}m",

    # RGB Color
    "FOREGROUND_RGB": "\x1b[38;2;{r};{g};{b}m",
    "BACKGROUND_RGB": "\x1b[48;2;{r};{g};{b}m",
}


class ANSIColor(ANSICode):
    """
    Class to model generic ANSI codes for color
    """

    def __init__(self, code: str = None):
        """
        ANSIColor constructor

        :param str code: color code in string format
        """
        super(ANSIColor, self).__init__(code)

    def apply(self, string: str, reset_after: bool = True) -> str:
        """
        Apply the color code to a string

        :param str string: string to be enriched
        :param bool reset_after: if true add a reset code at the end
        :return: the enriched string
        :rtype: str
        """
        if reset_after:
            return super(ANSIColor, self).apply(string + RESET)
        else:
            return super(ANSIColor, self).apply(string)


class ANSIColorRGB(ANSIColor):
    """
    Class to model ANSI codes for RGB color
    """
    red: int
    green: int
    blue: int

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, background: bool = False):
        """
        ANSIColorRGB constructor

        :param int red: red channel value
        :param int green: green channel value
        :param int blue: blue channel value
        :param bool background: if true create a background color, if false a foreground color
        """
        # Use RGB direct values if they are valid
        if red < 0 or red > 255:
            raise ValueError("'r' must lies within 0 and 255 (included)")
        if green < 0 or green > 255:
            raise ValueError("'g' must lies within 0 and 255 (included)")
        if blue < 0 or blue > 255:
            raise ValueError("'b' must lies within 0 and 255 (included)")
        r, g, b = red, green, blue

        # Store values in object
        self.red = r
        self.green = g
        self.blue = b

        # Build object
        super(ANSIColorRGB, self).__init__(
            COLOR_STRINGS['BACKGROUND_RGB' if background else 'FOREGROUND_RGB'].format(r=r, g=g, b=b))

    def __str__(self):
        return self._code.format(r=self.red, g=self.green, b=self.blue)


class ANSIColorHEX(ANSIColorRGB):
    """
    Class to model ANSI codes for HEX color
    """
    red: int
    green: int
    blue: int

    def __init__(self, hex_code: str, background: bool = False):
        """
        ANSIColorHex constructor

        :param bool background: if true create a background color, if false a foreground color
        :param str hex_code: hexadecimal representation f the code (overwrites 'red', 'green', 'blue' params)
        """

        # Convert hex code into RGB values
        try:
            h = hex_code.lstrip('#')
            if not len(h) == 6:
                raise ValueError("'hex_code' in wrong format (required 'hex_code'=#6_CHAR_CODE")

            r, g, b = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        except Exception as e:
            raise (ValueError("'hex_code' in wrong format (required 'hex_code'=#6_CHAR_CODE)"))

        # Build object
        super(ANSIColorHEX, self).__init__(red=r, green=g, blue=b, background=background)


class ANSIColor256(ANSIColor):
    """
    Class to model extended ANSI codes for color
    """
    value: int

    def __init__(self, value: int, background: bool = False):
        """
        ANSIColor256 constructor

        :param int value: color id (0 to 255)
        :param bool background: if true create a background color, if false a foreground color
        """
        if value < 0 or value > 255:
            raise ValueError("'code' must lies within 0 and 255 (included)")

        self.value = value

        super(ANSIColor256, self).__init__(
            COLOR_STRINGS['BACKGROUND_256' if background else 'FOREGROUND_256'].format(code=value))

    def __str__(self):
        return self._code.format(value=self.value)


# Defaults
BLACK = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLACK'])
RED = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['RED'])
GREEN = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['GREEN'])
YELLOW = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['YELLOW'])
BLUE = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLUE'])
MAGENTA = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['MAGENTA'])
CYAN = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['CYAN'])
WHITE = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['WHITE'])
DEFAULT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['DEFAULT'])
BLACK_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLACK_BRIGHT'])
RED_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['RED_BRIGHT'])
GREEN_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['GREEN_BRIGHT'])
YELLOW_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['YELLOW_BRIGHT'])
BLUE_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLUE_BRIGHT'])
MAGENTA_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['MAGENTA_BRIGHT'])
CYAN_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['CYAN_BRIGHT'])
WHITE_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['WHITE_BRIGHT'])
BLACK_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLACK_AIXTERM_BRIGHT'])
RED_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['RED_AIXTERM_BRIGHT'])
GREEN_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['GREEN_AIXTERM_BRIGHT'])
YELLOW_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['YELLOW_AIXTERM_BRIGHT'])
BLUE_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['BLUE_AIXTERM_BRIGHT'])
MAGENTA_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['MAGENTA_AIXTERM_BRIGHT'])
CYAN_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['CYAN_AIXTERM_BRIGHT'])
WHITE_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['FOREGROUND_16']['WHITE_AIXTERM_BRIGHT'])
BLACK_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLACK'])
RED_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['RED'])
GREEN_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['GREEN'])
YELLOW_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['YELLOW'])
BLUE_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLUE'])
MAGENTA_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['MAGENTA'])
CYAN_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['CYAN'])
WHITE_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['WHITE'])
DEFAULT_BACKGROUND = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['DEFAULT'])
BLACK_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLACK_BRIGHT'])
RED_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['RED_BRIGHT'])
GREEN_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['GREEN_BRIGHT'])
YELLOW_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['YELLOW_BRIGHT'])
BLUE_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLUE_BRIGHT'])
MAGENTA_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['MAGENTA_BRIGHT'])
CYAN_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['CYAN_BRIGHT'])
WHITE_BACKGROUND_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['WHITE_BRIGHT'])
BLACK_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLACK_AIXTERM_BRIGHT'])
RED_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['RED_AIXTERM_BRIGHT'])
GREEN_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['GREEN_AIXTERM_BRIGHT'])
YELLOW_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['YELLOW_AIXTERM_BRIGHT'])
BLUE_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['BLUE_AIXTERM_BRIGHT'])
MAGENTA_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['MAGENTA_AIXTERM_BRIGHT'])
CYAN_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['CYAN_AIXTERM_BRIGHT'])
WHITE_BACKGROUND_AIXTERM_BRIGHT = ANSIColor(COLOR_STRINGS['BACKGROUND_16']['WHITE_AIXTERM_BRIGHT'])
