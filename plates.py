# Define main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define is_valid
def is_valid(s):

    # Check if the license plate starts with at least two letters
    if not starts_with_two_letters(s):
        return False

    # Check license plate length
    if not has_valid_length(s):
        return False
    # Check if the numbers are at the end
    if not numbers_at_end(s):
        return False

    # Check for invalid characters
    if not numbers_at_end(s):
        return False

    return True


def starts_with_two_letters (s):
    return len(s) >= 2 and s[0:2].isalpha()

def has_valid_length (s):
    return 2 <= len(s) <= 6

def numbers_at_end(s):

    # Find the first occurrence of a number
    for index, char in enumerate(s):
         if char.isdigit():
             # Check if it is the first number and is not '0'
             if index == 0 or (char == '0' and index == len(s) - 1):
                 return False
             #Check if there are any alphabetic characters after a number
             if not s[index:].isdigit():
                return False
    return True     # If there are no numbers, it is valid

def no_invalid_characters(s):
    return all(c.isalnum() for c in s)

# Run the program
if __name__ == "__main__":
    main()
