# TODO: consider adding class for strings
# from .code import ANSICode
# from .style import SUCCESS, WARNING, ERROR
#
#
# class ANSIString(str):
#     def enrich(self, code: ANSICode, reset_after: bool = True):
#         """
#         Enrich ANSIString with an ANSICode
#         :param code: the code to be applied
#         :param reset_after: if true end the enriched string with a reset code
#         :return: the enriched ANSIString
#         """
#         return ANSIString(code + self + ANSICode.reset())
#
#     # STYLES
#     def success(self):
#         """
#         Apply the "success" style to the string
#         :return: the styled ANSIString
#         """
#         return SUCCESS.apply_to(self)
#
#     def warning(self):
#         """
#         Apply the "warning" style to the string
#         :return: the styled ANSIString
#         """
#         return WARNING.apply_to(self)
#
#     def error(self):
#         """
#         Apply the "error" style to the string
#         :return: the styled ANSIString
#         """
#         return ERROR.apply_to(self)
#
#     # EFFECTS
#     def reset(self):
#         return ANSIString(ANSICode.reset() + self)
#
#     def bold(self, reset_after: bool = True):
#         """
#         Apply bold to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bold() + self)
#         else:
#             return ANSIString(ANSICode.bold() + self + ANSICode.reset())
#
#     def underline(self, reset_after: bool = True):
#         """
#         Apply underline to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.underline() + self)
#         else:
#             return ANSIString(ANSICode.underline() + self + ANSICode.reset())
#
#     def reverse(self, reset_after: bool = True):
#         """
#         Apply reverse to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.reverse() + self)
#         else:
#             return ANSIString(ANSICode.reverse() + self + ANSICode.reset())
#
#     # COLORS
#     def black(self, reset_after: bool = True):
#         """
#         Apply black to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.black() + self)
#         else:
#             return ANSIString(ANSICode.black() + self + ANSICode.reset())
#
#     def red(self, reset_after: bool = True):
#         """
#         Apply red to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.red() + self)
#         else:
#             return ANSIString(ANSICode.red() + self + ANSICode.reset())
#
#     def green(self, reset_after: bool = True):
#         """
#         Apply green to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.green() + self)
#         else:
#             return ANSIString(ANSICode.green() + self + ANSICode.reset())
#
#     def yellow(self, reset_after: bool = True):
#         """
#         Apply yellow to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.yellow() + self)
#         else:
#             return ANSIString(ANSICode.yellow() + self + ANSICode.reset())
#
#     def blue(self, reset_after: bool = True):
#         """
#         Apply blue to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.blue() + self)
#         else:
#             return ANSIString(ANSICode.blue() + self + ANSICode.reset())
#
#     def magenta(self, reset_after: bool = True):
#         """
#         Apply magenta to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.magenta() + self)
#         else:
#             return ANSIString(ANSICode.magenta() + self + ANSICode.reset())
#
#     def cyan(self, reset_after: bool = True):
#         """
#         Apply cyan to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.cyan() + self)
#         else:
#             return ANSIString(ANSICode.cyan() + self + ANSICode.reset())
#
#     def white(self, reset_after: bool = True):
#         """
#         Apply white to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.white() + self)
#         else:
#             return ANSIString(ANSICode.white() + self + ANSICode.reset())
#
#     def bright_black(self, reset_after: bool = True):
#         """
#         Apply bright black to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_black() + self)
#         else:
#             return ANSIString(ANSICode.bright_black() + self + ANSICode.reset())
#
#     def bright_red(self, reset_after: bool = True):
#         """
#         Apply bright red to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_red() + self)
#         else:
#             return ANSIString(ANSICode.bright_red() + self + ANSICode.reset())
#
#     def bright_green(self, reset_after: bool = True):
#         """
#         Apply bright green to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_green() + self)
#         else:
#             return ANSIString(ANSICode.bright_green() + self + ANSICode.reset())
#
#     def bright_yellow(self, reset_after: bool = True):
#         """
#         Apply bright yellow to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_yellow() + self)
#         else:
#             return ANSIString(ANSICode.bright_yellow() + self + ANSICode.reset())
#
#     def bright_blue(self, reset_after: bool = True):
#         """
#         Apply bright blue to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_blue() + self)
#         else:
#             return ANSIString(ANSICode.bright_blue() + self + ANSICode.reset())
#
#     def bright_magenta(self, reset_after: bool = True):
#         """
#         Apply bright magenta to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_magenta() + self)
#         else:
#             return ANSIString(ANSICode.bright_magenta() + self + ANSICode.reset())
#
#     def bright_cyan(self, reset_after: bool = True):
#         """
#         Apply bright cyan to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_cyan() + self)
#         else:
#             return ANSIString(ANSICode.bright_cyan() + self + ANSICode.reset())
#
#     def bright_white(self, reset_after: bool = True):
#         """
#         Apply bright white to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_white() + self)
#         else:
#             return ANSIString(ANSICode.bright_white() + self + ANSICode.reset())
#
#     def black_background(self, reset_after: bool = True):
#         """
#         Apply black background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.black_background() + self)
#         else:
#             return ANSIString(ANSICode.black_background() + self + ANSICode.reset())
#
#     def red_background(self, reset_after: bool = True):
#         """
#         Apply red background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.red_background() + self)
#         else:
#             return ANSIString(ANSICode.red_background() + self + ANSICode.reset())
#
#     def green_background(self, reset_after: bool = True):
#         """
#         Apply green background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.green_background() + self)
#         else:
#             return ANSIString(ANSICode.green_background() + self + ANSICode.reset())
#
#     def yellow_background(self, reset_after: bool = True):
#         """
#         Apply yellow background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.yellow_background() + self)
#         else:
#             return ANSIString(ANSICode.yellow_background() + self + ANSICode.reset())
#
#     def blue_background(self, reset_after: bool = True):
#         """
#         Apply blue background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.blue_background() + self)
#         else:
#             return ANSIString(ANSICode.blue_background() + self + ANSICode.reset())
#
#     def magenta_background(self, reset_after: bool = True):
#         """
#         Apply magenta background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.magenta_background() + self)
#         else:
#             return ANSIString(ANSICode.magenta_background() + self + ANSICode.reset())
#
#     def cyan_background(self, reset_after: bool = True):
#         """
#         Apply cyan background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.cyan_background() + self)
#         else:
#             return ANSIString(ANSICode.cyan_background() + self + ANSICode.reset())
#
#     def white_background(self, reset_after: bool = True):
#         """
#         Apply white background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.white_background() + self)
#         else:
#             return ANSIString(ANSICode.white_background() + self + ANSICode.reset())
#
#     def bright_black_background(self, reset_after: bool = True):
#         """
#         Apply bright black background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_black_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_black_background() + self + ANSICode.reset())
#
#     def bright_red_background(self, reset_after: bool = True):
#         """
#         Apply bright red background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_red_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_red_background() + self + ANSICode.reset())
#
#     def bright_green_background(self, reset_after: bool = True):
#         """
#         Apply bright green background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_green_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_green_background() + self + ANSICode.reset())
#
#     def bright_yellow_background(self, reset_after: bool = True):
#         """
#         Apply bright yellow background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_yellow_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_yellow_background() + self + ANSICode.reset())
#
#     def bright_blue_background(self, reset_after: bool = True):
#         """
#         Apply bright blue background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_blue_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_blue_background() + self + ANSICode.reset())
#
#     def bright_magenta_background(self, reset_after: bool = True):
#         """
#         Apply bright magenta background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_magenta_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_magenta_background() + self + ANSICode.reset())
#
#     def bright_cyan_background(self, reset_after: bool = True):
#         """
#         Apply bright cyan background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_cyan_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_cyan_background() + self + ANSICode.reset())
#
#     def bright_white_background(self, reset_after: bool = True):
#         """
#         Apply bright white background to the string
#         :param reset_after: end the string with a RESET code
#         :return: the transformed ANSIString
#         """
#         if not reset_after:
#             return ANSIString(ANSICode.bright_white_background() + self)
#         else:
#             return ANSIString(ANSICode.bright_white_background() + self + ANSICode.reset())
