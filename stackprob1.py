class stack(object):
    
    def __init__(self):
        self.items =[]
        self.box =[]


    def push(self,item):
        self.box.append(item)


    def pop(self):
        self.items.pop()


    def peak(self):
        if self.items:
            return self.items[-1]
        else:
            return  None


    def size(self):
        if self.items:
            return len(self.items +1)
        else:
            return None


    def Isempty(self):
        if self.items == []:
            return True
        else:
            return False


    def functions(self):
        for i in range(len(self.items),-1,-1,-1):
            print(self.items[i], end ='')


    #  def func(self):
    #      for i in range(self.items,-1,-1,-1):
              

if __name__=="__main__":
    stac = stack()
    

    a =int(input("enter ln " ))
    stac.push(a)
    
    b = int(input("enter lbn " ))
    stac.push(b)
    
    c = int(input("enter thrdnum "))
    stac.push(c)

    d = int(input("enter fourthnum "))
    stac.push(d)


    # k=print(stack.size())

    print(stac.functions())
    # for i in range(1):
    #     l =print(stac.pop())
    #     stac.push(l)
    #     l = None
            
        


        

        