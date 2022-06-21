# TODO: add function to print
# from .code import *
#
#
# def ansiprint(string: str,
#               color: str = None, background: str = None,
#               bold: bool = False, underline: bool = False, reverse: bool = False):
#     output_str = string + RESET
#
#     if color is not None:
#         try:
#             output_str = FOREGROUND_COLORS[color] + output_str
#         except KeyError:
#             raise ValueError(f'Unknown value for "color", please choose from {FOREGROUND_COLORS.keys()}')
#     if background is not None:
#         try:
#             output_str = BACKGROUND_COLORS[background] + output_str
#         except KeyError:
#             raise ValueError(f'Unknown value for "background", please choose from {BACKGROUND_COLORS.keys()}')
#     if bold:
#         output_str = BOLD + output_str
#     if underline:
#         output_str = UNDERLINE + output_str
#     if reverse:
#         output_str = REVERSE + output_str
#
#     print(output_str)
