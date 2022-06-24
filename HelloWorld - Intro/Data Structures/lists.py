names = ['Nayeon', 'Jeongyeon', 'Momo', 'Sana', 'Jihyo']
print(names[0:])

# Exercise - Find Largest Number in a List

numbers = [3, 6, 2, 9, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'Max Number: {max}')

# List Methods

names.append('Dahyun')
names.insert(5, 'Mina')
names.append('JYP')
names.pop()
print(f"Jihyo is the {names.index('Jihyo') + 1}th Oldest Member of Twice")
print(names[0:])
print('Chaeyoung' in names)
print(names.count('Mina'))

numbers2 = numbers.copy()

numbers.sort()
numbers.reverse()

numbers2.append(69)

print(numbers)
print(numbers2)

# Exercise - Remove Duplicates

dup_numbers = [2, 2, 4, 6, 3, 6, 1]
uniques = []

for i in dup_numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)


# 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for column in row:
        print(column)

