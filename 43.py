class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class AdmissionSystem:
    def __init__(self):
        self.students = []

    def admit_student(self, name, department):
        student = Student(name, department)
        self.students.append(student)

    def count_students(self, department):
        count = sum(1 for student in self.students if student.department == department)
        return count

    def sort_students(self):
        self.students.sort(key=lambda x: x.name)

if __name__ == "__main__":
    admission_system = AdmissionSystem()

    while True:
        print("\n1. Admit Student")
        print("2. Count Students in a Department")
        print("3. Display Sorted Student List")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter student name: ")
            department = input("Enter department (pgdm/btech): ")
            admission_system.admit_student(name, department)
            print("Student admitted successfully.")

        elif choice == "2":
            department = input("Enter department to count students: ")
            count = admission_system.count_students(department)
            print(f"Number of students in {department} department: {count}")

        elif choice == "3":
            admission_system.sort_students()
            print("\nSorted Student List:")
            for student in admission_system.students:
                print(f"{student.name} - {student.department}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
