def insertAtBottom(stack, item): 
    if isEmpty(stack): 
        push(stack, item) 
    else: 
        temp = pop(stack) 
        insertAtBottom(stack, item) 
        push(stack, temp)

def reverse(stack): 
    if not isEmpty(stack): 
        temp = pop(stack) 
        reverse(stack) 
        insertAtBottom(stack, temp)


def createStack(): 
    stack = [] 
    return stack

def isEmpty( stack ): 
    return len(stack) == 0
    
def push( stack, item ): 
    stack.append( item )

def pop( stack ): 
  
    # If stack is empty 
    # then error 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 




def prints(self): 
    for i in range(len(self.items)-1, -1, -1): 
        print(self.items[i], end = ' ')

