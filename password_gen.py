# Secure Password Generator
# -------------------------------------------------------------------------------------------
# * Use Variables, Strings, Loops, Functions. 
# 1. A password should be at least 12 characters long (idealy 16 characters or more)
# 2. A password should include a combination of letters (both uppercase and lowercase),
# numbers, and characters
# 3. A password shouldn't include any of your personal information.
# 4. A password shouldn't contain any consecutive letters or numbers (i.e. ABCD, 1234, etc.)
# 5. A password shouldn't be the word 'password or the same letter or number repeated.'

from random import choice

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!#$%&/()=?¡¨*[];:_,.-+'¿<>|°¬@̣"

character_choice = [uppercase, lowercase, numbers, symbols]

password_legnth = int(input("Please enter the legnth of the password (between 12 and 16): "))

password = ""

for i in range(0, password_legnth):
    character_set = choice(character_choice)
    char = choice(character_set)
    password += str(char)

print(password)