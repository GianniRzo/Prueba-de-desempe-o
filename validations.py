
students = []

def add_students():
    id = input("ID: ")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    state = input("State: ")

    student = {
        "id": id,
        "name": name,
        "age": age,
        "grade": grade,
        "state": state
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, State: {student['state']}") 

def search_students():
    search_id = input("Enter student ID to search: ")
    for student in students:
        if student['id'] == search_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, State: {student['state']}")
            return
    print("Student not found.")

def delete_students():
    delete_id = input("Enter student ID to delete: ")
    for student in students:
        if student['id'] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def edit_students():
    edit_id = input("Enter student ID to edit: ")
    for student in students:
        if student['id'] == edit_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, State: {student['state']}")
            # Update student information
            student['name'] = input("New Name: ")
            student['age'] = input("New Age: ")
            student['grade'] = input("New Grade: ")
            student['state'] = input("New State: ")
            print("Student updated successfully!")
            return
    print("Student not found.")

