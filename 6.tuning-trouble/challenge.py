from pyprojroot import here
import os
# Day 6 - https://adventofcode.com/2022/day/6
with open(os.path.join(here(), "data", "6.signal.txt"), "r") as f:
    txt = f.read()
    f.close()
# part 1
# How many characters need to be processed before the first start-of-packet marker is
# detected?


def get_n_processed(txt=txt, seqLen=4):
    """Return n characters processed in sequence to reach a unique set of seqLen length.

    Args:
        txt (str, optional): Sequence of characters. Defaults to txt.
        seqLen (int, optional): The unique sequence length. Defaults to 4.
    """
    for ind, char in enumerate(txt):
        pat = txt[ind - (seqLen - 1):ind + 1]
        if len(set(pat)) == seqLen:
            return(ind + 1)
        else:
            continue


print(f"Characters processed: {get_n_processed()}")
# part 2
# Change seqLen to 14
print(f"Characters processed: {get_n_processed(seqLen=14)}")
