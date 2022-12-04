import os
from pyprojroot import here
# https://adventofcode.com/2022/day/4
# In how many assignment pairs does one range fully contain the other?
# read
with open(os.path.join(here(), "data", "4.cleanup.txt")) as f:
    txt = f.read()
    f.close()
# process
pairs = txt.splitlines()
elves = [elf.split(",") for elf in pairs]


def get_zones(zoneString):
    """Return all zones for a zonestring. Eg - '2-3' -> [2,3]

    Args:
        zoneString (str): String representation of all zones to cover.

    Returns:
        list: Inclusive integer zones.
    """
    start_stop = zoneString.split("-")
    start_stop = [int(num) for num in start_stop]
    zones = range(start_stop[0], start_stop[-1] + 1)
    return zones


# get those zones
elfZones = list()
for pair in elves:
    pairZones = list()
    for elf in pair:
        pairZones.append(get_zones(elf))
    elfZones.append(pairZones)

# compare
is_contained = list()
for pair in elfZones:
    pairLimits = list()
    for zones in pair:
        first = zones[0]
        last = zones[-1]
        firstlast = tuple([first, last])
        pairLimits.append(firstlast)
    
    if pairLimits[0][0] >= pairLimits[-1][0] and pairLimits[0][-1] <= pairLimits[-1][-1]:
        print("hit1")
        is_contained.append(1)
    elif pairLimits[-1][0] >= pairLimits[0][0] and pairLimits[-1][-1] <= pairLimits[0][-1]:
        print("hit2")
        is_contained.append(1)
    
    else:
        print("miss")
        is_contained.append(0)

sum(is_contained)

# Part 2
# Instead, the Elves would like to know the number of pairs that overlap at all.



