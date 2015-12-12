""" christmas.py 
Prints a christmas tree on the terminal using coloured and blinking characters.
Uses ansi terminal escape sequences.
The '\033[' part is the escape code. 
We pass '5;' for the colours other than green to make them blink.
The next part is the colour code and the 'm' ends the sequence.
To reset the colour we pass "\033[0m" after each character.
Python 3 version by antiloquax (2015), based on code from datamungeblog.com.
"""

from random import choice
from random import random

def main():
    """Make the tree and print it."""
    # If you change this, use an odd number.
    SIZE = 21
    print(makeTree(SIZE))

def makeTree(size):
    """Creates the tree string."""  
    # Probability that a character will be green.
    prob_gr = 0.6
    # Colour codes.
    colours = [31, 33, 34, 35, 36, 37]
    # Characters to use for decorations. Experiment with these.
    # The chr(169) and chr(174) characters may not work in all terminals
    # (extended ASCII, c and r in a circle).
    decs = ['@', '&', '*', chr(169), chr(174)]

    # Format string for printing blinking characters.
    blink_col = "\033[5;{0}m{1}\033[0m"
    # String to print a green octothorpe ('#').
    leaf = "\033[32m#\033[0m"

    # Width of the tree, will grow by 2 each time.
    width = 1
    # Initialise the tree string, with a star at the top.
    tree = "\n{}*\n".format(' ' * (size))

    """ Main Loop starts now."""
    
    """ We can't use the normal "format" centering approach:
        ("{:^nn}".format(string) where "nn" is the width of the line), 
        with these ansi codes. This is because Python sees the strings as being
        more than one character long (15 & 10 for baubles and leaves)."""

    # Loop from (size - 1) down to 0, using the counter as the padding size.
    for pad in range(size - 1, -1, -1):
        # Increase the width of the tree by 2.
        width += 2
        
        # Put the characters for the line in "temp".
        temp = ""
        for j in range(width):
            # Make some leaves.
            if random() < prob_gr:
                temp += leaf
            # And also some baubles.
            else:
                temp += blink_col.format(choice(colours), choice(decs))

        # Add that string to the line, with padding.
        tree += "{0}{1}\n".format(' ' * pad, temp)

    # Add a "trunk" of 2 lines and return.
    return tree + "{0}{1}\n".format(' ' * (size - 1), "000") * 2

if __name__ == "__main__":
    main()
