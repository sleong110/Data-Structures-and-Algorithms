class deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addRear(self, item):
        self.items.insert(0, item)
    def addFront(self, item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop(0)
    def removeFront(self):
        return self.items.pop()
        
def isPalindrome(aString):
    chardeque = deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
    
        
    