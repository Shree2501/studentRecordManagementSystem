FILE_NAME = "students.txt"

# 1. Add student record (append mode)
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:   # a = append
        file.write(f"{roll},{name},{marks}\n")

    print("Student record added successfully.\n")

# 2. Read all student records (read mode)
def view_students():
    try:
        with open(FILE_NAME, "r") as file:  # r = read
            records = file.readlines()
            if not records:
                print("No records found.\n")
                return

            print("\nRoll\tName\tMarks")
            print("-" * 25)
            for record in records:
                roll, name, marks = record.strip().split(",")
                print(f"{roll}\t{name}\t{marks}")
            print()

    except FileNotFoundError:
        print("File does not exist.\n")


# 3. Update student record (read + write)
def update_student():
    roll_to_update = input("Enter Roll Number to update: ").strip()
    found = False
    updated_records = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")

                if roll == roll_to_update:
                    print("Leave input empty if no change required")

                    new_name = input(f"Enter new Name ({name}): ").strip()
                    new_marks = input(f"Enter new Marks ({marks}): ").strip()

                    if new_name == "":
                        new_name = name
                    if new_marks == "":
                        new_marks = marks

                    updated_records.append(f"{roll},{new_name},{new_marks}\n")
                    found = True
                else:
                    updated_records.append(line)

        if not found:
            print("Roll number not found.\n")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)

        print("Student record updated successfully.\n")

    except FileNotFoundError:
        print("File does not exist.\n")


# Main Menu
def main():
    while True:
        print("You would like to ?")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            print("Exited")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
