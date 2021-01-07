numbers = [1, 2, 3, 4, 5, 6] #of numbers 
objects = ["Hello", 2, 4.5, True, "World"] #aAny object

#we can access like a string or array of strings
print(objects[0]) #access to element 1, position 0

objects.append(False) #To add an element to
objects.pop(1) #Erase the 1 position element
print(objects)

for elements in objects:
    print(elements)
