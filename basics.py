# Starting out with python programming
print('Hello, world!')

# Working with variables
fname = 'Jija' # string
lname = 'Kahn' # string
age = '40' # string
person_age = 40 # integer
email = 'jijakahn6@gmail.com' # string
contacts = [ 553020508, 204860341 ] # list
telephone = ( 30553020508, 30204860341 ) # tuple
contact_types = { 'Home': 204860341, 'Work': 553020508 } # dictionary
married = False # boolean

print()
print('Fname is', fname, 'it is of type', type(fname))
print('Person age is', person_age, 'it is of type', type(person_age))
print('Contacts is', contacts, 'it is of type', type(contacts))
print('Contact types is', contact_types, 'it is of type', type(contact_types))
print('Married is', married, 'it is of type', type(married))
print(f'Dictionary keys => { contact_types.keys() }')
print(f'Dictionary values => { contact_types.values() }')
print()

# Performing some computations
number_1 = 12
number_2 = 15

print(f'Number 1\'s value => { number_1 }')
print(f'Number 2\'s value => { number_2 }')
print()

add = number_1 + number_2
print(f'The sum of both numbers => { add }')

sub = number_2 - number_1
print(f'The difference of both numbers => { sub }')

prod = number_1 * number_2
print(f'The product of both numbers => { prod }')
print()

# Taking input from users

# print('Enter your first name:')
fname = input('Enter your first name: ')

# print('Enter your last name:')
lname = input('Enter your last name: ')

age = input('Enter your age: ')

print(f'Your first name is: { fname } and it is of type: { type( fname ) }')
print(f'Your last name is: { lname } and it is of type: { type( lname ) }')
print(f'Your age is: { age } and it is of type: { type( age ) }')
print()

# Typecasting the age
new_age = int( age ) + 5
print(f'Your new age after adding 5 years is: { new_age } and it is of type { type( new_age ) }')
