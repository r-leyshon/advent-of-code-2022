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

def choice_score(selection, outcome):
    """Return the score for the chosen play.

    Args:
        selection (str): Either 'A', 'B' or 'C'. Corresponding to Rock,
        Paper, Scissors.
        outcome (str): Either 'lose', 'draw' or 'win'.

    Returns:
        int: An updated score including the selected value.
    """
    score = 0
    if selection == "A":
        score += 1
    elif selection == "B":
        score += 2
    else:
        score += 3
    
    if outcome == "win":
        score += 6
    elif outcome == "draw":
        score += 3
    else:
        return score

    return score



scores = list()
for x, y in zip(opponent, me):
    if x == y:
        outcome = "draw"
    elif (x == "A" and y == "B") or (x == "B" and y == "C") or (x == "C" and y == "A"):
        outcome = "win"
    else:
        outcome = "lose"        

    score = choice_score(y, outcome)


    
    scores.append(score)
print(f"In total, I scored {sum(scores):,} points")

# Part 2
"""Anyway, the second column says how the round needs to end: X means you
need to lose, Y means you need to end the round in a draw, and Z means you
need to win. Good luck!"""
scores = list()
for x, y in zip(opponent, me):
    if y == "B":
        # draw, so set your choice to opponents
        choice = x
        outcome = "draw"
    elif y == "C":
        outcome = "win"
        if x == "A":
            choice = "B"
        elif x == "B":
            choice = "C"
        else:
            choice = "A"
    else:
        outcome = "lose"
        if x == "A":
            choice = "C"
        elif x == "B":
            choice = "A"
        else:
            choice = "B"
    score = choice_score(choice, outcome)
    scores.append(score)

print(f"After the new instructions, I scored {sum(scores):,} points.")
