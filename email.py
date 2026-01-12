import re
# hw 1: email validator


def email_validation(email):
    pattern = r'^[\w+\.-]+@[\w+\.-]+\.\w+$'
    return bool(re.match(pattern, email))


email = input("Please enter your email : ")
# print("Email :", email)

# print(email_validation('wrong@email'))
if email_validation(email):
    print("Valid email")
else:
    print(f"Invalid email")
