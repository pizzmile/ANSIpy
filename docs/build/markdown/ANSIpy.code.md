# ANSIpy.code package

## Submodules

## ANSIpy.code.code module


### _class_ ANSIpy.code.code.ANSICode(code: str)
Bases: `object`

Class to model generic ANSI codes


#### apply(string: str)
Apply the code to a string


* **Parameters**

    **string** (*str*) – string to be enriched



* **Returns**

    the enriched string



* **Return type**

    str


## ANSIpy.code.color module


### _class_ ANSIpy.code.color.ANSIColor(code: Optional[str] = None)
Bases: `ANSICode`

Class to model generic ANSI codes for color


#### apply(string: str, reset_after: bool = True)
Apply the color code to a string


* **Parameters**

    
    * **string** (*str*) – string to be enriched


    * **reset_after** (*bool*) – if true add a reset code at the end



* **Returns**

    the enriched string



* **Return type**

    str



### _class_ ANSIpy.code.color.ANSIColor256(value: int, background: bool = False)
Bases: `ANSIColor`

Class to model extended ANSI codes for color


#### value(_: in_ )

### _class_ ANSIpy.code.color.ANSIColorHEX(hex_code: str, background: bool = False)
Bases: `ANSIColorRGB`

Class to model ANSI codes for HEX color


#### blue(_: in_ )

#### green(_: in_ )

#### red(_: in_ )

### _class_ ANSIpy.code.color.ANSIColorRGB(red: int = 0, green: int = 0, blue: int = 0, background: bool = False)
Bases: `ANSIColor`

Class to model ANSI codes for RGB color


#### blue(_: in_ )

#### green(_: in_ )

#### red(_: in_ )
## ANSIpy.code.cursor module


### _class_ ANSIpy.code.cursor.ANSICursor()
Bases: `object`

Class to model the cursor in the terminal


#### _static_ erase(command: str)
Erase a portion of the screen as specified by command

Available commands:
UNTIL_END_SCREEN
FROM_START_SCREEN
SCREEN
SAVED
UNTIL_END_LINE
FROM_START_LINE
LINE


* **Parameters**

    **command** (*str*) – specify the erase mode



* **Returns**

    


* **Return type**

    None



#### _static_ position(command: str, \*\*kwargs)
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


* **Parameters**

    
    * **command** (*str*) – determine how to move the cursor


    * **kwargs** – optional arguments for movement



* **Returns**

    


* **Return type**

    None



#### _static_ restore_position()
Restore the position of the cursor


* **Returns**

    


* **Return type**

    None



#### _static_ restore_screen()
Restore the saved screen


* **Returns**

    


* **Return type**

    None



#### _static_ save_position()
Save the position of the cursor


* **Returns**

    


* **Return type**

    None



#### _static_ save_screen()
Save the screen


* **Returns**

    


* **Return type**

    None



#### _static_ screen_mode(mode_id: int)
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


* **Parameters**

    **mode_id** (*int*) – id of the mode



* **Returns**

    


* **Return type**

    None



#### _static_ set_cursor_visibility(value: bool)
Change cursor visibility


* **Parameters**

    **value** (*bool*) – if true set the cursor visible, if false invisible



* **Returns**

    


* **Return type**

    None


## ANSIpy.code.effect module


### _class_ ANSIpy.code.effect.ANSIEffect(code: str, reset: str)
Bases: `ANSICode`

Class to model ANSI codes for effects


#### apply(string: str, reset_after: bool = True)
Apply the effect code to a string


* **Parameters**

    
    * **string** (*str*) – string to be enriched


    * **reset_after** (*bool*) – if true add a reset code at the end



* **Returns**

    the enriched string



* **Return type**

    str



#### reset(_: st_ )
## Module contents
