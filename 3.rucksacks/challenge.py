import os
from pyprojroot import here

# https://adventofcode.com/2022/day/3

with open(os.path.join(here(), "data", "3.rucksacks.txt"), "r") as f:
    txt = f.read()
    f.close()

sacks = txt.splitlines()

# part 1

def elfPriority(letter):
    """Return the elf priority score for any upper or lowercase letter.

    Args:
        letter (str): A-Za-z

    Returns:
        int: The priority score of the item type.
    """
    # get ascii value and convert to elf score
    dupeVal = ord(letter)
    # handle case letters
    if dupeVal < 91:
        # UPPERCASE
        elfScore = dupeVal - 38
    elif dupeVal > 90:
        # lowercase
        elfScore = dupeVal - 96
    return elfScore


dupeVals = []
for sack in sacks:
    # split the sack into 2 compartments
    n = len(sack)
    divider = int(n/2)
    c1 = sack[0:divider]
    c2 = sack[divider:n]
    # check for item occurences between compartments
    c1unique = list(set(c1))
    c2unique = list(set(c2))
    dupes = []
    for item in c1unique:
        if item in c2unique:
            dupe = item
            dupes.append(dupe)
    # get ascii value and convert to elf score
    for dup in dupes:
        elfScore = elfPriority(dup)
        dupeVals.append(elfScore)

print(f"the sum of all the misplaced item scores is {sum(dupeVals):,}.")

# part 2
# get all the elf trios
        
count = 0
badgeVals = []
for entry in range(0, len(sacks) + 1):
    if (count % 3) != 0:
        pass
    elif count == 0:
        pass
    else:
        startInd = count - 3
        team = sacks[startInd:count]
        # get the unique items in each rucksack
        teamUnique = []
        for sack in team:
            teamUnique.append("".join(set(sack)))
        # find the badges
        for item in teamUnique[0]:
            if item in teamUnique[1] and item in teamUnique[2]:
                badge = item
                badgeVal = elfPriority(badge)
                badgeVals.append(badgeVal)
    count += 1

print(f"the sum of all the elves' badge values is {sum(badgeVals):,}")
