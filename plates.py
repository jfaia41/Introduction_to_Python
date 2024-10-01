def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (check_length(s) and
            check_start_with_two_letters(s) and
            check_no_invalid_chars(s) and
            check_numbers_position(s))


def check_length(s):
    # Check if the length is between 2 and 6 characters
    return 2 <= len(s) <= 6


def check_start_with_two_letters(s):
    # Check if the first two characters are letters
    return s[0].isalpha() and s[1].isalpha()


def check_no_invalid_chars(s):
    # Check for only alphanumeric characters
    return s.isalnum()


def check_numbers_position(s):
    # Find the first digit in the string
    number_found = False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and not number_found:
                return False  # First number cannot be '0'
            number_found = True
        elif number_found:
            return False  # If a letter appears after a number, it's invalid
    return True


if __name__ == "__main__":
    main()
