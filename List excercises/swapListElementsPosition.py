#swap function
def swapPositions (list, pos1, pos2):

 list[pos1], list[pos2] = list[pos2], list[pos1]

 return list

#driver function
list = [10,12,13,14,15]
pos1, pos2 = 1, 3

print (swapPositions (list, pos1-1, pos2-1))

print (list[0])
