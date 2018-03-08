class deque:
    """Deque is a data structure that items can be added and removed from 
       either end.
    
    Attributes:
        items: Any primitive data type that can be added into deque.
    """
    def __init__(self):
        """Initialize deque as empty list"""
        self.items = []
    def __str__(self):
        """Return string format of the deque."""
        return str(self.items)
    def addFront(self, item):
        """Add item at the front of the deque."""
        self.items.append(item)
    def addRear(self, item):
        """Add item at the back of the deque."""
        self.items.insert(0,item)
    def removeFront(self):
        """Return the item removed from the front of deque."""
        return self.items.pop()
    def removeRear(self):
        """Return the time removed from the rear of deque."""
        return self.items.pop(0)
    def isEmpty(self):
        """Return boolean value to determine if the deque is empty."""
        return self.items == []
    def size(self):
        """Return the length of deque."""
        return len(self.items)
    