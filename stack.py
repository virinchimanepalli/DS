class stack(object):

    def __init__(self):
         self.items =[]
         self.box =[]

    
    def push(self,item):
        self.items.append(item)



    def pushed(self,boxx):
        self.box.append(boxx)

    def pop(self):
        k = self.items.pop()
        print(k)
        pass
    
    def peak(self):
        if self.items :
            return self.items[-1]
        else:
            return None
    
    def size(self):
        if self.items:
            return (len(self.items)+1)
        else:
            return None

    def isempty(self):
        if self.items == []:
            return True
        else:
            return False

    def prints(self): 
        for i in range(len(self.items)-1, -1, -1): 
            print(self.items[i], end = ' ') 

    def printed(self):
        for i in range(len(self.box)-1,-1,-1):
            print(self.box[i],end='')
        

if __name__ == "__main__":
    stack =stack()
   
    a =int(input("enter ln " ))
    stack.push(a)
    
    b = int(input("enter lbn " ))
    stack.push(b)
   
    c = int(input("enter thrdnum "))
    stack.push(c)

    d = int(input("enter fourthnum "))
    stack.push(d)

    # print(stack.prints())


    # for i in range(4):
    #     k = stack.pushed(stack.pop())

    # print(stack.printed())
        



   
   
   
  
    k =int(stack.pop())       
    print(k)         #pop always returns none after it removes
   
    # print(stack.size())
    
   

     
    # print(stack.peak())
    # print(stack.isempty()) #returns true or false 

    

    

    
    
  
    


    

    

    