import datetime
class User: 
    pass    #at least one line has to to written

user1 = User()
user1.firstname = "one"
user1.secondname ="second"

user2 = User()
user2.firstname = "three"
user2.secondname = "four"

print(user1.firstname,user1.secondname)
print(user2.firstname,user2.secondname) #each obj has individual attributes

class Test:
    def __init__(self, var1,var2):
        self.first_value = var1
        self.second_value = var2

obj = Test(1,2)
print(obj.first_value)

