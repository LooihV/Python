from random import randint, choice

# Difficulty

EASY = [0, 50]
MEDIUM = [0, 100]
HARD = [0, 200]

DIFFICULTY = [EASY, MEDIUM, HARD]

# Functions 

def set_difficulty() -> int:
    """
    This Function asks the user the difficulty they want the game to be
    with a choice based prompt between 0 and 3:
        - 1 for easy.
        - 2 for medium.
        - 3 for hard.
        - 0 for a random difficulty.

    Returns:
        int: A number between 0 and 3 as the user's choice.
    """
    while True: 
        try:
            choice = int(input(
                "Difficulty:"
                f"\n 1. Easy {EASY}"
                f"\n 2. Medium {MEDIUM}"
                f"\n 3. Hard {HARD}"
                "\n 0. Random difficulty"
                "\n Please input the desired difficulty (0 -> 3): "
            ))
        except ValueError as e:
            print(f"Error, set difficulty invalid input: {e}")
        else:
            if 0 <= choice <= 3:
                break
            else:
                print("The choice must be an option between 0 and 3")
    return choice

def number_pick(difficulty: int) -> int:
    """
    This function picks a random number depending on the difficulty of
    the user choose previously.

    Args:
        difficulty (int): The difficulty that the user chose previously

    Returns:
        int: The number picked for the user to guess
    """
    number = 0
    
    if difficulty == 1:
        print("Difficulty set to EASY...")
        number = randint(EASY[0], EASY[1])
        print("Easy range 0 to 50."
              "\n ¡Number picked!...")
    elif difficulty == 2:
        print("Difficulty set to MEDIUM...")
        number = randint(MEDIUM[0], MEDIUM[1])
        print("Medium range 0 to 100."
              "\n ¡Number picked!...")
    elif difficulty == 3:
        print("Difficulty set to HARD...")
        number = randint(HARD[0], HARD[1])
        print("Hard range 0 to 200."
              "\n ¡Number picked!...")
    else:
        print("Difficulty set to RANDOM...")
        rand_diff = choice(DIFFICULTY)
        number = randint(rand_diff[0], rand_diff[1])
        print(f"Random range between {rand_diff(0)} and {rand_diff(1)}."
              "\n ¡Number picked!...")
    
    return number

def number_prompt(difficulty: int) -> int:
    """
    This function prompts the user and checks if the number entered by
    the user is within the difficulty range.

    Args:
        difficulty (int): The difficulty choice

    Returns:
        int: Number guessed by the user within the difficulty range
    """
    
    range = DIFFICULTY[(difficulty - 1)]
    
    while True:
        try:
            guess = int(input("Please guess a number within the range "
                            f"{range[0]} to {range[1]}"
                            "\n=> "))
        except Exception as e:
            print(f"Error, number prompt invalid input: {e}")
        else:
            if range[0] <= guess <= range[1]:
                break
            else:
                print(f"The guess must be a number between {range[0]} "
                      f"and {range[1]}")
    return guess

def number_guesser(number: int, difficulty: int) -> int:
    """
    This core function checks the user's choice and gives them clues as 
    to whether it's lower or higher if the choice is wrong.

    Args:
        number (int): The number for the user to guess

    Returns:
        int: The amount of attempts used by the user to guess the number
    """
    attempts = 0
    print(difficulty, type(difficulty))
    input("xd")
    while True:
        try:
            guess = number_prompt(difficulty)
        except Exception as e:
            print(f"Error, number guesser invalid input: {e}")
        else:
            if guess > number:
                if 1 <= (guess-number) <= 10:
                    print("You are close!")
                attempts += 1
                print("Lower!")
            elif guess < number:
                if 1 <= (number-guess) <= 10:
                    print("You are close!")
                attempts += 1
                print("Higher!")
            else:
                attempts += 1
                print("You win!")
                break
    return attempts

def score_calc(attempts: int) -> int:
    """
    This function calculates the score the user got; the base score is
    100. If the user gets it at the first attempt, the score is 99. Each
    attempt subtracts one from the base score.

    Args:
        attempts (int): The amount of attempts used by the user to guess
        the number

    Returns:
        int: The final score
    """
    base_score = 100
    score = base_score - attempts
    
    if score <= 50:
        print("Oh, you'll get better at it")
    elif score >= 90:
        print("You're really good!")
    elif score == 99:
        print("Wow, so lucky!")
    else:
        print("Well done, but you can be better!")
        
    return score

def game():
    """
    This function runs the game
    """
    
    difficulty = set_difficulty()
    number = number_pick(difficulty)
    attempts = number_guesser(number, difficulty)
    score = score_calc(attempts)
    
    print(f"Score: {score}")

            
            

                

