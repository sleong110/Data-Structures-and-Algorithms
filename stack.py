class stack:
    """Stack is a data structure where items can be added to and removed in
       a LIFO manner.
    
    Attributes:
        items: Any primitive data types that can be added into the stack.
    """
    def __init__(self):
        """Initialize stack as a list."""
        self.items = []
    def isEmpty(self):
        """Return a boolean to determine if the stack is empty."""
        return self.items == []
    def size(self):
        """Return size of the stack."""
        return len(self.items)
    def push(self, item):
        """Push item at the rear of the stack."""
        self.items.append(item)
    def pop(self):
        """Return the last item removed from the stack."""
        return self.items.pop()
    def peek(self):
        """Return the size of the stack."""
        return self.items[len(self.items)-1]
    