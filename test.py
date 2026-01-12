import json
from phone import *

with open("numbers.txt") as file:
    numb_py = file.read().splitlines()
    # print(numb_py)
with open("numbers.json", "w") as file:
    json.dump(numb_py, file, indent=2)
with open("numbers.json", "r") as file:
    numb_json = json.load(file)
    for numb in numb_json:
        if find_usa_number(numb):
            print("Number found :", numb)
        else:
            print("NO match")

    # print(numb_json)
