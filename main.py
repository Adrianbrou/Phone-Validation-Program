# phone validator
import re
from phone import phone_validation
from us_numb import find_us_numbers

while (True):
    try:
        print("""
            1.search  number
            2.verify number
            3.exit
            """)

        choice = input("Choose an option :")
        if choice == "1":
            find_us_numbers()
        elif choice == "2":
            phone_numb = input("Please enter the phone number :")

            if phone_validation(phone_numb):
                print("Valid phone number ")
            else:
                print("Invalid phone number")
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid Input")
    except ValueError as e:
        print("Invalid input :", e)
