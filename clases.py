'''
moke list of students an show all of the students 
'''



class Student:
    def __init__(self,f_name,l_name,age,instructore,stack):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.instructore = instructore
        self.stack = stack


    def display_student_info(self):
        print("Student name",self.f_name,self.l_name)
        print("Studetn age",self.age)
        print("student instructore",self.instructore)
        print("Students stack",self.stack)

Lenddy = Student("Lenddy","Morales",18,"Alfredo","python")
student_list = []

student_list.append(Lenddy)

for item in student_list:
    item.display_student_info()




class User :
    def __init__(self,f_name = "NA",l_name = "NA",age="NA",email = "NA"):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.age = age

    def disply_info(self):
        print("your name",self.f_name,self.l_name)
        print("age",self.age)
        print("email",self.email)

user= User("Lenddy","morales",18,)
user.disply_info()



class User :
    def __init__(self,f_name = "NA",l_name = "NA",age="NA",email = "NA",balance = 0):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.age = age
        self.balance = balance

    def disply_info(self):
        print("your name",self.f_name,self.l_name)
        print("age",self.age)
        print("email",self.email)


    def make_deposit(self,amount):
        curent_balance = self.balance
        new_balance = curent_balance + amount
        self.balance = new_balance
    
    def display_user_account(self):
        print("your balance is  ",self.balance)

user= User("Lenddy","morales",18,)
user.disply_info()
user.make_deposit(1)
user.display_user_account()













class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)



kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.display_info()) # prints small forward
