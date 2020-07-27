class stack(): #This program is for deleting middle element in given stack
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]
    
    def prints(self): 
        for i in range(len(self.items)-1, -1, -1): 
            print(self.items[i], end = ' ')


def delete(st,n,curr): # for deleting middle values
    if (st.isEmpty() or curr == n):
        return
    
    p = st.peek()
    st.pop()
    delete(st,n,curr+1) 

    if (curr!= int(n/2)):
        st.push(p)
    
st = stack()


st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)

delete(st,st.size(),0)

while (st.isEmpty() == False):
    k = st.peek()
    st.pop()
    print (str(k) + " ", end="")



# print(st.prints()) #or we can use print the entire stack