def createstack():
    stack = []
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
    
def prints(stack): #dought
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print()

stack = createstack()
push(stack,int(1))
push(stack,int(2))
push(stack,int(3))
push(stack,int(4))

stack_a = createstack()
def sort(stack):
    # stack_a = createstack()
    while isEmpty(stack) == False:
        temp = top(stack)
        pop(stack)
        push(stack_a,temp)
    return stack_a



def sortable_or(stack_a):
        for i in range(len(stack_a)-1, -1, -1):
            if stack_a[i]>stack_a[i-1]:
                return False
        return True

print("original stack is:")    
prints(stack)

print("reverse stack is:")
k =sort(stack)
prints(k)

l =sortable_or(stack_a)
print(l)