
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#for index in range(len(numbers)):
#        print(numbers[index])

list_1 =[]
list_2 =[]

for y in numbers:
    if y % 2 == 0:
        list_1.append(y)

    else:
        list_2.append(y)

print(list_1)
print(list_2)