import json

class Student:
    def __init__(self, student_id, student_name, CGPA, age, branch):
        self.Student_id = student_id
        self.Student_name = student_name
        self.CGPA = CGPA
        self.age = age
        self.Branch = branch

    @staticmethod
    def add_student():
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        CGPA = float(input("Enter the student CGPA: "))
        age = int(input("Enter the student age: "))
        branch = input("Enter the student branch: ")
        return Student(student_id, student_name, CGPA, age, branch)

    def display_student(self):
        print("Student_ID:", self.Student_id)
        print("Student_name:", self.Student_name)
        print("CGPA:", self.CGPA)
        print("Age:", self.age)
        print("Branch:", self.Branch)


def search_student(students, student_id):
    for student in students:
        if student.Student_id == student_id:
            return student
    return None


def delete_student(students, student_id):
    for index, student in enumerate(students):
        if student.Student_id == student_id:
            del students[index]
            return True
    return False


def update_student(student):
    while True:
        choice = input("Enter field to update (name/cgpa/age/branch) or done: ")
        if choice.lower() == "name":
            student.Student_name = input("Enter the new name: ")
        elif choice.lower() == "cgpa":
            student.CGPA = float(input("Enter the new CGPA: "))
        elif choice.lower() == "age":
            student.age = int(input("Enter the new age: "))
        elif choice.lower() == "branch":
            student.Branch = input("Enter the new branch: ")
        elif choice.lower() == "done":
            break
        else:
            print("Invalid choice.")

        cont = input("Do you want to update anything else? (yes/no): ")
        if cont.lower() != "yes":
            break

    return True


def save_students_to_file(students, filename):
    with open(filename, 'w') as file:
        json.dump([student.__dict__ for student in students], file)


def load_students_from_file(filename):
    try:
        with open(filename, 'r') as file:
            students_data = json.load(file)
            return [Student(**data) for data in students_data]
    except FileNotFoundError:
        return []


def main():
    students = load_students_from_file('students.json')

    while True:
        print("\n===========STUDENT MANAGEMENT SYSTEM===========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student = Student.add_student()
            students.append(student)
            print("Student added successfully.")
        elif choice == "2":
            if not students:
                print("No students available.")
            for student in students:
                student.display_student()
                print("-----")
        elif choice == "3":
            student_id = input("Enter the student ID to search: ")
            found_student = search_student(students, student_id)
            if found_student:
                print("Student found:")
                found_student.display_student()
            else:
                print("Student not found.")
        elif choice == "4":
            student_id = input("Enter the student ID to delete: ")
            if delete_student(students, student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        elif choice == "5":
            student_id = input("Enter the student ID to update: ")
            found_student = search_student(students, student_id)
            if found_student:
                update_student(found_student)
                print("Student updated successfully.")
            else:
                print("Student not found.")
        elif choice == "6":
            save_students_to_file(students, 'students.json')
            print("Students saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
