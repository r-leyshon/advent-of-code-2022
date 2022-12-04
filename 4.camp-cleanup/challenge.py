import os
from pyprojroot import here
# read
with open(os.path.join(here(), "data", "4.cleanup.txt")) as f:
    txt = f.read()
    f.close()
# process
pairs = txt.splitlines()
elves = [elf.split(",") for elf in pairs]

def get_zones(zoneString="3-5"):
    start_stop = zoneString.split("-")
    start_stop = [int(num) for num in start_stop]
    zones = range(start_stop[0], start_stop[-1] + 1)
    return zones
