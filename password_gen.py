# Secure Password Generator
# ------------------------------------------------
# * Use Variables, Strings, Loops, Functions. 
# 1. A password should be at least 12 characters 
#    long (ideally 16 characters or more).
# 2. A password should include a combination of 
#    letters (both uppercase and lowercase), numbers, 
#    and characters.
# 3. A password shouldn't include any of your 
#    personal information.
# 4. A password shouldn't contain any consecutive 
#    letters or numbers (i.e., ABCD, 1234, etc.)
# 5. A password shouldn't be the word 'password' 
#    or the same letter or number repeated.

from random import choice

# Sets of chars as constants

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SYMBOLS = "!#$%&/()=?¡¨*[];:_,.-+'¿<>|°¬@̣"

CHARACTER_CHOICE = [UPPERCASE, LOWERCASE, NUMBERS, SYMBOLS]

# Functions

def get_password_length() -> int:
    """
    This function asks the user for the desired length
    they want the password to be (between 12 and 16).
    
    Returns:
        int: password length 
    """
    
    while True:
        try:
            length = int(input(
                "Please enter the length of the password "
                "(between 12 and 16): "
                ))
        except ValueError as e:
            print(f"Error, invalid input: {e}")
        else:
            if 12 <= length <= 16:
                break
            else:
                print("The password length must be between 12 and 16")
        
    return length

def password_build(length: int) -> str:
    """
    This function builds the password without
    quality assurance using the random module and
    a set of characters.
    
    Args:
        length (int): password length

    Returns:
        str: password without quality assurance
    """
    
    password = ""
    
    for _ in range(length):
        character_set = choice(CHARACTER_CHOICE)
        char = choice(character_set)
        password += str(char)
    
    return password

def password_quality_assurance(password: str) -> str:
    """
    This function checks if the password 
    generated has consecutive repeated chars.
    If it does, it replaces them with a new char.
    Also, it can be used to enhance existing 
    passwords.

    Args:
        password (str): Password previously 
        generated or password to enhance
    Returns:
        str: Password quality assurance completed
    """

    def pick_new_char() -> str:
        character_set = choice(CHARACTER_CHOICE)
        char = choice(character_set)
        return char
    
    password_list = list(password)
    
    for i in range(1, len(password_list)):
        if password_list[i] == password_list[i-1]:
            password_list[i] = pick_new_char()
            print(f"Found repeated consecutive character"
                  f" '{password_list[i-1]}', formatting")
        
    return ''.join(password_list)