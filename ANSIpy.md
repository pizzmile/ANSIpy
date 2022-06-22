# ANSIpy package

## Subpackages


* [ANSIpy.code package](ANSIpy.code.md)


    * [Submodules](ANSIpy.code.md#submodules)


    * [ANSIpy.code.code module](ANSIpy.code.md#module-ANSIpy.code.code)


    * [ANSIpy.code.color module](ANSIpy.code.md#module-ANSIpy.code.color)


    * [ANSIpy.code.cursor module](ANSIpy.code.md#module-ANSIpy.code.cursor)


    * [ANSIpy.code.effect module](ANSIpy.code.md#module-ANSIpy.code.effect)


    * [Module contents](ANSIpy.code.md#module-ANSIpy.code)


## Submodules

## ANSIpy.print module


### ANSIpy.print.ansiprint(string: str, \*\*kwargs)
Print a string with the specified ANSI codes
:param string: string to print
:param kwargs: optional arguments to encode the color and the effects of ‘string’
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
:return: None

## ANSIpy.string module


### _class_ ANSIpy.string.ANSIString()
Bases: `str`

Class to model string type that implement specific method to add ANSI style codes


#### bg_color_16bit(name: str)
Colorize the background of the string
:param name: name of the 16bit color
:return: the colored string


#### bg_color_hex(hex_code: str)
Colorize the background of the string
:param hex_code: hexadecimal color code
:return: the colored string


#### bg_color_rgb(red: int, green: int, blue: int)
Colorize the background of the string
:param red: red channel value
:param green: green channel value
:param blue: blue channel value
:return: the colored string


#### fg_color_16bit(name: str)
Colorize the foreground of the string
:param name: name of the 16bit color
:return: the colored string


#### fg_color_hex(hex_code: str)
Colorize the foreground of the string
:param hex_code: hexadecimal color code
:return: the colored string


#### fg_color_rgb(red: int, green: int, blue: int)
Colorize the foreground of the string
:param red: red channel value
:param green: green channel value
:param blue: blue channel value
:return: the colored string


#### stylize(style: ANSIStyle)
## ANSIpy.style module


### _class_ ANSIpy.style.ANSIStyle(\*\*kwargs)
Bases: `object`

Class to model a collection of ANSI codes that define a custom style


#### apply(string)
Apply the style to ‘string’
:param string: string to enrich
:return: the enriched string


#### get_background_color()
Get the value of the property background_color
:return: None


#### get_blinking()
Get the value of the property blinking
:return: None


#### get_bold()
Get the value of the property bold
:return: None


#### get_faint()
Get the value of the property faint
:return: None


#### get_foreground_color()
Get the value of the property foreground_color
:return: None


#### get_hidden()
Get the value of the property hidden
:return: None


#### get_inverse()
Get the value of the property inverse
:return: None


#### get_italic()
Get the value of the property italic
:return: None


#### get_reset_after()
Get the value of the property reset_after
:return: None


#### get_reset_before()
Get the value of the property reset_before
:return: None


#### get_strikethrough()
Get the value of the property strikethrough
:return: None


#### get_underline()
Get the value of the property underline
:return: None


#### set_background_color(value: [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor))
Set background_color property
:param value: value to be set for the property
:return: None


#### set_blinking(value: bool)
Set blinking property
:param value: value to be set for the property
:return: None


#### set_bold(value: bool)
Set bold property
:param value: value to be set for the property
:return: None


#### set_faint(value: bool)
Set faint property
:param value: value to be set for the property
:return: None


#### set_foreground_color(value: [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor))
Set foreground_color property
:param value: value to be set for the property
:return: None


#### set_hidden(value: bool)
Set hidden property
:param value: value to be set for the property
:return: None


#### set_inverse(value: bool)
Set inverse property
:param value: value to be set for the property
:return: None


#### set_italic(value: bool)
Set italic property
:param value: value to be set for the property
:return: None


#### set_reset_after(value: bool)
Set reset_after property
:param value: value to be set for the property
:return: None


#### set_reset_before(value: bool)
Set reset_before property
:param value: value to be set for the property
:return: None


#### set_strikethrough(value: bool)
Set strikethrough property
:param value: value to be set for the property
:return: None


#### set_underline(value: bool)
Set underline property
:param value: value to be set for the property
:return: None

## Module contents
