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

    def delete(self,position):
        currentposition = 0
        currentNode = self.head
        while True:
            if currentposition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            else:   
                previousNode = currentNode
                currentNode = currentNode.next
                currentposition+=1


    def sortedduplicate(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data: #while comparing value we should compare with data
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

    def unsortedduplicate(self):
        start = self.head
        while start.next is not None: #loop running till end
            temp = start
            while temp.next is not None:
                if start.data ==temp.next.data:  #1.start = 1;2.start = 2; where numbers are positions of pointer
                    new = temp.next.next
                    temp.next =None
                    temp.next = new
                else:
                    temp = temp.next
            start = start.next

    def oddeven(self):
        temp = self.head
        while True:
            if temp.data %2 ==0:
                break
            temp = temp.next

        print(temp.data)
      


    def reverse(self):
        prev =None
        current = self.head
        while current is not None:
            next = current.next #next is pointer points to next
            current.next = prev #pionts ton previous value
            prev = current #previous value is stored in current value
            current = next #both current and prev pointer will move 
        self.head = prev  #not prev =self.head 

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

    def detectLoop(self):
        s = set()
        temp = self.head

        while temp is not None:
            while temp in s:
                return True

                s.add(temp)
                temp = temp.next
            return False

    def swap(self):
        start = self.head # storing
        previousNode = start
        start = start.next
        dum = start
        previousNode.next = start.next
        # dum = start
        start.next = None
        self.head = dum
        self.head.next = previousNode
        
        current  = self.head

       





                    
                

                
    




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

            
# linkedList.unsortedduplicate()
# linkedList.oddeven()
# linkedList.reverse()
# k = linkedList.sortedduplicate()
# linkedList.FromLastNode(8)
# print(linkedList.detectLoop())
linkedList.swap(2)
linkedList.printList()

# print(k)

