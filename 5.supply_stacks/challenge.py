import os
from pyprojroot import here

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


def get_top_box(stack=stacks[0]):
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
