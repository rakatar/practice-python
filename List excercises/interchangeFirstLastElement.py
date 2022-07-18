
# swap function
def swapList(newList):
    size = (len(newList))
    #swap
    temp = newList[0]
    newList[0] = newList [size-1]
    newList [size-1] = temp
    return (newList) 
# driver code
newList = [1,2,3,4]
print (swapList(newList))

