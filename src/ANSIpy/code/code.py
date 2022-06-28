class ANSICode:
    """
    Class to model generic ANSI codes
    """
    _code: str

    def __init__(self, code: str):
        self._code = code

    def __str__(self):
        return self._code

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()

    def apply(self, string: str) -> str:
        """
        Apply the code to a string

        Parameters:
            string (str): string to be enriched

        Returns:
            str: the enriched string
        """
        return self + string


# Default
RESET = ANSICode("\x1b[0m")
