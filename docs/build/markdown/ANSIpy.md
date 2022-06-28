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


* **Parameters**

    
    * **string** (*str*) – string to print


    * **kwargs** – optional arguments to encode the color and the effects of ‘string’



* **Keyword Arguments**

    
    * **foreground_color** – name of the color to be applied as foreground


    * **background_color** – name of the color to be applied as background


    * **foreground_hex** – hexadecimal code of the color to be applied as foreground (overwrite name colors)


    * **background_hex** – hexadecimal code of the color to be applied as background (overwrite name colors)


    * **foreground_rgb** – tuple containing (r, g, b) values for the color to be applied as foreground (overwrite hex


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

## ANSIpy.string module


### _class_ ANSIpy.string.ANSIString()
Bases: `str`

Class to model string type that implement specific method to add ANSI style codes


#### apply_style(style: ANSIStyle)
Apply a style to the string


* **Parameters**

    **style** (*ANSIStyle*) – the style to apply



* **Returns**

    the styled string



* **Return type**

    ANSIString



#### color_16bit(name: str, background: bool = False)
Colorize the string from standard color code


* **Parameters**

    
    * **background** (*bool*) – if true change the background color, if false change the foreground


    * **name** (*str*) – name of the 16bit color



* **Returns**

    the colored string



* **Return type**

    ANSIString



#### color_256bit(value: int, background: bool = False)
Colorize the string from extended color code


* **Parameters**

    
    * **background** (*bool*) – if true change the background color, if false change the foreground


    * **value** (*int*) – the integer value corresponding to the color in extended 256 colors ANSI encoding



* **Returns**

    the colored string



* **Return type**

    ANSIString



#### color_hex(hex_code: str, background: bool = False)
Colorize the string from HEX code


* **Parameters**

    
    * **hex_code** (*str*) – hexadecimal color code


    * **background** (*bool*) – if true change the background color, if false change the foreground



* **Returns**

    the colored string



* **Return type**

    ANSIString



#### color_rgb(red: int, green: int, blue: int, background: bool = False)
Colorize the string from RGB code


* **Parameters**

    
    * **background** (*bool*) – if true change the background color, if false change the foreground


    * **red** (*int*) – red channel value


    * **green** (*int*) – green channel value


    * **blue** (*int*) – blue channel value



* **Returns**

    the colored string



* **Return type**

    ANSIString


## ANSIpy.style module


### _class_ ANSIpy.style.ANSIStyle(\*\*kwargs)
Bases: `object`

Class to model a collection of ANSI codes that define a custom style


#### apply(string)
Apply the style to ‘string’


* **Parameters**

    **string** (*str*) – string to enrich



* **Returns**

    the enriched string



* **Return type**

    str



#### get_background_color()
Get the value of the property background_color


* **Returns**

    background_color attribute



* **Return type**

    [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor)



#### get_blinking()
Get the value of the property blinking


* **Returns**

    blinking attribute



* **Return type**

    bool



#### get_bold()
Get the value of the property bold


* **Returns**

    f attribute



* **Return type**

    bool



#### get_faint()
Get the value of the property faint


* **Returns**

    faint attribute



* **Return type**

    bool



#### get_foreground_color()
Get the value of the property foreground_color


* **Returns**

    foreground_color attribute



* **Return type**

    [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor)



#### get_hidden()
Get the value of the property hidden


* **Returns**

    hidden attribute



* **Return type**

    bool



#### get_inverse()
Get the value of the property inverse


* **Returns**

    inverse attribute



* **Return type**

    bool



#### get_italic()
Get the value of the property italic


* **Returns**

    italic attribute



* **Return type**

    bool



#### get_reset_after()
Get the value of the property reset_after


* **Returns**

    reset_after attribute



* **Return type**

    bool



#### get_reset_before()
Get the value of the property reset_before


* **Returns**

    reset_before attribute



* **Return type**

    bool



#### get_strikethrough()
Get the value of the property strikethrough


* **Returns**

    strikethrough attribute



* **Return type**

    bool



#### get_underline()
Get the value of the property underline


* **Returns**

    underline attribute



* **Return type**

    bool



#### set_background_color(value: [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor))
Set background_color property


* **Parameters**

    **value** ([*ANSIColor*](ANSIpy.code.md#ANSIpy.code.color.ANSIColor)) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_blinking(value: bool)
Set blinking property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_bold(value: bool)
Set bold property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_faint(value: bool)
Set faint property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_foreground_color(value: [ANSIColor](ANSIpy.code.md#ANSIpy.code.color.ANSIColor))
Set foreground_color property


* **Parameters**

    **value** ([*ANSIColor*](ANSIpy.code.md#ANSIpy.code.color.ANSIColor)) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_hidden(value: bool)
Set hidden property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_inverse(value: bool)
Set inverse property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_italic(value: bool)
Set italic property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_reset_after(value: bool)
Set reset_after property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_reset_before(value: bool)
Set reset_before property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_strikethrough(value: bool)
Set strikethrough property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None



#### set_underline(value: bool)
Set underline property


* **Parameters**

    **value** (*bool*) – value to be set for the property



* **Returns**

    


* **Return type**

    None


## Module contents
