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
            print(f"Error, invalid input: {e}")
        else:
            if 0 <= choice <= 3:
                break
            else:
                print("The choice must be an option between 0 and 3")
    return choice

def game_start() -> int:
    pass

