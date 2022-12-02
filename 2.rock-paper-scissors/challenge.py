import os
from pyprojroot import here
import re
# https://adventofcode.com/2022/day/2
# Part 1 - calculate score
# read
with open(os.path.join(here(), "data", "2.strategy-guide.txt"), "r") as f:
    txt = f.read()
txt = txt.replace(" ", "\n")
txt = txt.split("\n")
# process
oppPat = re.compile("A|B|C")
opponent = [letter for letter in txt if oppPat.search(letter)]
myPat = re.compile("X|Y|Z")
me = [letter for letter in txt if myPat.search(letter)]
# Recode the codes for my strategy
me = ["A" if code == "X" else "B" if code == "Y" else "C" for code in me]

# rules
"""
The score for a single round is the score for the shape you selected (1 for Rock, 2 for
Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3
if the round was a draw, and 6 if you won)
"""
scores = list()
for x, y in zip(opponent, me):
    score = 0
    if y == "A":
        score += 1
    elif y == "B":
        score += 2
    else:
        score += 3

    if x == y:
        # catch all draw cases
        score += 3
    elif (x == "A" and y == "B") or (x == "B" and y == "C") or (x == "C" and y == "A"):
        # catch all win cases
        score += 6
    else:
        # lose conditions
        print("I lose!")
    scores.append(score)
print(f"In total, I scored {sum(scores):,} points")



