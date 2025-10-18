# Student Database Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Age": age, "Course": course}
    print("✅ Student added successfully!\n")

def display_students():
    if not students:
        print("No records found.\n")
    else:
        print("\n--- Student Records ---")
        for roll, details in students.items():
            print(f"Roll: {roll}, Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        s = students[roll]
        print(f"\nFound Record:\nName: {s['Name']}\nAge: {s['Age']}\nCourse: {s['Course']}\n")
    else:
        print("❌ Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("🗑️ Student record deleted.\n")
    else:
        print("❌ Roll number not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        course = input("Enter New Course: ")
        students[roll] = {"Name": name, "Age": age, "Course": course}
        print("✅ Record updated successfully!\n")
    else:
        print("❌ Roll number not found.\n")

def main():
    while True:
        print("====== Student Database Menu ======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
main()
