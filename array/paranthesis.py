def parn(a):   #dought
    s = []
    for i in range(len(a)):
        if a[i]=='{ 'or a[i]=='[' or a[i]=='(':
            s.append(a[i])
            continue

        if len(a)==0:
            return False
        
        if a[i] ==')':
            x = s.pop()
            if x == '{' or x =='[':
                return False

        elif a[i]==']':
            x = s.pop()
            if x == '{' or x =='(':
                return False

        elif  a[i] =='}':
            x = s.pop()
            if x == '(' or x == '[' :
                return False
        
    if len(a) ==0:
        return False
    else:
        return True

if __name__ == "__main__" :  
  
    expr = "{()}[]";  
    # k = parn(expr)

    if (parn(expr)) : 
        print("Balanced") 
    else : 
        print("Not Balanced")
        



        
