# chai-learns-python

Here I will be breaking down what I learned in Python.

# HelloWorld

This is the introduction to Python.  Several Concepts will be simple or fundamental aspects of programming principles.

## Print Messages

Nothing too game changing.  Basic programming knowledge, uses `print()` function to print messages to console

One immediate difference from C++ is the ability to evaluate expressions within print statement, for example `print('*' * 10)` will print `**********` to the console window.

## Variables

There is no need to declare the type of variable.  They are dynamically casted based on whatever is assigned to them, much like the `auto` feature in c++.

```py
price = 10      # Saves as an int
range = 4.9     # Saves as a float
name = 'Chai'   # Saves as a string
```

## Input

Input is much more intuitive, allowing users to both output a display message, and collect input with one statement.

```py
name = input('What is your name? ')
```

Effectively prints "What is your name? " on the users console, obtains input, then saves that input to the variable `name`

## Type Conversion
Nothing too major.  Typecasting is standard and involves invoking the function and passing in the value we want to convert.

A la `variable_type(input)`

Assuming we ask user to input their age, it is store as a string.

```py
birth_year = input('Birth year: ')      # Stored as '1999'
age = 2022 - int(birth_year)            # Converts to 1999
print(age)                              # Prints 23
```

### Type Checking

We can use `type(input)` to obtain the value/class of the object passed in.

```py
birth_year = input('Birth year: ')
print(type(birth_year))                 # Prints <class 'str'>
age = 2022 - int(birth_year)
print(type(age))                        # Prints <class 'int'>
print(age)
```

