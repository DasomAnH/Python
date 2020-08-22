groceries_list = []

while True:

    action = input('Do you want to add,print, or remove an item?').lower()
    if action == 'add':
        add2 = 'yes'
        while add2 == "yes":
            item = input('what would you like to add?')
            groceries_list.append(item)
            add2 = input('add another?').lower()
            if add2 != 'yes' and add2 != 'no':
                print('please try again')
    elif action == 'print':
        print('\nGrocery list:')
        for index in range(len(groceries_list)):
            print(f'{index + 1}:{groceries_list[index].capitalize()}')

    elif action == 'remove':
        remove2 = 'yes'
        while remove2 == "yes":
            remove1 = input('what woudl you like to remove?')
            groceries_list.append(remove1)
            if remove2 != 'yes' and remove2 != 'no':
                print('please try agian')
    else:
        print('please try agin')
        