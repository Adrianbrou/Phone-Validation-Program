import re
from phone import *


def find_us_numbers():

    pattern = r'\b(?:\+1[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}\b'

    pattern_2 = r'^(\+1[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}$'

    with open("numbers.txt") as file:
        text = file.read()

    matches = re.findall(pattern, text)

    print("US numbers found:")
    for number in matches:
        if bool(re.match(pattern_2, number)):
            print("US number :", number)
        else:
            print("Not US number", number)
