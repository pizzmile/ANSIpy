class _ANSICode:
    _code: str
    # _fmt = "\x1b[{code}m"

    def __init__(self, code: str):
        self._code = code

    def apply(self, string: str) -> str:
        return self + string

    def __str__(self):
        return self._code

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()


# GRAPHIC_MODE = "\x1b[1;34;{modes}m"
RESET = _ANSICode("\x1b[0m")
