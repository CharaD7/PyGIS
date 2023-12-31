# List datatypes
from operator import index


contacts = [ 553020508, 204860341 ] # list

print()
print('First item in contacts list => ', contacts[0])
print('Second item in contacts list => ', contacts[1])

print()
additional_contacts = [ 2553322314, 552938123, 207236168 ]
# print('Assigning a new item to the 1st position in contacts list => ', contacts[0])
contacts.extend(additional_contacts)
print('View all elements in contacts list => ', contacts)

contacts.append(271029899)
print()
print('View all elements in contacts list => ', contacts)

print()
print('=' * 40)
print('Implementing slicing')
print('=' * 40)
print('From 0th index to 3rd index =>', contacts[0:3])
print('From 3rd index to the last index =>', contacts[3:-1])
print('From 3rd index (inclusive) to the 1st index =>', contacts[:3])
print('From 3rd index (exclusive) to the 1st index =>', contacts[::3])

print()
fullname = 'Bernard Asamoah'
print('Splitting fullname', fullname.split(' '))
first_name = fullname.split(' ')[0]
last_name = fullname.split(' ')[1]

print('')
print('Full name:', fullname)
print('First name:', first_name)
print('Last name:', last_name)

print('')
print('The length of fullname is:', len(fullname))
print('Index of the space character is:', fullname.index(' '))
print('Items before index 7', fullname[:7])
print('Items after index 7', fullname[7:])

# Dictionary datatypes
account = {
  'name' : {
    'first_name' : 'John',
    'last_name' : 'Smith',
  },
  'contact' : 23023323022,
  'email' : 'jsmith@gmail.com',
}

print()
print('----------------------------------------')
print('Working with Dictionary variables')
print('----------------------------------------')
print('Account contents:', account)
print('Account information:', account.values())
print('Account API_name:', account['name'])
print('Account name:', account['name'].values())
print('Account first name:', account['name']['first_name'])
print('Account last name:', account['name']['last_name'])
print('Account phone:', account['contact'])
print('Account email:', account['email'])

print()
print('Changing the first name to Michael')
account['name']['first_name'] = 'Michael'
print('Display the new first name:', account['name']['first_name'])

print()
# print('Emptying the dictionary')
# account = {}
# account.clear()

# print('Account details', account)

print('Deleting the contact information')
account.pop('contact')
print('Account information', account)

additional_info = {
  'sex': 'Male',
  'religion': 'Christian',
  'children': ['Cephas', 'Sonia', 'Aseph', 'Kate']
}

account.update(additional_info)
print('Account updated', account)