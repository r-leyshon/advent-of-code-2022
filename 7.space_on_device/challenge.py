import os
from pyprojroot import here
import tempfile

with open(os.path.join(here(), "data", "7.fileOps.txt"), "r") as f:
    txt = f.read()
    f.close()
fileOps = txt.splitlines()
# Part 1
# Find all of the directories with a total size of at most 100000. What is the sum of
# the total sizes of those directories?
dirKey = str()
curwd = here()
tmp = tempfile.TemporaryDirectory(dir=curwd)

for ind, op in enumerate(fileOps):
    print(f"Line {ind}: {op}")
    if op.startswith("$"):
        if "$ cd /" in op:
            os.chdir(tmp.name)
            targetDir = tmp.name
        elif "$ cd " in op:
            targetDir = op.split(" ")[-1]
            dirKey = targetDir
            os.chdir(targetDir)
    elif op.startswith("dir"):
        target = os.path.join(os.getcwd(), op.split(" ")[-1])
        print(f"Creating directory {target}")
        os.mkdir(target)
    else:
        size, filenm = op.split(" ")
        target = os.path.join(os.getcwd(), filenm)
        print(f"Write file to {target}")
        f = open(target, "w")
        f.write(size)
        f.close()

# go back to pyprojroot
os.chdir(curwd)


def sum_file_size(directory):
    """Recursively reads files in a directory and sums the integers in
    contents.

    Args:
        directory (path): Path to the directory.

    Returns:
        int: Sum of the found integers.
    """
    sizes = list()
    for root, dirs, files in os.walk(directory):
        for name in files:
            with open(os.path.join(root, name), "r") as f:
                size = int(f.read())
                sizes.append(size)
                f.close()
    return sum(sizes)


smaller_100k = list()
# get all the available directories
for root, dirs, files in os.walk(tmp.name):
    for dir in dirs:
        tot = sum_file_size(os.path.join(root, dir))
        if tot <= 100000:
            smaller_100k.append(tot)

print(f"The sum of the folders with size at most 100k: {sum(smaller_100k)}")

# part 2
# Find the smallest directory that, if deleted, would free up enough space on the
# filesystem to run the update. What is the total size of that directory?
filesystem = 70000000
required = 30000000
used = sum_file_size(tmp.name)
free_up = abs(filesystem - required - used)
qual_free_up = []
for root, dirs, files in os.walk(tmp.name):
    for dir in dirs:
        tot = sum_file_size(os.path.join(root, dir))
        if tot > free_up:
            qual_free_up.append(tot)
print(f"The size of the smallest folder to delete is {min(qual_free_up)}")
tmp.cleanup()
