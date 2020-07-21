# HASHING CHAIN HASHING (PAIR_CHAIN_HASHING) USING CLASS


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def hashing(self,key):
        k = 0
        for char in key:
            k += ord(char)
        return k % self.MAX
    
    def add(self,key,value):
        h = self.hashing(key)
        self.arr[h] = value

    def ladd(self,key,value):
        h = self.hashing(key)
        found = False
        for idx , element in enumerate(self.arr[h]):
            print(element)
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break

        if not found:
            self.arr[h].append((key,value))
    

    
    def get_element(self,key):
        h = self.hashing(key)
        if self.arr[h]:
            return self.arr[h]
        else:
            return "not found"

    def lget(self,key):
        h = self.hashing(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def do_del(self,key):
        h = self.hashing(key)
        self.arr[h] = None

    def l_del(self,key):
        h = self.hashing(key)
        if self.arr[h] is 0:
            return "not an element"
        
        for index,element in enumerate(self.arr[h]):
            if element[0]== key:
                del self.arr[h][index]




method = "linkedlist"
t = HashTable()
#conversion of a string to asci value .
print(t.hashing("march 17"))

details = ["march 6","march 6", "march 8", "march 9"," march 10"]
if  method == "linkedlist":
    for i in details:
        print("enter {} value:".format(i) )
        t.ladd(i,int(input()))






print(t.arr)
t.l_del("march 6")
print(t.lget("march 6"))




















