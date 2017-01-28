def program():
    print('Are you wanting to do a customer or manager action')
    action = input('c or m\n')
    if action == "c":
        print("Are you renting or returning an item? ")
        a = input('rent or return? \n')
     
    elif action == "m":
     
        print('m')
    else:
        print("invalid input")
        program()


