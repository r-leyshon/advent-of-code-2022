import os
from pyprojroot import here
import re

# https://adventofcode.com/2022/day/5
# Part 1
# After the rearrangement procedure completes, what crate ends up on top of each stack?

# import
with open(os.path.join(here(), "data", "5.crates.txt")) as f:
    txt = f.read()
    f.close()

crates, guide = txt.split("\n\n")
guide = guide.splitlines()

# too many spaces to see gaps in crates
crates = crates.replace(" ", "-")
crates = crates.splitlines()
# separate out the boxes
allRows = list()
for row in crates:
    start = 0
    stop = 3
    currRow = list()
    print(row[start:stop])
    for i in range(0, 9):
        contents = "".join(row[start:stop]).strip()
        print(contents)
        currRow.append(contents)
        start += 4
        stop += 4
    print(currRow)
    allRows.append(currRow)

stackLabels = allRows.pop(-1)
# stack the crates as list sequences
stacks = list()
for ind, stack in enumerate(stackLabels):
    column = list()
    for row in allRows:
        column.append(row[ind])
    column.append(stack)
    stacks.append(column)


def get_top_box(stack):
    """Get the top populated crate for a given stack

    Args:
        stack (list): A list of stacked crates.
    Returns:
        tuple: (int) The index of the topmost crate, (str) The topmost
        crate content.
    """
    for ind, crate in enumerate(stack):
        if crate == "---":
            pass
        else:
            return (ind, crate)


def interpret_rule(rule):
    """Return the rule details from a string instruction.

    Args:
        rule (str): A rule to match entities and actions. Eg - 'move 5 from
        8 to 2'.

    Returns:
        tuple: (int): number of crates to move. (int): Stack number to move
        crates from. (int): Stack number to move crates to.
    """
    targetIdPat = re.compile("(?<=from )[\d]")
    targetStack = int(targetIdPat.search(rule).group())
    destIdPat = re.compile("(?<=to )[\d]")
    destStack = int(destIdPat.search(rule).group())
    nCratesPat = re.compile("(?<=move )[\d]+")
    nCrates = int(nCratesPat.search(rule).group())
    return (nCrates, targetStack - 1, destStack - 1)

for rule in guide:
    n, start, dest = interpret_rule(rule)
    ind, crate = get_top_box(stacks[start])
    movingCrates = stacks[start][ind:ind + n]
    # update the remaining stack
    stacks[start] = stacks[start][ind + n: len(stacks[start]) + 1]
    # get the top crate for the destination stack
    ind2, crate2 = get_top_box(stacks[dest])
    for box in movingCrates:
        stacks[dest].insert(ind2, box)

solution = []
for stack in stacks:
    n, topBox = get_top_box(stack)
    solution.append(topBox)

print(
    f"The top crates are {''.join(solution).replace('[', '').replace(']', '')}."
    )

# Part 1

