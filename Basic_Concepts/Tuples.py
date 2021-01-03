#Clasic lists
numbers = [1, 2, 3, 4, 5] #list dinamic objetc
numbers.append("Hello")
print(numbers)

numbers2 = [6, 7, 8, 9]

final_List = numbers + numbers2

print(final_List)

#Tuples
tupleOne = (1, 3, "hello", "world") #cannot append or erase, static structure

for number in tupleOne:
    print(number)