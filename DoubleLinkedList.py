class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def addingNone(self,newNode):
        # currentNodeH = self.head
        # currentNodeT = self.tail

        if self.head is None:
            self.head = self.tail = newNode
            self.head.next = None
            self.tail.next = None

        else:
            self.tail.next = newNode
            newNode.previous = self.tail 
            self.tail = newNode #points to newNode
            self.tail.next = None

    def print(self):
        

        if self.head is None:
            print("list is empty")
        
        currentvalue = self.head
        while currentvalue is not None:
            print(currentvalue.data)
            currentvalue = currentvalue.next



dl = DoubleLinkedList()
firstnode = Node("apple")
dl.addingNone(firstnode)
secondNone = Node("bananna")
dl.addingNone(secondNone)


dl.print()

