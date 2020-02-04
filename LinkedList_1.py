class Node:
    def __init__(self,data):
        self.data =data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head = None

    def LinkedLength(self):
        currentNode = self.head
        currentPosition = 0
        if currentNode is None:
            print("list is empty")
        while True:
            if currentNode.next is None:
                break
            currentPosition+=1
            currentNode = currentNode.next
        return int(currentPosition*0.5)

    def linkedlength(self):
        length =0
        currentNode = self.head
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        return length

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


    # def printMiddle(self):
    #     currentNode = self.head
    #     if currentNode is None:
    #         print("empty")
    #         return
        
    #     while True:
    #         if currentNode.next is None:
    #             break

    #         if currentPosition == self.LinkedLength():
    #             print(currentNode.data)#present value
    #             break
    #         currentPosition+=1
    #         currentNode = currentNode.next

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        currentPosition = 0
        currentNode = self.head
        while True:
            if currentNode is None: #if it reaches end it will break
                break
            
            if currentPosition == self.LinkedLength():
                print(currentNode.data)#present value
            currentPosition+=1
            currentNode = currentNode.next #increment

linkedList = LinkedList()

firstNode =Node('john')
linkedList.insert(firstNode)

secondNode =Node('ram')
linkedList.insert(secondNode)

thirdNode =Node('rishi')
linkedList.insert(thirdNode)

fourthNode = Node('v')
linkedList.insert(fourthNode)

fiveNode = Node('virinchi')
linkedList.insert(fiveNode)

# linkedList.insert(fourthNode)
# startNode = Node('boom')

linkedList.LinkedLength()
linkedList.printList()