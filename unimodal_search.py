def unimodal_search(mylist, left=0, right=None):
    """Accepts any list of numbers such that the sequence increases until it reaches
    element k and then decreases after. Returns index of the desired element. If
    list is empty, returns -1. Works for Monotone sequences, increasing or decreasing.
    """
    #set initial variables
    if right is None:
        right = len(mylist) - 1
    midpoint = (left + right) // 2

    #Failed search entire list
    if left > right:
        return -1

    #Check end conditions
    try:
        if mylist[midpoint + 1] == None or mylist[midpoint - 1] == None:
            return midpoint
    except IndexError:
        return midpoint

    #if found the target in the list
    if mylist[midpoint] > mylist[midpoint - 1] and mylist[midpoint] > mylist[midpoint + 1]:
        return midpoint

    #Search the left half of the list
    elif mylist[midpoint] < mylist[midpoint - 1]:
        return unimodal_search(mylist, left, midpoint-1)

    #Search the right half of the list
    else:
        return unimodal_search(mylist, midpoint+1, right)

#Lists to test with
L = [1,2,3,4,5,6,7,6,5,4,3,2,1]  #normal
S = [1,2,3,4,5]                  #Rightmost answer
T = [5,4,3,2,1]                  #Leftmost answer
