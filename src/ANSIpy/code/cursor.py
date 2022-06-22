import sys

from .code import ANSICode

POSITION_STRINGS = {
    "END": "\r",
    "HOME": "\x1b[H",
    "TO": "\x1b[{line};{column}H",
    "UP": "\x1b[{n}A",
    "DOWN": "\x1b[{n}B",
    "RIGHT": "\x1b[{n}C",
    "LEFT": "\x1b[{n}D",
    "NEXT_LINE": "\x1b[{n}E",
    "PREV_LINE": "\x1b[{n}F",
    "COLUMN": "\x1b[{n}G",
    "GET": "\x1b[6n",
    "SAVE": "\x1b[s",
    "RESTORE": "\x1b[u"
}

ERASE_STRINGS = {
    "UNTIL_END_SCREEN": "\x1b[0J",
    "FROM_START_SCREEN": "\x1b[1J",
    "SCREEN": "\x1b[2J",
    "SAVED": "\x1b[3J",
    "UNTIL_END_LINE": "\x1b[0K",
    "FROM_START_LINE": "\x1b[1K",
    "LINE": "\x1b[2K",
}

SCREEN_MODE_FORMAT = "\x1b[={id}h"
SAVE_SCREEN = "\x1b[?47l"
RESTORE_SCREEN = "\x1b[?47h"

CURSOR_MODES = {
    "VISIBLE": "\x1b[?25l",
    "INVISIBLE": "\x1b[?25h"
}


class ANSICursor:
    """
    Class to model the cursor in the terminal
    """

    # Position
    @staticmethod
    def position(command: str, **kwargs) -> None:
        """
        Move the cursor

        Movements:
        END - Move the cursor to the end
        HOME - Move the cursor to the home position
        TO - Move the cursor to a specific position (params: row, column)
        UP - Move the cursor N lines up (params: n)
        DOWN - Move the cursor N lines down (params: n)
        RIGHT - Move the cursor N columns to the right (params: n)
        LEFT - Move the cursor N columns to the left (params: n)
        NEXT_LINE - Move the cursor N lines after (params: n)
        PREV_LINE - Move the cursor N lines before (params: n)
        COLUMN - Move the cursor to the column N (params: n)

        :param str command: determine how to move the cursor
        :param kwargs: optional arguments for movement
        :return:
        :rtype: None
        """
        try:
            if len(kwargs) > 0:
                sys.stdout.write(POSITION_STRINGS[command].format(**kwargs))
            else:
                sys.stdout.write(POSITION_STRINGS[command])
        except KeyError:
            raise ValueError(f"Unknown command {command}")

    # TODO: to be developed
    # @staticmethod
    # def get_position() -> None:
    #     """
    #     Get the position of the cursor
    #     :return:
    #     """
    #     sys.stdout.write(POSITION_STRINGS["GET_POSITION"])

    @staticmethod
    def save_position() -> None:
        """
        Save the position of the cursor

        :return:
        :rtype: None
        """
        sys.stdout.write(POSITION_STRINGS["SAVE_POSITION"])

    @staticmethod
    def restore_position() -> None:
        """
        Restore the position of the cursor

        :return:
        :rtype: None
        """
        sys.stdout.write(POSITION_STRINGS["RESTORE_POSITION"])

    # Erase
    @staticmethod
    def erase(command: str) -> None:
        """
        Erase a portion of the screen as specified by command

        Available commands:
        UNTIL_END_SCREEN
        FROM_START_SCREEN
        SCREEN
        SAVED
        UNTIL_END_LINE
        FROM_START_LINE
        LINE

        :param str command: specify the erase mode
        :return:
        :rtype: None
        """
        try:
            sys.stdout.write(ERASE_STRINGS[command])
        except KeyError:
            raise ValueError(f"Unknown command {command}")

    # Screen mode
    @staticmethod
    def screen_mode(mode_id: int) -> None:
        """
        Change screen mode

        Mode ids:
        0 =>  40 x 25 monochrome (text)
        1 =>  40 x 25 color (text)
        2 =>  80 x 25 monochrome (text)
        3 =>  80 x 25 color (text)
        4 =>  320 x 200 4-color (graphics)
        5 =>  320 x 200 monochrome (graphics)
        6 =>  640 x 200 monochrome (graphics)
        7 =>  Enables line wrapping
        13 =>  20 x 200 color (graphics)
        14 =>  40 x 200 color (16-color graphics)
        15 =>  40 x 350 monochrome (2-color graphics)
        16 =>  40 x 350 color (16-color graphics)
        17 =>  40 x 480 monochrome (2-color graphics)
        18 =>  40 x 480 color (16-color graphics)
        19 =>  20 x 200 color (256-color graphics)

        :param int mode_id: id of the mode
        :return:
        :rtype: None
        """
        if mode_id < 0 or mode_id > 19:
            raise ValueError("'mode_id' must be grater than 0 and lesser or equal than 19")
        sys.stdout.write(SCREEN_MODE_FORMAT.format(id=mode_id))

    # Private mode
    @staticmethod
    def set_cursor_visibility(value: bool) -> None:
        """
        Change cursor visibility

        :param bool value: if true set the cursor visible, if false invisible
        :return:
        :rtype: None
        """
        if value:
            sys.stdout.write(CURSOR_MODES['VISIBLE'])
        else:
            sys.stdout.write(CURSOR_MODES['INVISIBLE'])

    @staticmethod
    def save_screen() -> None:
        """
        Save the screen

        :return:
        :rtype: None
        """
        sys.stdout.write(SAVE_SCREEN)

    @staticmethod
    def restore_screen() -> None:
        """
        Restore the saved screen

        :return:
        :rtype: None
        """
        sys.stdout.write(RESTORE_SCREEN)
