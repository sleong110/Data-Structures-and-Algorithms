class queue:
    """A queue is a data structure that orders a collections of items in 
       FIFO manner.
    
    Attributes:
        items: A collections of primitive data that can be either integer,
               float and string.
    """
    def __init__(self):
        """Initialize an empty list that represents a queue."""
        self.items = []
    def isEmpty(self):
        """Return a boolean value that shows if the queue is empty."""
        return self.items == []
    def size(self):
        """Return the length of the queue."""
        return len(self.items) - 1
    def enqueue(self, item):
        """Append an item into the queue."""
        self.items.append(item)
    def dequeue(self):
        """Remove first item from the queue."""
        return self.items.pop(0)
    def __str__(self):
        """Return a string formatted queue."""
        return str(self.items)