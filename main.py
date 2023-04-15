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

# DONE TASK: get the data
# (can't find a source to download & using webscraping is out-of-scope,
# so I'll just create the lists myself).
# generate a seperate data.csv for that
data = pd.read_csv(DATA_FILE, sep=';')
# print(data)

# DONE TASK: create list that contains unique race names present in data.
# the user will be able to choose a race from this list.
unique_races = list(data.race_name.unique())

# TASK: get the oldest & newest year from the years present in data column year
oldest_year = int(data.year.min())
newest_year = int(data.year.max())


# TASK: ask user which race it wants to play with
def pick_race():
    """ Function that asks the user to pick a race from a list of races"""
    print(f"Available races: {', '.join(unique_races)}")
    answer = input("Pick a race from the ones listed above: ")
    return answer


# OK TASK: initialize the game with some ASCII art
print(art.LOGO)
print("-------------------------------------------------------------------------------------------")
print("Welcome to the Cycling Quiz!")
print("Instructions: Pick a race and name the last 10 winners (using last names in random order)")
print("Instructions: Answer 'exit' to quit the game.")
print("Good Luck!")
print("-------------------------------------------------------------------------------------------")

GAME_IS_ON = True
while GAME_IS_ON:
    # TASK: ask user which race it wants to play with
    race_choice = pick_race()

    # TASK: check if race_choice in unique_races. If not, ask again
    if race_choice not in unique_races:
        print(f"{race_choice} not in list of available races. Try Again.\n")
        race_choice = pick_race()

    # TASK: ask user for winners of the last 10 years
    # answer = input(f"Pick a winner from {race_choice}")
    # TASK: check if the user's guess was correct

    # TASK: keep track of user score

    # TASK: ask user if it wants to play again (different race)

    GAME_IS_ON = False