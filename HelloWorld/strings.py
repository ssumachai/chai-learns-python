# To use a single quote in a string...just put them in between double quotes

course = "Python's Course for Beginners"
print(course)

# To use a double quote in a string...just put in between single quotes

course_two = 'Python for "Beginners"'
print(course_two)

course_three = '''
Hi Ivan,

Here is our first email to you.

Thank you,
Chai
'''
print(course_three)

indexing = "Python for Beginners"
another = indexing[:]       # Copies essentially

print(indexing[0])          # Will Print "P"
print(indexing[-1])         # Will Print "s"
print(indexing[0:3])        # Will Print "Pyt"
print(indexing[0:])         # is Essentially print all
print(indexing[1:])         # Will print from Index 1 onwards
print(indexing[:5])         # Will Print from 0 to 4

name = 'Jennifer'
print(name[1:-1])
