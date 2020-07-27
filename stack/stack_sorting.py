def createstack():
    stack =[]
    return stack

def isEmpty(stack):
    return len(stack) ==0

def push(stack,item):
    stack.append(item)

def top(stack):
    p = len(stack)
    return stack[p-1] # p-1 is due to out of range

def pop(stack):
    if isEmpty(stack):
        print("stack is empty")
        # exit(1)
    else:
        return stack.pop()
    
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
    

stack = createstack()
push( stack, int(34) ) 
push( stack, int(3) ) 
push( stack, int(31) ) 
push( stack, int(98) ) 
push( stack, int(92) ) 
push( stack, int(23) )

def sort_stack(stack):
    tempstack = createstack()
    while(isEmpty(stack)== False):
        temp = top(stack)
        pop(stack) # we can peek inplace of top
        while isEmpty(tempstack) == False and int(top(tempstack))> int(temp): # temp ntng but top eklement in stack
            push(stack,top(tempstack))
            pop(tempstack)

        push(tempstack,temp)
    return tempstack        

lk =sort_stack(stack)
prints(lk)
    
    



