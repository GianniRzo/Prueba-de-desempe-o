import validations

def show_menu():
    while True: 
        print("\t.:STUDENT MANAGEMENT SYSTEM:.")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Edit Student  ")
        print("6. Exit")
    
        choice = input("Please select an option: ")

        if choice == '1':
            validations.add_students()
        elif choice == '2':
            validations.view_students()
        elif choice == '3':
            validations.search_students()
        elif choice == '4':
            validations.delete_students()
        elif choice == '5':
            validations.edit_students()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

show_menu()

