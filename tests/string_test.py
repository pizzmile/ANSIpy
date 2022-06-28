import unittest

from src.ANSIpy import ANSIString, COLOR_STRINGS


class ANSICodeTest(unittest.TestCase):
    def test_concatenation(self):
        string = "Hello"
        ansi_string = ANSIString("World")

        self.assertEqual(string + " " + ansi_string, "Hello World")
        self.assertEqual(ansi_string + " " + string, "World Hello")

    def test_conversion(self):
        string = "Hello World"
        ansi_string = ANSIString("Hello World")

        self.assertEqual(str(ansi_string), string)

    def test_16bit_color(self):
        # Test for legal arguments
        ansi_string = ANSIString("FOREGROUND")
        for key in COLOR_STRINGS['FOREGROUND_16'].keys():
            print(ansi_string.color_16bit(key))

        print()

        ansi_string = ANSIString("BACKGROUND")
        for key in COLOR_STRINGS['BACKGROUND_16'].keys():
            print(ansi_string.color_16bit(key, background=True))

        # Test for illegal arguments
        self.assertRaises(ValueError, ansi_string.color_16bit, "PIPPO")
        self.assertRaises(ValueError, ansi_string.color_16bit, "PLUTO", background=True)

    def test_256bit_color(self):
        # Test for legal arguments
        ansi_string = ANSIString("FOREGROUND")
        for i in range(0, 256):
            print(ansi_string.color_256bit(i))

        ansi_string = ANSIString("BACKGROUND")
        for i in range(0, 256):
            print(ansi_string.color_256bit(i, background=True))

        # Test for illegal arguments
        self.assertRaises(ValueError, ansi_string.color_256bit, -1)
        self.assertRaises(ValueError, ansi_string.color_256bit, 256)
        self.assertRaises(ValueError, ansi_string.color_256bit, -1, background=True)
        self.assertRaises(ValueError, ansi_string.color_256bit, 256, background=True)

    def test_rgb_color(self):
        # Test for legal arguments
        ansi_string = ANSIString("FOREGROUND")
        print(ansi_string.color_rgb(255, 0, 0))
        print(ansi_string.color_rgb(125, 125, 0))
        print(ansi_string.color_rgb(0, 255, 0))
        print(ansi_string.color_rgb(0, 125, 125))
        print(ansi_string.color_rgb(0, 0, 255))
        print(ansi_string.color_rgb(125, 0, 125))
        print(ansi_string.color_rgb(255, 255, 255))
        print(ansi_string.color_rgb(0, 0, 0))

        ansi_string = ANSIString("BACKGROUND")
        print(ansi_string.color_rgb(255, 0, 0, background=True))
        print(ansi_string.color_rgb(125, 125, 0, background=True))
        print(ansi_string.color_rgb(0, 255, 0, background=True))
        print(ansi_string.color_rgb(0, 125, 125, background=True))
        print(ansi_string.color_rgb(0, 0, 255, background=True))
        print(ansi_string.color_rgb(125, 0, 125, background=True))
        print(ansi_string.color_rgb(255, 255, 255, background=True))
        print(ansi_string.color_rgb(0, 0, 0, background=True))

        # Test for illegal arguments
        self.assertRaises(ValueError, ansi_string.color_rgb, -1, 0, 0)
        self.assertRaises(ValueError, ansi_string.color_rgb, 256, 0, 0)
        self.assertRaises(ValueError, ansi_string.color_rgb, -1, 0, 0, background=True)
        self.assertRaises(ValueError, ansi_string.color_rgb, 256, 0, 0, background=True)

    def test_hex_color(self):
        # Test for legal arguments
        ansi_string = ANSIString("FOREGROUND")
        print(ansi_string.color_hex("#FFFFFF"))
        print(ansi_string.color_hex("#000000"))
        print(ansi_string.color_hex("#FF0000"))
        print(ansi_string.color_hex("#00FF00"))
        print(ansi_string.color_hex("#0000FF"))

        ansi_string = ANSIString("BACKGROUND")
        print(ansi_string.color_hex("#FFFFFF", background=True))
        print(ansi_string.color_hex("#000000", background=True))
        print(ansi_string.color_hex("#FF0000", background=True))
        print(ansi_string.color_hex("#00FF00", background=True))
        print(ansi_string.color_hex("#0000FF", background=True))

        # Test for illegal arguments
        self.assertRaises(ValueError, ansi_string.color_hex, "prova")
        self.assertRaises(ValueError, ansi_string.color_hex, "#FF000000")
        self.assertRaises(ValueError, ansi_string.color_hex, "prova", background=True)
        self.assertRaises(ValueError, ansi_string.color_hex, "#FF000000", background=True)
