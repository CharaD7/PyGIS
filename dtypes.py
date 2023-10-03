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





# Dictionary datatypes