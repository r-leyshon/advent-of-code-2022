import os
from pyprojroot import here
# https://adventofcode.com/2022/day/1
# Part 1 - find the value of the most calories carried
# import
with open(os.path.join(here(), "data", "1.calories.txt"), "r") as f:
    dat = f.read()
    f.close()
# process
elves = dat.split("\n\n")
calsCarried = list()
for elf in elves:
    elfCarries = elf.split("\n")
    calInts = []
    for food in elfCarries:
        calInts.append(int(food))
    calsCarried.append(sum(calInts))
# summarise
most = max(calsCarried)
whichMost = calsCarried.index(most)
# outputs
print(f"Elf number {whichMost} carried a total of {most:,} calories.")

# Part 2 - find calorie total for the top 3 elves
n1 = calsCarried.pop(calsCarried.index(max(calsCarried)))
n2 = calsCarried.pop(calsCarried.index(max(calsCarried)))
n3 = calsCarried.pop(calsCarried.index(max(calsCarried)))
print(f"The 3 elves with the most calories carry a total of {n1+n2+n3:,} calories")

