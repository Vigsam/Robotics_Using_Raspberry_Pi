#1. Creating a list

fruits = ["mango","banana","apple",45,54,22,2.0]
print(fruits)

#2. Access an item in the list

print(fruits[0])
print(fruits[0:3])


#3. Update an item in the list

fruits[3] = 100
print(fruits)

#4. Add item in the list

fruits.append(98)
print(fruits)

#5. Remove Item in the list

fruits.remove(98)
print(fruits)