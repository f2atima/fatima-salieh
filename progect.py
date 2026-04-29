class Grade:
    def __init__(self, name, student_id, major):
        self.name = name
        self.__student_id = student_id
        self.major = major

    def get_id(self):
        return self.__student_id

    def set_id(self, new_id):
        self.__student_id = new_id


class FirstTermGrade(Grade):
    def __init__(self, name, student_id, major, grade):
        super().__init__(name, student_id, major)
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, ID: {self.get_id()}, Major: {self.major}, Grade: {self.grade}")


FILE_NAME = "data.txt"


def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, sid, major, grade = line.strip().split(",")
                students.append(FirstTermGrade(name, sid, major, grade))
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s.name},{s.get_id()},{s.major},{s.grade}\n")


def add_student(students):
    name = input("Enter name: ")
    sid = input("Enter ID: ")
    major = input("Enter major: ")
    grade = input("Enter grade: ")

    if name == "":
        print("Invalid name")
        return

    if not sid.isdigit():
        print("Invalid ID")
        return

    if major == "":
        print("Invalid major")
        return

    if grade == "":
        print("Invalid grade")
        return

    students.append(FirstTermGrade(name, sid, major, grade))
    print("Student added successfully")


def delete_student(students):
    sid = input("Enter ID to delete: ")
    for s in students:
        if s.get_id() == sid:
            students.remove(s)
            print("Deleted successfully")
            return
    print("Not found")


def update_student(students):
    sid = input("Enter ID to update: ")
    for s in students:
        if s.get_id() == sid:
            name = input("New name: ")
            major = input("New major: ")
            grade = input("New grade: ")

            if name == "":
                print("Invalid name")
                return

            if major == "":
                print("Invalid major")
                return

            if grade == "":
                print("Invalid grade")
                return

            s.name = name
            s.major = major
            s.grade = grade
            print("Updated successfully")
            return
    print("Not found")


def view_students(students):
    if not students:
        print("No data")
    for s in students:
        s.display()


def main():
    students = load_students()

    while True:
        print("1- Add Student")
        print("2- Delete Student")
        print("3- Update Student")
        print("4- View Students")
        print("5- Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            view_students(students)
        elif choice == "5":
            save_students(students)
            break
        else:
            print("Invalid choice")


main()