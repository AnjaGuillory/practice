"""

You are given a Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

Any positions in the grid that do not have a specified character should be filled with a space character.

You can assume the document will always have the same format as the example document linked above.

Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

-----------------------------------------
x-coordinates | Character | y-coordinates
-----------------------------------------
        0          █            0
        0          █            2
        1          ▀            1
        1          ▀            2
        2          ▀            1
        2          ▀            2
        3          ▀            2

"""

"""
Approach

1. Find max of x and y, and build a 2D array out of those values
2. For each x and y, place character in that [x][y] index of the grid

"""
import requests
from html.parser import HTMLParser
"""

Class MyHTMLParser overriding HTMLParser functions
    handle_starttag
    handle_endtag
    handle_data

Using a character dictionary that maps coordinates as key: Tuples
to the respective unicode character as its value: char

Checks for the maximum x and y coordinates for traversing the grid

"""
class MyHTMLParser(HTMLParser):
    charMap = {}
    x_coord = None
    y_coord = None
    unicode_char = None

    max_y_coord = 0
    max_x_coord = 0

    inCol = False

    # Indictaes beginning of table column to begin retrieving data
    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.inCol = True

    # Ends parsing when end of the table colum, is reached
    def handle_endtag(self, tag):
        if tag == 'td':
            self.inCol = False

    # Collects x coordinates, y coordinates, and characters
    def handle_data(self, data):
        if self.x_coord is not None and self.y_coord is not None and self.unicode_char is not None:
            self.charMap[(self.x_coord,self.y_coord)] = self.unicode_char
            self.x_coord = None
            self.y_coord = None
            self.unicode_char = None


        if self.inCol:
            if self.x_coord is None:
                if data.isdigit():
                    self.x_coord = int(data)
                    if self.x_coord > self.max_x_coord:
                        self.max_x_coord = int(data)
            elif self.x_coord is not None and self.unicode_char is None:
                self.unicode_char = data
            elif self.x_coord is not None and self.unicode_char is not None and self.y_coord is None:
                if data.isdigit():
                    self.y_coord = int(data)
                    if self.y_coord > self.max_y_coord:
                        self.max_y_coord = int(data)

"""
decode_message: Loads document from URL argument, feeds to a parser, and prints the decoded message in a gridded format
"""
def decode_message(url, googledoc=None):
    googledoc = requests.get(url)
    parser = MyHTMLParser()
    parser.feed(googledoc.content.decode())
    max_length = max(parser.max_x_coord,parser.max_y_coord)
    secret_msg = ""

    for y_coord in range(max_length, -1, -1):
        for x_coord in range(max_length+1):
            try:
                secret_msg += parser.charMap[(x_coord,y_coord)]
            except KeyError:
                secret_msg += " "
        secret_msg += '\n'

    print(secret_msg)





# decode_message('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')
decode_message('https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub')
#Parse coordinates and characters from document

# █▀▀▀
# █▀▀
# █

# █▀▀▀
# █▀▀
# █
"""
    
3         

2   █   ▀   ▀   ▀

1   █   ▀   ▀

0   █
    0   1   2   3
"""