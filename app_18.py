#class and object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Kshitish", 49)

print(person3.name)
print(person3.age)

message = person1.greet()
print(message)

# class Car:
#     def __init__(self, company, model):
#         self.company = company
#         self.model = model

#     def greet(self):
#         return f"Hello, I have {self.company} car and it is of {self.model} model."
# car1 = Car("Honda", 2009)
# car2 = Car("Suzuki", 2013)

# print(car2.company)
# print(car2.model)

# message = car2.greet()
# print(message)


# class Car:
#     wheels = 4

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# print(Car.wheels)

# car1 = Car("Toyota", "Canrry")
# car2 = Car("Honda", "Accord")

# print(car1.make)
# print(car2.model)

# class Car:
#     wheels = 4

#     def __init__(self):
#         self.make = "hyundai"
#         self.model = "2009"

# print(Car.wheels)

# car1 = Car("Toyota", "Canrry")
# car2 = Car("Honda", "Accord")

# print(car1.make)
# print(car2.model)


# class Parents:
#     def __init__(self, song):
#         print(f"i can singthis {song}")
          
# class Child(Parents):
#     def __init__(self, songdance):
#         self.song = song
#     def dance(self):
#         print(f"i can dance on this {self.song}")
# c1 = child("hello")
# c2 = child("abc")
# c1.sing("aaa")

#Multiple inheritance
# class A:
#     def method_A(self):
#         return "Method A"
# class B:
#     def method_B(self):
#         return "Method B"
# class C(A, B):
#     def method_c(self):
#         return "Method C"

# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_c())

#Multilevel Inheritence

# class A:
#     def method_A(self):
#         return "Method A"
# class B(A):
#     def method_B(self):
#         return "Method B"
# class C(B):
#     def method_c(self):
#         return "Method C"

# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_c())

# class rect:
#     def area(self, length, width):
#         return length * width
# class sq(rect):
#     def area_of_sq(self, length):
#         result = super().area(length,length)
#         print(result)
# box = sq()

# tv = sq()

# box.area_of_sq(5)
# tv.area_of_sq(10)