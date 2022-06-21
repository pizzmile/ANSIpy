# TODO: implement style
# from .code import ANSICode, RESET, BOLD, UNDERLINE
#
#
# class ANSIStyle:
#     __format = "{string}"
#
#     def __init__(self, fmt):
#         self.__format = fmt
#
#     def apply_to(self, string: str):
#         """
#         Apply the style to a string
#         :param string: string to be styled
#         :return: the styled string
#         """
#         return self.__format.format(string=string)
#
#     @staticmethod
#     def build(color: ANSICode = None, background: ANSICode = None, bold: bool = False, underline: bool = False,
#               reverse: bool = False, reset_after: bool = True):
#         """
#         Build an ANSIStyle object
#         :param color: foreground color
#         :param background: background color
#         :param bold: if true add the BOLD effect (default: False)
#         :param underline: if true add the UNDERLINE effect (default: False)
#         :param reverse: if true add the REVERSE effect (default: False)
#         :param reset_after: if true add a RESET code at the end (default: True)
#         :return: the ANSIStyle object
#         """
#         fmt = "{string}"
#         if color is not None:
#             fmt = color + fmt
#         if background is not None:
#             fmt = background + fmt
#         if bold:
#             fmt = BOLD + fmt
#         if underline:
#             fmt = UNDERLINE + fmt
#         if reverse:
#             fmt = REVERSE + fmt
#         if reset_after:
#             fmt = fmt + RESET
#         return ANSIStyle(fmt)
#
#
# # DEFAULT STYLES
# SUCCESS = ANSIStyle.build(color=BRIGHT_GREEN, bold=True)
# WARNING = ANSIStyle.build(color=BRIGHT_YELLOW, bold=True)
# ERROR = ANSIStyle.build(color=BRIGHT_RED, bold=True)
