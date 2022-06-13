import sys
import os
from time import sleep

# Local files
from config import *

# Adding ASCII color sequences to text
def FormatColors(word):
    # Highligthing for the middle letter
    try:
        word_highlighting_mid = len(word) // 2
        word = word.replace(word[word_highlighting_mid], f"\033[1;{MIDDLE_LETTER}m{word[word_highlighting_mid]}\033[0m", 1)
    except ValueError:
        pass

    # Highligthing for '
    try:
        word_highlighting_apostrophe = word.index("'")
        word = word.replace(word[word_highlighting_apostrophe], f"\033[1;{APOSTROPHE}m{word[word_highlighting_apostrophe]}\033[0m")
    except ValueError:
        pass

    # Highligthing for .
    try:
        word_highlighting_dot = word.index(".")
        word = word.replace(word[word_highlighting_dot], f"\033[1;{DOT}m{word[word_highlighting_dot]}\033[0m")
    except ValueError:
        pass

    try:
        word_highlighting_comma = word.index(",")
        word = word.replace(word[word_highlighting_comma], f"\033[1;{COMMA}m{word[word_highlighting_comma]}\033[0m")
    except ValueError:
        pass

    return word

# "renders" the word to a screen
def Render(word, ClearCommand):
  
    # Gets terminal dimensions
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]
    spaces = [""]
    spaces_stationary = [""]

    for i in range(width // 2 - 3 + PIPE_CALIBRATION):
        spaces_stationary.append(" ")

    os.system(ClearCommand)
    for x in range(height):
    
        print()
        # When it reaches half of the height it will start calculating the half od the width
        if x == (height // 2 + 1):
            
            # When it calculated the half of the width plus some calibration it will append " " in a list
            # The list will have exactly enough spaces in it so the word will be in the center
            
            # Could probably be done in a list coprehension
            for i in range((width // 2 - len(word) // 2) - 1):
                spaces.append(" ")

            print(f"{''.join(spaces_stationary)}\033[1;{PIPE}m|\033[0m")

            word = FormatColors(word)
            print(f"{''.join(spaces)}{word}", end="")

            print(f"\n{''.join(spaces_stationary)}\033[1;{PIPE}m|\033[0m")
            print("\r", end="")

# Returns the command that is appropiate for a certain OS
def Os():
    if os.name in ("posix"):
        return "clear"

    elif os.name in ("nt"):
        return "cls"

os.system(Os())
sentence = input("> Type your sentences here: \n")
sentence = sentence.split()

WPM = len(sentence) / WPM

counter = 0

# Hides the cursor
sys.stdout.write("\033[?25l")

while True:

    try:
        sleep(WPM)
        Render(sentence[counter], Os())

    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h")
        os.system(Os())
        raise SystemExit("\nUser interruped with the operation, aborting.")
    
    if counter == len(sentence) - 1:
        print("Done")
        break

    counter = counter + 1

# Shows the cursor
sys.stdout.write("\033[?25h")