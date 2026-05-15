import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Course"])


# Add Student
def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sid, name, age, course])

    print("✅ Student added successfully!\n")


# View Students
def view_students():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        print("\n--- Student Records ---")
        for row in reader:
            print(row)
    print()


# Update Student
def update_student():
    sid = input("Enter ID to update: ")
    updated = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == sid:
                print("Enter new details:")
                name = input("Name: ")
                age = input("Age: ")
                course = input("Course: ")
                updated.append([sid, name, age, course])
                found = True
            else:
                updated.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(updated)
        print("✅ Student updated successfully!\n")
    else:
        print("❌ Student not found!\n")


# Delete Student
def delete_student():
    sid = input("Enter ID to delete: ")
    updated = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != sid:
                updated.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(updated)
        print("✅ Student deleted successfully!\n")
    else:
        print("❌ Student not found!\n")


# Menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")


# Run program
menu()
