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

## Strings

There are apparently no rules or laws here and it's ridiculous.  We are told that you can use single-quotes and double-quotes interchangeably, but there are cases for when you want to use other ones.

Unlike c++, where the use of `'` and `"` within strings will break the formatting and throw errors, if we want to avoid those problems we literally just have to use the opposing encapsulator to avoid those problems.

Too many fancy words? Okay, to use single quote in a string...put your string in double quotes:

```py
course = "Python's Course for Beginners"
```

Want to put your double quote in a string??

```py
course = 'Python for "Beginners"'
```

## Triple-Quotes

Triple Quotes will also allow you to type in multiple lines, although for now this seems to be the tip of the iceberg.

```py
course = '''
To Whom it May Concern,

It appears that Strings are absolutely broken in Python.

Best,
Chai
'''
```

## Indexing

Indexing Here is pretty similar in terms of accessing one element, but there is a lot more automation here.  You can define the indexing as such:

`print(index[start_index (inclusive): end_index (non-inclusive)])`

meaning that if we have our string: "Bobcat", doing `print(st[0:2])` would yield "Bo". 

Negative Indexing is Also a thing, so assuming we keep our same string, doing `print(st[-1])` would yield the last value in our string, "t".

### Indexing Defaults

For all these examples, consider the string `st = "Bobcat"`:

If no end index is provided, it will assume until the end of the string:

```py
print(st[0:])
```

yields "Bobcat"

If no start index is provided, it will assume from start of the string until the non-inclusive end:

```py
print(st[:3])
```
yields "Bob"

Providing no Indices is similar to just telling the console to print everything:

```py
print(st[:])
```
yields "Bobcat"

## Formatted Strings

While we can use string cocantenation, it does start to get messy sometimes as strings get more and more complicated, to combat this, we can use f-strings, or formatted strings.

```py
last = 'Park'
first = 'Jihyo'
msg = f'{last} {first} is the leader of TWICE'
print(msg)
```
This allows us to clearly see the format of the string that is going to be printed.  The variables that are used in the curly brackets serve as placeholders until the program is run.  At runtime, they are then filled with the appropriate details.



