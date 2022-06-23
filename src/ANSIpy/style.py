from .code import ANSIColor, ANSIColorRGB, ANSIColor256, ANSIEffect
from .code import UNDERLINE, BOLD, FAINT, INVERSE, BLINKING, ITALIC, RESET, HIDDEN, STRIKETHROUGH
from .code import COLOR_STRINGS


class ANSIStyle:
    """
    Class to model a collection of ANSI codes that define a custom style
    """
    __options: dict = {
        "foreground_color": None,
        "background_color": None,
        "foreground_256": None,
        "background_256": None,
        "foreground_hex": None,
        "background_hex": None,
        "foreground_rgb": None,
        "background_rgb": None,
        "underline": False,
        "bold": False,
        "faint": False,
        "inverse": False,
        "blinking": False,
        "italic": False,
        "hidden": False,
        "strikethrough": False,
        "reset_before": True,
        "reset_after": True
    }

    __foreground_color: ANSIColor
    __background_color: ANSIColor
    __underline: bool
    __bold: bool
    __faint: bool
    __inverse: bool
    __blinking: bool
    __italic: bool
    __hidden: bool
    __strikethrough: bool
    __reset_before: bool
    __reset_after: bool

    def __init__(self, **kwargs):
        """
        ANSIStyle constructor

        :param kwargs: optional arguments to encode the color and the effects of 'string'
        :keyword str foreground_color: name of the color to be applied as foreground
        :keyword str background_color: name of the color to be applied as background
        :keyword str foreground_hex: hexadecimal code of the color to be applied as foreground (overwrite name colors)
        :keyword str background_hex: hexadecimal code of the color to be applied as background (overwrite name colors)
        :keyword tuple[int] foreground_rgb: tuple containing (r, g, b) values for the color to be applied as foreground (overwrite hex
        and name colors)
        :keyword tuple[int] background_rgb: tuple containing (r, g, b) values for the color to be applied as background (overwrite hex
        and name colors)
        :keyword bool underline: if true add underline effect
        :keyword bool bold: if true add bold effect
        :keyword bool faint: if true add faint effect
        :keyword bool inverse: if true add reverse effect
        :keyword bool blinking: if true add blink effect
        :keyword bool italic: if true add italic effect
        :keyword bool reset_before: if true add a reset code at the beginning
        :keyword bool reset_after: if true add a reset code at the end
        """
        self.__options.update(kwargs)

    def __str__(self):
        foreground_color = ""
        if self.__options['foreground_color'] is not None:
            foreground_color = COLOR_STRINGS['FOREGROUND_16'][self.__options["foreground_color"]]
        if self.__options['foreground_256'] is not None:
            foreground_color = ANSIColor256(value=self.__options['foreground_256'])
        if self.__options['foreground_hex'] is not None:
            foreground_color = ANSIColorRGB(hex_code=self.__options["foreground_color"])
        if self.__options['foreground_rgb'] is not None:
            foreground_color = ANSIColorRGB(red=tuple(self.__options["foreground_color"])[0],
                                            green=tuple(self.__options["foreground_color"])[1],
                                            blue=tuple(self.__options["foreground_color"])[2])
        output_string = foreground_color

        background_color = ""
        if self.__options['background_color'] is not None:
            background_color = COLOR_STRINGS['BACKGROUND_16'][self.__options["background_color"]]
        if self.__options['background_256'] is not None:
            background_color = ANSIColor256(value=self.__options['background_256'], background=True)
        if self.__options['background_hex'] is not None:
            background_color = ANSIColorRGB(hex_code=self.__options["background_color"], background=True)
        if self.__options['background_rgb'] is not None:
            background_color = ANSIColorRGB(red=tuple(self.__options["background_color"])[0],
                                            green=tuple(self.__options["background_color"])[1],
                                            blue=tuple(self.__options["background_color"])[2],
                                            background=True)
        output_string += background_color

        if self.__options['bold']:
            output_string = BOLD + output_string
        if self.__options['inverse']:
            output_string = INVERSE + output_string
        if self.__options['faint']:
            output_string = FAINT + output_string
        if self.__options['blinking']:
            output_string = BLINKING + output_string
        if self.__options['underline']:
            output_string = UNDERLINE + output_string
        if self.__options['italic']:
            output_string = ITALIC + output_string
        if self.__options['reset_before']:
            output_string = RESET + output_string
        output_string += "{string}"
        if self.__options['reset_after']:
            output_string = output_string + RESET

        return str(output_string)

    def __add__(self, other):
        return self + other

    def __radd__(self, other):
        return other + self

    def __dict__(self):
        return self.__options

    def apply(self, string):
        """
        Apply the style to 'string'

        :param str string: string to enrich
        :return: the enriched string
        :rtype: str
        """
        return self.__str__().format(string=string)

    def set_foreground_color(self, value: ANSIColor) -> None:
        """
        Set foreground_color property

        :param value: value to be set for the property
        :type value: ANSIColor
        :return:
        :rtype: None
        """
        self.__options['foreground_color'] = value
        self.__foreground_color = value

    def set_background_color(self, value: ANSIColor) -> None:
        """
        Set background_color property

        :param value: value to be set for the property
        :type value: ANSIColor
        :return:
        :rtype: None
        """
        self.__options['background_color'] = value
        self.__background_color = value

    def set_underline(self, value: bool) -> None:
        """
        Set underline property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['underline'] = value
        self.__underline = value

    def set_bold(self, value: bool) -> None:
        """
        Set bold property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['bold'] = value
        self.__bold = value

    def set_faint(self, value: bool) -> None:
        """
        Set faint property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['faint'] = value
        self.__faint = value

    def set_inverse(self, value: bool) -> None:
        """
        Set inverse property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['inverse'] = value
        self.__inverse = value

    def set_blinking(self, value: bool) -> None:
        """
        Set blinking property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['blinking'] = value
        self.__blinking = value

    def set_italic(self, value: bool) -> None:
        """
        Set italic property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['italic'] = value
        self.__italic = value

    def set_hidden(self, value: bool) -> None:
        """
        Set hidden property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['hidden'] = value
        self.__hidden = value

    def set_strikethrough(self, value: bool) -> None:
        """
        Set strikethrough property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['strikethrough'] = value
        self.__strikethrough = value

    def set_reset_before(self, value: bool) -> None:
        """
        Set reset_before property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['reset_before'] = value
        self.__reset_before = value

    def set_reset_after(self, value: bool) -> None:
        """
        Set reset_after property

        :param bool value: value to be set for the property
        :return:
        :rtype: None
        """
        self.__options['reset_after'] = value
        self.__reset_after = value

    def get_foreground_color(self) -> ANSIColor:
        """
        Get the value of the property foreground_color

        :return: foreground_color attribute
        :rtype: ANSIColor
        """
        return self.__foreground_color

    def get_background_color(self) -> ANSIColor:
        """
        Get the value of the property background_color

        :return: background_color attribute
        :rtype: ANSIColor
        """
        return self.__background_color

    def get_underline(self) -> bool:
        """
        Get the value of the property underline

        :return: underline attribute
        :rtype: bool
        """
        return self.__underline

    def get_bold(self) -> bool:
        """
        Get the value of the property bold

        :return: f attribute
        :rtype: bool
        """
        return self.__bold

    def get_faint(self) -> bool:
        """
        Get the value of the property faint

        :return: faint attribute
        :rtype: bool
        """
        return self.__faint

    def get_inverse(self) -> bool:
        """
        Get the value of the property inverse

        :return: inverse attribute
        :rtype: bool
        """
        return self.__inverse

    def get_blinking(self) -> bool:
        """
        Get the value of the property blinking

        :return: blinking attribute
        :rtype: bool
        """
        return self.__blinking

    def get_italic(self) -> bool:
        """
        Get the value of the property italic

        :return: italic attribute
        :rtype: bool
        """
        return self.__italic

    def get_hidden(self) -> bool:
        """
        Get the value of the property hidden

        :return: hidden attribute
        :rtype: bool
        """
        return self.__hidden

    def get_strikethrough(self) -> bool:
        """
        Get the value of the property strikethrough

        :return: strikethrough attribute
        :rtype: bool
        """
        return self.__strikethrough

    def get_reset_before(self) -> bool:
        """
        Get the value of the property reset_before

        :return: reset_before attribute
        :rtype: bool
        """
        return self.__reset_before

    def get_reset_after(self) -> bool:
        """
        Get the value of the property reset_after

        :return: reset_after attribute
        :rtype: bool
        """
        return self.__reset_after
