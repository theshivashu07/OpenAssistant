def modify_list(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] += 1

numbers = [1, 2, 3, 4, 5, 6]
x = 3

for i in range(x):
    modify_list(numbers)
    numbers.append(numbers[i] * 2)
    x = len(numbers)

print(numbers)

