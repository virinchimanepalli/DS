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


    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None





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


    def deleteAtmiddle(self,position):
        if position < 0 or position >  self.linkedlength():
            print("invalid position")
            return
        # if self.linkedlength is not 0:
        #     self.deletehe
        currentNode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentposition+=1



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



linkedList.deleteAtmiddle(1)
# linkedList.deleteEnd()
linkedList.printList()
