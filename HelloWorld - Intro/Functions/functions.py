def greet_user():
    print('Hi there!')
    print('Welcome aboard')

def greet_name(first_name, last_name):
    print(f'Hi {last_name} {first_name}!')
    print('Welcome aboard')


def square(number):
    print(number * number)



print("Start")
greet_user()
greet_name('Dahyun', 'Kim')
greet_name(last_name="Park", first_name="Jihyo")
print(f'The square of 3 is {square(3)}')
print("Finish")