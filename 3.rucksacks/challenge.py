import os
from pyprojroot import here

# https://adventofcode.com/2022/day/3

with open(os.path.join(here(), "data", "3.rucksacks.txt"), "r") as f:
    txt = f.read()
    f.close()

sacks = txt.splitlines()

dupeVals = []
for sack in sacks:
    # split the sack into 2 compartments
    n = len(sack)
    divider = int(n/2)
    c1 = sack[0:divider]
    c2 = sack[divider:n]
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    # check for item occurences between compartments
    c1unique = list(set(c1))
    c2unique = list(set(c2))
    dupes = []
    for item in c1unique:
        if item in c2unique:
            print(f"{item} is a dupe!!")
            dupe = item
            dupes.append(dupe)
    print(f"All dupes: {dupes}")
    # get ascii value and convert to elf score
    for dup in dupes:
        dupeVal = ord(dup)
        print(f"ascii: {dupeVal}")
        # handle case letters
        if dupeVal < 91:
            # UPPERCASE
            elfScore = dupeVal - 38
        elif dupeVal > 90:
            # lowercase
            elfScore = dupeVal - 96
        dupeVals.append(elfScore)

print(f"the sum of all the misplaced item scores is {sum(dupeVals):,}.")
        
