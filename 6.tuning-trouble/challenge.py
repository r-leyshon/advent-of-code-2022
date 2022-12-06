from pyprojroot import here
import os
# Day 6 - https://adventofcode.com/2022/day/6
with open(os.path.join(here(), "data", "6.signal.txt"), "r") as f:
    txt = f.read()
    f.close()

# part 1
# How many characters need to be processed before the first start-of-packet marker is
# detected?
for ind, char in enumerate(txt):
    # search for unique combos of 4 digits
    if ind > 2:
        pat = txt[ind-3:ind+1]
        if len(set(pat)) == 4:
            print(f"Start of packet marker is {pat}")
            print(f"{ind + 1} characters were processed.")
            break
        else:
            continue
            
        
