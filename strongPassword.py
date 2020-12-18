import re


def uppercase_check(password):
    if re.search('[A-Z]', password):  # at least one uppercase character
        return True
    return False


def lowercase_check(password):
    if re.search('[a-z]', password):  # at least one lowercase character
        return True
    return False


def digit_check(password):
    if re.search('[0-9]', password):  # at least one digit
        return True
    return False


def character_check(password):
    if re.search('[!@#$%^&*?|/,.+=]', password):  # at least one special character
        return True
    return False


def user_input_password_check():
    while True:
        password = input("Enter password : ")
        # at least 8 character long
        if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password) \
                and character_check(password):
            print("Strong Password")
            break
        else:
            print("Weak Password. Please input another password.")


user_input_password_check()
