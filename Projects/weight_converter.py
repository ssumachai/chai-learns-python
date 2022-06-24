import math

weight = int(input('Weight: '))
weight_type = input('(L)bs or (K)g: ')

if weight_type.upper() == 'L':
    converted_weight = weight * 0.45
    weight_string = 'kgs'
elif weight_type.upper() == 'K':
    converted_weight = weight * 2.2
    weight_string = 'lbs'
else:
    print('Invalid Input')

print(f'You are {converted_weight} {weight_string}')