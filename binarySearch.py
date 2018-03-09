def binarySearch(alist, item):
     """Perform binary search for a data sequence.
    Binary Search starts off with comparing the item in the middle with the 
    target. 
    If the searched item is bigger than the target item, the second half of
    the sequence will be discarded.
    If the searched item is smaller than the target item, the first half of 
    the sequence will be discarded.
    """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found 
    
