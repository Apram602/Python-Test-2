print("")
print("WELCOME TO THE GRANN'S PHONE DIRECTORY\n")
print("1. Add a record ") 
print("2. Search a record ")
print("3. Update a record ")
print("4. Sort the record alphabetically")
print("5. Delete a record")
print("6. Quit\n")

phoneDirectory={}
x=int(input("Enter your choice: "))

while x !=6:
    if x == 1:
        name = input("Enter Name: ")
        if name in phoneDirectory:
            print("Name already exists in the directory.")
            user = input("Do you want to update the name? (yes/no): ").lower()
            if user == 'yes':
               print("Your name is updated")
            elif user == 'no':
               print("The name is not updated")
        if name.isalpha():
            number = input("Enter your 10-digit phone number: ")
            if number.isnumeric and len(number) == 10:
                phoneDirectory[name] = {"Number": number}
                print("\nRecord Added\n")
                print("Name:", name)
                print("Number:", number)
                print("\n")
                print("Your Contacts",phoneDirectory)
            else:
                print("Please enter a 10-digit numeric phone number.")
        else:
            print("Please enter a valid name with alphabet only.")
 
    elif x==2:
        search=input("Enter name to search: ")
        if search.isalpha in phoneDirectory:
            print("Number:", phoneDirectory[search])
        else:
            print("No contact exists with this name.")

    elif x==3:
        update_data1 =input("Enter Name to update: ")
        if update_data1  in phoneDirectory:
            name=input("Enter new Name: ")
            number = int(input("Enter your New 10-digit phone number: "))
            phoneDirectory.update({name:number})
            print("Updated", update_data1, "to :", name)
            print("Updated",  "Number to :", number)
            if phoneDirectory =={}:
                print("Your Phone Directory is Empty")
        else:
            print("No data not found")

    elif x==4:
        if phoneDirectory =={}:
            print("Your Phone Directory is Empty")
        else:
            myKeys = list(phoneDirectory.keys())
            myKeys.sort()
            sorted_dict = {i: phoneDirectory[i] for i in myKeys}

        print("\nSorted Phone Directory:\n")
        for name, number in sorted_dict.items():
            print("Name:", name)
            print("Number:", number['Number'])

    elif x ==5:
        if phoneDirectory =={}:
            print("Your Phone Directory is Empty")
        else:
            delete = input("Enter Contact Name to delete from records: ")
            if delete.isalpha in phoneDirectory:
                del phoneDirectory[delete]
                print("Deleted", delete)
            else:
                print("Please Enter the in Alphabet")


    print("")
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY\n")
    print("1. Add a record ") 
    print("2. Search a record ")
    print("3. Update a record ")
    print("4. Sort the record alphabetically")
    print("5. Delete a record")
    print("6. Quit\n")

    x=int(input("Enter your choice: "))

print("You have Quit the Menu...")


