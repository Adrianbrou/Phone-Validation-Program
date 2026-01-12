import re

# function to validate us number


def phone_validation(phone_number):
    pattern = r'^(\+1[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}$'
    return bool(re.match(pattern, phone_number))

# need to use a wrapper

# function to find a us number into a file


def find_usa_number(phone_number):
    pattern = r'^(\+1[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}$'
    result = re.search(pattern, phone_number)
    return result


find_usa_number("+49 151 23456789")
