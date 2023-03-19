number = input("Enter the number ").split(",")
print(number)
for i in range(len(number)):
    number[i] = int(number[i])
print(number)
for i in range(len(number)):
    for j in range(len(number)):
        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp
print()

for num in number:
    print(num, end=" ")
