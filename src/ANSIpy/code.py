import platform


class ANSICode(str):

    def apply(self, string: str, reset_after: bool = False):
        """
        Apply the code to a string
        :param string: the string to be enriched
        :param reset_after: if true add a terminal reset code to limit the code effect to the given string
        :return: the enriched string
        """
        if not reset_after:
            return self + string
        else:
            return self + string + "\x1b[0m"

    @staticmethod
    def build(code: int, *kwargs):
        pass

    @staticmethod
    def color16bit(code: int, bright: bool = False, background: bool = False):
        """
        Build a regular AnsiCode color string given.
        :param code: color code (0 to 7)
        :param bright: if true build a bright color code
        :param background: if true build a background color code, else a foreground color code
        :return: the AnsiCode string
        """
        if 0 <= code <= 8:
            if not background:
                return ANSICode(f"\x1b[3{code}{';1' if bright else ''}m")
            else:
                return ANSICode(f"\x1b[4{code}{';1' if bright else ''}m")

        else:
            raise ValueError('"code" must be comprised in [0; 7] interval')

    @staticmethod
    def color256bit(code: int, background: bool = False):
        """
        Build an extended AnsiCode color string given.
        :param code: color code (0 to 255)
        :param background: if true build a background color code, else a foreground color code
        :return: the AnsiCode string
        """
        if 0 <= code <= 255:
            if not background:
                return ANSICode(f"\x1b[38;5;{code}m")
            else:
                return ANSICode(f"\x1b[48;5;{code}m")
        else:
            raise ValueError('"code" must be comprised in [0; 255] interval')

    # EFFECTS
    @staticmethod
    def reset():
        """
        Default code builder
        :return: reset color code
        """
        return ANSICode("\x1b[0m")

    @staticmethod
    def bold():
        """
        Default code builder
        :return: bold color code
        """
        return ANSICode("\x1b[1m")

    @staticmethod
    def underline():
        """
        Default code builder
        :return: underline color code
        """
        return ANSICode("\x1b[4m")

    @staticmethod
    def reverse():
        """
        Default code builder
        :return: reverse color code
        """
        return ANSICode("\x1b[7m")

    # FOREGROUND COLORS
    @staticmethod
    def black():
        """
        Default code builder
        :return: black color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[30m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[30m")

    @staticmethod
    def red():
        """
        Default code builder
        :return: red color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[31m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[31m")

    @staticmethod
    def green():
        """
        Default code builder
        :return: green color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[32m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[32m")

    @staticmethod
    def yellow():
        """
        Default code builder
        :return: yellow color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[33m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[33m")

    @staticmethod
    def blue():
        """
        Default code builder
        :return: blue color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[34m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[34m")

    @staticmethod
    def magenta():
        """
        Default code builder
        :return: magenta color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[35m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[35m")

    @staticmethod
    def cyan():
        """
        Default code builder
        :return: cyan color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[36m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[36m")

    @staticmethod
    def white():
        """
        Default code builder
        :return: white color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[37m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[37m")

    @staticmethod
    def bright_black():
        """
        Default code builder
        :return: bright black color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;8m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[30;1m")

    @staticmethod
    def bright_red():
        """
        Default code builder
        :return: bright red color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;9m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[31;1m")

    @staticmethod
    def bright_green():
        """
        Default code builder
        :return: bright green color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;10m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[32;1m")

    @staticmethod
    def bright_yellow():
        """
        Default code builder
        :return: bright yellow color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;11m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[33;1m")

    @staticmethod
    def bright_blue():
        """
        Default code builder
        :return: bright blue color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;12m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[34;1m")

    @staticmethod
    def bright_magenta():
        """
        Default code builder
        :return: bright magenta color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;13m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[35;1m")

    @staticmethod
    def bright_cyan():
        """
        Default code builder
        :return: bright cyan color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;14m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[36;1m")

    @staticmethod
    def bright_white():
        """
        Default code builder
        :return: bright white color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[38;5;15m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[37;1m")

    @staticmethod
    def black_background():
        """
        Default code builder
        :return: black background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[40m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[40m")

    @staticmethod
    def red_background():
        """
        Default code builder
        :return: red background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[41m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[41m")

    @staticmethod
    def green_background():
        """
        Default code builder
        :return: green background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[42m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[42m")

    @staticmethod
    def yellow_background():
        """
        Default code builder
        :return: yellow background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[43m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[43m")

    @staticmethod
    def blue_background():
        """
        Default code builder
        :return: blue background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[44m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[44m")

    @staticmethod
    def magenta_background():
        """
        Default code builder
        :return: magenta background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[45m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[45m")

    @staticmethod
    def cyan_background():
        """
        Default code builder
        :return: cyan background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[46m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[46m")

    @staticmethod
    def white_background():
        """
        Default code builder
        :return: white background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[47m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[47m")

    @staticmethod
    def bright_black_background():
        """
        Default code build
        :return: bright black background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;8m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[40;1m")

    @staticmethod
    def bright_red_background():
        """
        Default code build
        :return: bright red background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;9m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[41;1m")

    @staticmethod
    def bright_green_background():
        """
        Default code builder
        :return: bright green background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;10m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[42;1m")

    @staticmethod
    def bright_yellow_background():
        """
        Default code builder
        :return: bright yellow background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;11m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[43;1m")

    @staticmethod
    def bright_blue_background():
        """
        Default code builder
        :return: bright blue background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;12m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[44;1m")

    @staticmethod
    def bright_magenta_background():
        """
        Default code builder
        :return: bright magenta background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;13m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[45;1m")

    @staticmethod
    def bright_cyan_background():
        """
        Default code builder
        :return: bright cyan background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;14m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[46;1m")

    @staticmethod
    def bright_white_background():
        """
        Default code builder
        :return: bright white background color code
        """
        if platform.system() == 'Darwin':
            return ANSICode("\x1b[48;5;15m")
        # elif platform.system() == 'Windows':
        #     return AnsiCode("30")
        # elif platform.system() == 'Linux':
        #     return AnsiCode("30")
        else:
            return ANSICode("\x1b[47;1m")


# DEFAULT CODES
RESET = ANSICode.reset()
BOLD = ANSICode.bold()
UNDERLINE = ANSICode.underline()
REVERSE = ANSICode.reverse()
BLACK = ANSICode.black()
RED = ANSICode.red()
GREEN = ANSICode.green()
YELLOW = ANSICode.yellow()
BLUE = ANSICode.blue()
MAGENTA = ANSICode.magenta()
CYAN = ANSICode.cyan()
WHITE = ANSICode.white()
BRIGHT_BLACK = ANSICode.bright_black()
BRIGHT_RED = ANSICode.bright_red()
BRIGHT_GREEN = ANSICode.bright_green()
BRIGHT_YELLOW = ANSICode.bright_yellow()
BRIGHT_BLUE = ANSICode.bright_blue()
BRIGHT_MAGENTA = ANSICode.bright_magenta()
BRIGHT_CYAN = ANSICode.bright_cyan()
BRIGHT_WHITE = ANSICode.bright_white()
BLACK_BACKGROUND = ANSICode.black_background()
RED_BACKGROUND = ANSICode.red_background()
GREEN_BACKGROUND = ANSICode.green_background()
YELLOW_BACKGROUND = ANSICode.yellow_background()
BLUE_BACKGROUND = ANSICode.blue_background()
MAGENTA_BACKGROUND = ANSICode.magenta_background()
CYAN_BACKGROUND = ANSICode.cyan_background()
WHITE_BACKGROUND = ANSICode.white_background()
BRIGHT_BLACK_BACKGROUND = ANSICode.bright_black_background()
BRIGHT_RED_BACKGROUND = ANSICode.bright_red_background()
BRIGHT_GREEN_BACKGROUND = ANSICode.bright_green_background()
BRIGHT_YELLOW_BACKGROUND = ANSICode.bright_yellow_background()
BRIGHT_BLUE_BACKGROUND = ANSICode.bright_blue_background()
BRIGHT_MAGENTA_BACKGROUND = ANSICode.bright_magenta_background()
BRIGHT_CYAN_BACKGROUND = ANSICode.bright_cyan_background()
BRIGHT_WHITE_BACKGROUND = ANSICode.bright_white_background()

EFFECTS = {
    "RESET": RESET,
    "BOLD": BOLD,
    "UNDERLINE": UNDERLINE,
    "REVERSE": REVERSE,
}

FOREGROUND_COLORS = {
    "black": BLACK,
    "red": RED,
    "green": GREEN,
    "yellow": YELLOW,
    "blue": BLUE,
    "magenta": MAGENTA,
    "cyan": CYAN,
    "white": WHITE,
    "bright_black": BRIGHT_BLACK,
    "bright_red": BRIGHT_RED,
    "bright_green": BRIGHT_GREEN,
    "bright_yellow": BRIGHT_YELLOW,
    "bright_blue": BRIGHT_BLUE,
    "bright_magenta": BRIGHT_MAGENTA,
    "bright_cyan": BRIGHT_CYAN,
    "bright_white": BRIGHT_WHITE,
}

BACKGROUND_COLORS = {
    "black": BLACK_BACKGROUND,
    "red": RED_BACKGROUND,
    "green": GREEN_BACKGROUND,
    "yellow": YELLOW_BACKGROUND,
    "blue": BLUE_BACKGROUND,
    "magenta": MAGENTA_BACKGROUND,
    "cyan": CYAN_BACKGROUND,
    "white": WHITE_BACKGROUND,
    "bright_black": BRIGHT_BLACK_BACKGROUND,
    "bright_red": BRIGHT_RED_BACKGROUND,
    "bright_green": BRIGHT_GREEN_BACKGROUND,
    "bright_yellow": BRIGHT_YELLOW_BACKGROUND,
    "bright_blue": BRIGHT_BLUE_BACKGROUND,
    "bright_magenta": BRIGHT_MAGENTA_BACKGROUND,
    "bright_cyan": BRIGHT_CYAN_BACKGROUND,
    "bright_white": BRIGHT_WHITE_BACKGROUND,
}