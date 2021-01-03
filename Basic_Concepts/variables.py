name = "Ivan Farid"
age = 28
lastName = input("Give me your last name: ")
print(lastName)
newAge = input("Give me your new age: ")
print(newAge) #this is a string, we need to cast it
print("Your age + 1 is " + newAge) #newAge is a string here
newAge = int(newAge)
newAge = newAge + 1
print("Your age + 1 is ", newAge) #newAge is a int here

is_Student = True #boolean typs
is_worker = False #booleans types