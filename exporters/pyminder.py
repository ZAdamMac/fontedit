"""
##    This file is part of the fork of FontEdit created for the PETI Project
##    This file specifically, copyright 2020 by Zac Adam-MacEwen for Kensho Security Labs
##
##    Fontedit is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    Fontedit is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Fontedit.  If not, see <http://www.gnu.org/licenses/>.
##

##
## Simple exporter for Pyminder's exporter font.
##
## Exports to a python dictionary of character data expressed as an array of 0,1 values.
##

## export function, name is unimportant but must be in the exporters
## dictionary below.  Must take a font object and filename as arguments.
"""

import json

def export(font, filename):
    # useful properties of the font object:
    # font.cols - the number of columns per character (i.e. width in px)
    # font.rows - the number of rows per character (i.e. height in px)
    # font.chars - total number of characters in the font
    # font.get_character(i) - get character number i (where 0<=i<font.chars)
    #                         returns a list of rows of integers
    #                         1 represents foreground in the editor,
    #                         0 represents background
    if font.cols != 8:
        # returning a string will popup an error message in the editor
        return "Can only handle fonts of width 8"

    # prepare the strings to start and end the file, add anything you like
    postamble = """font = %s"""

    # open a file for writing
    with open(filename, "w") as fw:


        # itterate over all characters
        output_font = {}
        for i in range(font.chars):
            if (i >= 32) and (i < 127):  # For convenience we can use string literals.
                key = "%c" % i
            else:  # else, get the unicode string literal
                key = "\\u%04x" % i
            # fetch the array of pixels
            value_raw = font.get_character(i)
            output_pixels = []
            for each in value_raw:
                output_row = []
                for pixel in each:
                    if pixel == 0:
                        output_row.append(1)
                    else:
                        output_row.append(0)
                output_pixels.append(output_row)
            output_font.update({key: output_pixels})

        # finally write the closure of the C list and close the file
        output_font_value = json.dumps(output_font, indent=2)
        fw.write(postamble % output_font_value)

    # return zero to indicate that we were successful
    return 0


# the exporters dict is where the program finds the importer from
# needs name, desc and func parts.
exporters = {"name": "Pyminder Font Exporter",
             "desc": "Matches the 8x12 Font for Pyminder",
             "func": export}


