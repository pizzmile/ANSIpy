import sys

from .code import ANSIColor, BOLD, UNDERLINE, ITALIC, INVERSE, FAINT, BLINKING, RESET, HIDDEN, STRIKETHROUGH
from .style import ANSIStyle


def ansiprint(string: str, **kwargs) -> None:
    """
    Print a string with the specified ANSI codes

    :param str string: string to print
    :param kwargs: optional arguments to encode the color and the effects of 'string'
    :keyword foreground_color: name of the color to be applied as foreground
    :keyword background_color: name of the color to be applied as background
    :keyword foreground_hex: hexadecimal code of the color to be applied as foreground (overwrite name colors)
    :keyword background_hex: hexadecimal code of the color to be applied as background (overwrite name colors)
    :keyword foreground_rgb: tuple containing (r, g, b) values for the color to be applied as foreground (overwrite hex
    and name colors)
    :keyword background_rgb: tuple containing (r, g, b) values for the color to be applied as background (overwrite hex
    and name colors)
    :keyword underline: if true add underline effect
    :keyword bold: if true add bold effect
    :keyword faint: if true add faint effect
    :keyword inverse: if true add reverse effect
    :keyword blinking: if true add blink effect
    :keyword italic: if true add italic effect
    :keyword reset_before: if true add a reset code at the beginning
    :keyword reset_after: if true add a reset code at the end
    :return:
    :rtype: None
    """
    tmp_style = ANSIStyle(**kwargs)
    sys.stdout.write(tmp_style.apply(string))

