# If Statements

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

# Logical Operators
has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print('Eligible for Loan (AND)')            # BOTH have to be true!

if has_high_income or has_good_credit:
    print("Eligible for loan (OR)")             # EITHER or BOTH can be true!

if has_good_credit and not has_criminal_record: # Flips Affected Bool
    print("Eligible for Loan (NOT)")

# Comparison Operators

temperature = 35

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

# Example using input validator

test_string = 'POP by IM NAYEON'

if len(test_string) < 3:
    print('Name must be at least 3 characters')
elif len(test_string) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')