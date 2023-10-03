# List datatypes
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
print('From 0th index to 3rd index => ', contacts[0:3])
print('From 3rd index to the last index => ', contacts[3:-1])
print('From 3rd index (inclusive) to the 1st index => ', contacts[:3])
print('From 3rd index (exclusive) to the 1st index => ', contacts[::3])

print()
fullname = 'Bernard Asamoah'




# Dictionary datatypes