students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully")

def mark_attendance():
    print("Mark Attendance")
    for student in students:
        status = input(f"{student} (P/A): ")
        with open("attendance.txt", "a") as f:
            f.write(f"{student} - {status}\n")

def view_attendance():
    with open("attendance.txt", "r") as f:
        print(f.read())

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

