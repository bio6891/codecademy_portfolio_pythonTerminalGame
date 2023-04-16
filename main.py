""" codecademy python course
portfolio project
create a python terminal game
I'll create a cycling quiz.
The user can choose from a predefined list of races
for which it then has to provide the last 10 winners (in random order).
A score out of 10 will be given.
"""

import pandas as pd
import art

# define variables
DATA_FILE = 'data.csv'

# get the data
# (can't find a source to download & using web scraping is out-of-scope,
# so I'll just create the lists myself).
# generate a separate data.csv for that
data = pd.read_csv(DATA_FILE, sep=';')
# print(data)

# create list that contains unique race names present in data.
# the user will be able to choose a race from this list.
unique_races = list(data.race_name.unique())

# get the oldest & newest year from the years present in data column year
oldest_year = int(data.year.min())
newest_year = int(data.year.max())


def pick_race():
    """ Function that asks the user to pick a race from a list of races"""
    print(f"Available races: {', '.join(unique_races)}")
    answer = str(input("Pick a race from the ones listed above: ")).title()
    if not check_exit(answer):
        return answer


def get_unique_winners(race):
    """ Function that will get a list of the unique winners for the selected race """
    data_selected_race = list(data[data.race_name == race].rider_last_name.unique())
    return data_selected_race


def check_exit(answer):
    """ Function that will check if the user has typed 'Exit'. This will end the game. """
    if answer == "Exit":
        print("Thanks for playing! Bye!")
        quit()
    return False


# initialize the game with some ASCII art
print(art.LOGO)
print("-------------------------------------------------------------------------------------------")
print("Welcome to the Cycling Quiz!")
print("Instructions: Pick a race and name the last 10 winners (using last names in random order)")
print("Instructions: Answer 'exit' to quit the game.")
print("Good Luck!")
print("-------------------------------------------------------------------------------------------")

GAME_IS_ON = True
while GAME_IS_ON:
    # ask user which race it wants to play with
    race_pick = pick_race()

    # check if race_pick in unique_races. If not, ask again
    if race_pick not in unique_races:
        print(f"{race_pick} not in list of available races. Try Again.\n")
        race_pick = pick_race()

    # get the number of unique winners for race_pick. Set this to max_score. Let the user know how many many winner it'll has get to get a max_score
    race_unique_winners = get_unique_winners(race_pick)
    max_score = len(race_unique_winners)
    print(f"\nThere are {max_score} unique winners for this race the last 10 years.")

    # ask user to pick winner and perform checks
    USER_PICKS_LEFT = 20
    picked_winners = []
    USER_SCORE = 0
    while USER_PICKS_LEFT > 0 and len(picked_winners) < max_score:
        print(f"\nYour current score: {USER_SCORE}/{max_score}.\nYou have {USER_PICKS_LEFT} picks left.")
        winner_pick = str(input(f"Pick a winner from {race_pick} between {oldest_year} & {newest_year}: ")).title()
        if not check_exit(winner_pick):
            # check if user has guessed this rider already
            if winner_pick in picked_winners:
                print(f"\nYou've picked '{winner_pick}' already. Try Again.\n")
            # check if the picked rider is indeed a winner
            elif winner_pick in race_unique_winners:
                USER_SCORE += 1
                picked_winners.append(winner_pick)
                print("\nCorrect! Next guess.\n")
                USER_PICKS_LEFT -= 1
            else:
                print("\nWrong! Try Again.\n")
                USER_PICKS_LEFT -= 1
    if USER_SCORE == max_score:
        print(f"You've guessed all {max_score} winners of {race_pick}! Congrats! Game will end.")
        GAME_IS_ON = False
    if USER_PICKS_LEFT == 0:
        print(f"You're out of guesses. Total score = {USER_SCORE}. Game will end.")
        GAME_IS_ON = False