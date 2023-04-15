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

# OK TASK: get the data
# (can't find a source to download & using webscraping is out-of-scope,
# so I'll just create the lists myself).
# generate a seperate data.csv for that
data = pd.read_csv('data.csv', sep=';')
# print(data)

# OK TASK: initialize the game with some ASCII art
# print(art.LOGO)
# print("Welcome to the Cycling Quiz!")

# TASK: ask user which race it wants to play with

# TASK: ask user for winners of the last 10 years

# TASK: check if the user's guess was correct

# TASK: keep track of user score

# TASK: ask user if it wants to play again (different race)
