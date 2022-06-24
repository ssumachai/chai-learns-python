for item in ['Nayeon', 'Jeongyeon', 'Jihyo']:
    print(item)

for items in range(5, 10, 2):
    print(items)

# Exercise

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f'Total: {total}')

# Nested Loops

for x_coor in range(4):
    for y_coor in range(4):
        print(f'({x_coor}, {y_coor})')

# Challenge - Print F from List!

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    output = ''
    for i in range(number):
        output += 'x'
    print(output)

# Challenge - Print L from the List!

l_numbers = [2, 2, 2, 5, 5]

for l_number in l_numbers:
    l_output = ''
    for i_l in range(l_number):
        l_output += 'x'
    print(l_output)