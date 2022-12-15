import os
os.system('cls' if os.name == 'nt' else 'clear')
print("----------------------------------------")


#! Topics to be Covered:
#* Everything in Python is class
#* Defining class
#* Defining class attributes
#* Difference between class attributes and instance attributes
#* SELF keyword
#* Defining methods
#* Class Methods vs. Static Methods and Instance Methods
#* Special methods (init, str)
#* 4 pillars of OOP:
    #? Encapsulation
    #? Abstraction
    #? Inheritance
        #? Multiple inheritance
    #? Polymorphism
        #? Overriding methods
#* Inner class
#* Overloading an operator (optional)
#* Abstract base class 



# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122, "victor", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)


# class Person:
#     name = "victor"
#     age = 32


# person1 = Person()
# person2 = Person()

# print(person1.name)

# Person.job = "Fullstack developer"

# print(person2.job)
# classta yapılan değişiklikler o classtan üretilen instancelara da aktarılır.

#! class attributes vs instance attributes


# class Person:
#     name = "victor"
#     age = 32

# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"
# print(person2.locaiton)
# bir instance a eklenen attribute diğerlerini değiştirmez
# person2.age = 18
# print(person2.age)
# print(person1.age)
# ? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆

#! SELF keywrd and methods


# class Person:
#     company:"Clarusway"

#     def test(self):
#         print("test")

#     def get_details(self):
#         print(f"{self.name}-{self.age}")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
    
#     @staticmethod
#     def salute():
#         print("hi there!")

# person1=Person()
# person2=Person()

# # person1.test()

# person1.name= "jason"
# person1.age= 33
# person1.get_details()

# # person2.name = "henry"
# # person2.age = 18

# person2.set_details("yasin",33)
# person2.get_details()

# person1.salute()

#! special methods (init, str)


class Person:
    company = "clarusway"
    person_count = 0

    def __init__(self,name,age,gender="male"):
        self.name=name
        self.age=age
        self.gender = gender
        Person.person_count = Person.person_count+1

    def get_details(self):
        print(f"{self.name}-{self.age}-{self.gender}")


    def __str__(self):
        return f"{self.name} - {self.age}"



# person1 = Person("jason",33)
# person1.get_details()

# person2=Person() içine argüman vermezsek hata alırız 
person2=Person("yasin",22)
person3=Person("yasin",22)
person3.get_details()

print(Person.person_count)












print("----------------------------------------")
