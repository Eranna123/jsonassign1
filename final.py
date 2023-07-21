# # 1. Assignment on employee details-------------------------------------------------------------------- 



# import json
# class Employee:
#     def __init__(self, name, dob, height, city, state):
#         self.name = name
#         self.dob = dob
#         self.height = height
#         self.city = city
#         self.state = state

# employees_data = [
#     {
#         "Name": "kumar",
#         "DOB": "2001-06-26",
#         "Height": 175,
#         "City": "haveri",
#         "State": "karnataka"
#     },
#     {
#         "Name": "eranna",
#         "DOB": "1998-05-07",
#         "Height": 173,
#         "City": "bengaluru",
#         "State": "karnataka"
#     },
#     {
#         "Name": "aruna",
#         "DOB": "1998-03-04",
#         "Height": 161,
#         "City": "hubli",
#         "State": "karnataka"
#     },
#     {
#         "Name": "sandhya",
#         "DOB": "1988-11-30",
#         "Height": 165,
#         "City": "Goa",
#         "State": "Goa"
#     },
#     {
#         "Name": "monika",
#         "DOB": "1998-08-03",
#         "Height": 146,
#         "City": "mysore",
#         "State": "karnataka"
#     }
# ]

# with open('C:/Users/EMC/Desktop/employee_mine.json', 'w') as json_file:
#     json.dump(employees_data, json_file)

# employees = []

# with open('C:/Users/EMC/Desktop/employee_mine.json', 'r') as json_file:
#     employees_data = json.load(json_file)
    
#     for employee_data in employees_data:
#         name = employee_data['Name']
#         dob = employee_data['DOB']
#         height = employee_data['Height']
#         city = employee_data['City']
#         state = employee_data['State']
        
#         employee = Employee(name, dob, height, city, state)
#         employees.append(employee)

# for employee in employees:
#     print(employee._dict_)



# #   json file on creation of states and capitals---------------------------------------------------------


# states = []
# capitals = []
# print("\nWe are going to know 7 States and their Capitals!")
# for i in range(7):
#     state = input("Enter State Name: ")
#     capital = input("Enter capital of %s :"%(state))

#     states.append(state)
#     capitals.append(capital)

# print("\nList of states: ", states)
# print("List of capital: ", capitals)

# state_capital_dict = {}

# for key in states:
#     for value in capitals:
#         state_capital_dict[key] = value
#         capitals.remove(value)
#         break

# print("\nDictionary formate of States and their Capital:")
# print(state_capital_dict)

# import json

# with open("C:/Users/EMC/Desktop/State.json" , 'w') as file:
#     json.dump(state_capital_dict,file, indent=3)

# print("\n")
# print(json.dumps(state_capital_dict, indent=4))



# # 2.  .Assignment on creation of dog class----------------------------------------------------------------------------


# class Dog:
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color

#     def description(self):
#         print("Name of Dog: ",self.name)
#         print("Age of Dog: ", self.age)

#     def get_info(self):
#         return self.coat_color
    
# class JackRussellTerrier(Dog):
#     def __init__(self, name, age, coat_color):
#         Dog.__init__(self, name, age, coat_color)

#     def details(self):
#         print("Name: {}".format(self.name))
#         print("Age: {} years".format(self.age))
#         print("Coat Color: {}".format(self.coat_color))

# class Bulldog(Dog):
#     def __init__(self, name, age, coat_color):
#         Dog.__init__(self, name, age, coat_color)
    
#     def details(self):
#         print("Name: {}".format(self.name))
#         print("Age: {} years".format(self.age))
#         print("Coat Color: {}".format(self.coat_color))

# print("Please Enter Details of Jack Russel Terrier Dog.")
# name1 = input("Enter name: ")
# age1 = int(input('Enter age: '))
# coat_color1 = input("Enter Coat Color: ")
# jack_russell_terrier = JackRussellTerrier(name1,age1,coat_color1)
# jack_russell_terrier.details()

# print("Please Enter Details of Bull Dog.")
# name2 = input("Enter name: ")
# age2 = int(input('Enter age: '))
# coat_color2 = input("Enter Coat Color: ")
# bull_dog = Bulldog(name2, age2, coat_color2)
# bull_dog.details()
















