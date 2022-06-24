from turtle import done, down


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Exercise

credit = False
price = 1000000

if credit:
    down_payment = price* 0.1
else:
    down_payment = price*  0.2
print(f'Down Payment: ${int(down_payment)} dollars')
