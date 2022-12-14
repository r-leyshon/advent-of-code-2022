import os
from pyprojroot import here
import numpy as np

# import data
with open(os.path.join(here(), "data", "8.trees.txt"), "r") as f:
    txt = f.read()
    f.close()
txt = txt.splitlines()

trees = []
for row in txt:
    trees.append([int(i) for i in row])


trees = np.asarray(trees)
# int conversion will drop zeroes at start of line, do this one at a time
# part 1
# Consider your map; how many trees are visible from outside the grid?


def is_visible(tree, ind, stand):
    """Is the tree visible among its neighbours.

    Args:
        tree (int): Height value of the tree.
        ind (int): Index of the tree in the stand.
        stand (numpy.ndarray): Array containing height integers of trees.

    Returns:
        bool: True if the tree is visible.
    """
    comps = [tree > x for i, x in enumerate(stand, start=1) ]
    # subset comparisons but omit the tree that is the current ind
    side1 = comps[0:ind]
    side2 = comps[ind+1:len(stand)]
    isViz = False
    if ind == 0:
        isViz = True
    elif ind == len(stand)-1:
        isViz = True
    else:
        if all(side1):
            isViz = True
        elif all(side2):
            isViz = True
    
    return isViz
        

allRows = list()
for stand in trees:
    rowViz = []
    for ind, tree in enumerate(stand):
        rowViz.append(is_visible(tree, ind, stand))
    allRows.append(rowViz)

allCols = list()    
for stand in trees.T:
    colViz = []
    for ind, tree in enumerate(stand):
        colViz.append(is_visible(tree, ind, stand))
    allCols.append(colViz)
    
x = np.asarray(allRows)
y = np.asarray(allCols).T

print(f"There are {sum(sum(x + y))} visible trees.")

# Part 2: Consider each tree on your map. What is the highest scenic score
# possible for any tree?


def scenic_score(tree, ind, stand):
    """Calculate the scenic score of a tree.

    Args:
        tree (int): Height value of the tree.
        ind (int): Index of the tree in the stand.
        stand (numpy.ndarray): Array containing height integers of trees.

    Returns:
        int: Product of the score from both views in a stand.
    """
    comps = [tree <= x for i, x in enumerate(stand)]
    # subset comparisons but omit the tree that is the current ind
    side1 = comps[0:ind]
    side2 = comps[ind+1:len(stand)]

    if ind == 0:
        leftScore = 0
    elif all(item == False for item in side1):
        leftScore = len(side1)
    else:
        viewL = [i for i, x in enumerate(np.flip(side1)) if x]
        # Add 1 because the blocking tree is also visible
        leftScore = viewL[0] + 1
    
    if len(side2) == 0:
        rightScore = 0
    elif all(item == False for item in side2):
        rightScore = len(side2)
    else:
        # if index is neg, return 0
        rightScore = max(side2.index(True) + 1, 0)
    
    return leftScore * rightScore


rowScores = []
for stand in trees:
    rowScore = []
    for ind, tree in enumerate(stand):
        rowScore.append(scenic_score(tree, ind, stand))
    rowScores.append(rowScore)

colScores = []
for stand in trees.T:
    colScore = []
    for ind, tree in enumerate(stand):
        colScore.append(scenic_score(tree, ind, stand))
    colScores.append(colScore)

x = np.asarray(rowScores)
y = np.asarray(colScores).T
z = x * y
maxes = list()
for r in z:
    maxes.append(max(r))

print(f"The highest scenic score is {max(maxes)}.s")
