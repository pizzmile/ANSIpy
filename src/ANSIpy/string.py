from .code import *
from .style import ANSIStyle


class ANSIString(str):
    """
    Class to model string type that implement specific method to add ANSI style codes
    """

    def fg_color_16bit(self, name: str):
        """
        Colorize the foreground of the string
        :param name: name of the 16bit color
        :return: the colored string
        """
        color_code = ANSIColor(COLOR_STRINGS['FOREGROUND_16'][name])
        return ANSIString(color_code.apply(self))

    def fg_color_rgb(self, red: int, green: int, blue: int):
        """
        Colorize the foreground of the string
        :param red: red channel value
        :param green: green channel value
        :param blue: blue channel value
        :return: the colored string
        """
        color_code = ANSIColorRGB(red=red, green=green, blue=blue)
        return ANSIString(color_code.apply(self))

    def fg_color_hex(self, hex_code: str):
        """
        Colorize the foreground of the string
        :param hex_code: hexadecimal color code
        :return: the colored string
        """
        color_code = ANSIColorRGB(hex_code=hex_code)
        return ANSIString(color_code.apply(self))

    def bg_color_16bit(self, name: str):
        """
        Colorize the background of the string
        :param name: name of the 16bit color
        :return: the colored string
        """
        color_code = ANSIColor(COLOR_STRINGS['BACKGROUND_16'][name])
        return ANSIString(color_code.apply(self))

    def bg_color_rgb(self, red: int, green: int, blue: int):
        """
        Colorize the background of the string
        :param red: red channel value
        :param green: green channel value
        :param blue: blue channel value
        :return: the colored string
        """
        color_code = ANSIColorRGB(red=red, green=green, blue=blue, background=True)
        return ANSIString(color_code.apply(self))

    def bg_color_hex(self, hex_code: str):
        """
        Colorize the background of the string
        :param hex_code: hexadecimal color code
        :return: the colored string
        """
        color_code = ANSIColorRGB(hex_code=hex_code, background=True)
        return ANSIString(color_code.apply(self))

    def stylize(self, style: ANSIStyle):
        return ANSIString(style.apply(self))
