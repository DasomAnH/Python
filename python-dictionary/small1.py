phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
# retrieve value
person = phonebook_dict['Elizabeth']
print(person)

# add a value

phonebook_dict['kareem'] = '938-489-1234'

# delete
phonebook_dict['Alice'] = 'number hot found'
del phonebook_dict['Alice']

# removed_contact = phonebook_dict.pop('Alice')
# edit
phonebook_dict['Bob'] = "968-345-2345"
print(phonebook_dict)
