from password_gen import *

if __name__ == "__main__":
    length = get_password_length()
    password = password_build(length)
    print(password_quality_assurance(password))
    test = "AAAAAAAAAAAAAAA"
    test = password_quality_assurance(test)
    print(f"Test result {test}")