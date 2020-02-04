class Node:
    def __init__(self,data):
        self.data =data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head = None


    def isListEmpty(self):
        if self.head is None:
            print("list is empty")
            return True
        else:
            return False


    def insertAt(self,newNode,position):
        if position < 0 or position> self.linkedlength():
            print("invalid position")
            return
        
        if position is 0:
            self.insertatstart(newNode)
            return
        currentNode = self.head
        currentPosition = 0 #1

        while True:
            if currentPosition == position:
                previousNode.next = newNode#15
                newNode.next = currentNode#20
                break

            previousNode = currentNode #10
            currentNode = currentNode.next#20
            currentPosition +=1




    def insert(self,newNode):
        if self.head is None:
            #head => john =>points to None
            self.head = newNode
        else:
            lastNode = self.head # to start from beggining 
            while True:# loop runs untill it finds last element
                if lastNode.next is None: #means linked list is at end then i will breeak
                    break
                lastNode = lastNode.next # increment lastnone value for checking(here it is second value (ram))
            lastNode.next = newNode #last value
   
   
    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None: #if it reaches end it will break
                break
            print(currentNode.data)#present value
            currentNode = currentNode.next #increment


    def linkedlength(self):
        length =0
        currentNode = self.head
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        return length



#Node =>data , next
#firstNode.data = data ,firstnode.next= None
firstNode =Node('john')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode =Node('ram')
linkedList.insert(secondNode)
thirdNode =Node('rishi')
linkedList.insert(thirdNode)
fourthNode = Node('virinchi')
linkedList.insert(fourthNode)
startNode = Node('boom')


middleNode = Node(000)
linkedList.insertAt(middleNode,2)
linkedList.printList()
