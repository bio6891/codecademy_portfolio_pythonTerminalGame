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


# ask user which race it wants to play with
def pick_race():
    """ Function that asks the user to pick a race from a list of races"""
    print(f"Available races: {', '.join(unique_races)}")
    answer = str(input("Pick a race from the ones listed above: ")).title()
    return answer


def check_winner(name, race):
    """ Function that will perform checks on the name of the winner the user has picked """
    data_selected_race = data[data.race_name == race]
    return name in list(data_selected_race.rider_last_name)


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

    # ask user to pick winner and perform checks
    USER_PICKS_LEFT = 20
    picked_winners = []
    USER_SCORE = 0
    while USER_PICKS_LEFT > 0 and len(picked_winners) < 10:
        print(f"\nYour current score: {USER_SCORE}/10.\nYou have {USER_PICKS_LEFT} picks left.")
        winner_pick = str(input(f"Pick a winner from {race_pick} between {oldest_year} & {newest_year}: ")).title()
        if winner_pick in picked_winners:
            print(f"\nYou've picked '{winner_pick}' already. Try Again.\n")
        elif check_winner(winner_pick, race_pick):
            USER_SCORE += 1
            picked_winners.append(winner_pick)
            print("\nCorrect! Next guess.\n")
            USER_PICKS_LEFT -= 1
        else:
            print("\nWrong! Try Again.\n")
            USER_PICKS_LEFT -= 1
    GAME_IS_ON = False

# TODO: take into account that 1 rider could have won multiple time in the past ten 10 years
# TODO: take into account that due to Covid19 Paris Roubaix didn't have a winner in 2020 ...
# TODO: end game if user has guessed all winners
# TODO: end game is user input equals 'exit'