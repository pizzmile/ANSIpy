from .code import *
from .style import ANSIStyle


class ANSIString(str):
    """
    Class to model string type that implement specific method to add ANSI style codes
    """

    def color_16bit(self, name: str, background: bool = False):
        """
        Colorize the string from standard color code

        :param bool background: if true change the background color, if false change the foreground
        :param str name: name of the 16bit color
        :return: the colored string
        :rtype: ANSIString
        """
        try:
            if not background:
                color_code = ANSIColor(COLOR_STRINGS['FOREGROUND_16'][name])
            else:
                color_code = ANSIColor(COLOR_STRINGS['BACKGROUND_16'][name])
            return ANSIString(color_code.apply(self))
        except KeyError as e:
            raise ValueError(f"Unknown color name '{name}'")

    def color_rgb(self, red: int, green: int, blue: int, background: bool = False):
        """
        Colorize the string from RGB code

        :param bool background: if true change the background color, if false change the foreground
        :param int red: red channel value
        :param int green: green channel value
        :param int blue: blue channel value
        :return: the colored string
        :rtype: ANSIString
        """
        color_code = ANSIColorRGB(red=red, green=green, blue=blue, background=background)
        return ANSIString(color_code.apply(self))

    def color_hex(self, hex_code: str, background: bool = False):
        """
        Colorize the string from HEX code

        :param str hex_code: hexadecimal color code
        :param bool background: if true change the background color, if false change the foreground
        :return: the colored string
        :rtype: ANSIString
        """
        color_code = ANSIColorHEX(hex_code=hex_code, background=background)
        return ANSIString(color_code.apply(self))

    def color_256bit(self, value: int, background: bool = False):
        """
        Colorize the string from extended color code

        :param bool background: if true change the background color, if false change the foreground
        :param int value: the integer value corresponding to the color in extended 256 colors ANSI encoding
        :return: the colored string
        :rtype: ANSIString
        """
        color_code = ANSIColor256(value=value, background=background)
        return ANSIString(color_code.apply(self))

    def apply_style(self, style: ANSIStyle):
        """
        Apply a style to the string

        :param style: the style to apply
        :type style: ANSIStyle
        :return: the styled string
        :rtype: ANSIString
        """
        return ANSIString(style.apply(self))
