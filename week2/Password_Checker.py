MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"
NUMBERS = "0123456789"

def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    # TODO: if length is wrong, return False
    passwordlength = len(password)
    if passwordlength < MIN_LENGTH or passwordlength > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper+=1
        if char.isdigit():
            count_digit+=1
        if char in SPECIAL_CHARACTERS:
            count_special+=1
            print(count_special)

        pass

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0 or count_upper ==0 or count_digit ==0:
        return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero
    if count_special ==0:
        return False
    # if we get here (without having returned False), then the password must be valid
    return True




main()
