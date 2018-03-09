class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def getData(self):
        return self.data
    def getNextext(self):
        return self.next
        
class OrderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return current
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop: 
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def index(self, item):
        current = self.head
        found = False
        count = 0
        index = None
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count = count + 1
        if found == True:
            index = count
            return index
        else:
            print('Item not found')
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def pop(self):
        current = self.head
        previous = None
        count = 0
        while current.getNext() != None:
            count = count + 1
            previous = current
            current = current.getNext()
        data = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return data    
