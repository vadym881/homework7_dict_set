'hw_7.1'
def say_hi(name, age):
    expression = f"Hi. My name is {name} and I'm {age} years old"
    return expression

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

name = input('Enter name: ')
age = input('Enter age: ')

print(say_hi(name, age))