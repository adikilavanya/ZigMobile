class Person:
    def _init_(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

# Example usage
name = input("Enter name: ")
age = int(input("Enter age: "))
mobile = input("Enter mobile number: ")
person = Person(name, age, mobile)
print("Name:", person.name)
print("Age:", person.age)
print("Mobile:", person.mobile)
