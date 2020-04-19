class Node: # display Nth node from end
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


    def insert(self,newNode):
        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head
            while True:
                if lastNode.next is None :
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

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

    def length(self):
        start = self.head
        count = 0
        while True:
            if start.next is not None:
                count = count +1
                start = start.next
            else:
                return count

    def FromLastNode(self,position):

        currretposition = 0
        current = self.head
        l = self.length()
        if position > l:
            print("syntax error please enter within linkedlist")
            return
        
        last =( l -position +1)
        while True:
            if currretposition == last:
                print(current.data)
                break
            
            current = current.next
            currretposition +=1


linkedList = LinkedList()
firstNode =Node(1)
linkedList.insert(firstNode)
secondNode =Node(2)
linkedList.insert(secondNode)
thirdNode =Node(3)
linkedList.insert(thirdNode)
fourthNode = Node(45)
linkedList.insert(fourthNode)
fifthnode = Node(8)
linkedList.insert(fifthnode)



linkedList.FromLastNode(8)
linkedList.printList()