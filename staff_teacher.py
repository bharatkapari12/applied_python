class Teacher:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.__salary = salary  # Private attribute, denoted with double underscores

    def initialDisplay(self):
        print(f'''*********Staff Management System**********
            Kathmandu, Nepal
------------------------------------------''')

    def inputInformation(self):
        self.name = input("Enter the name of the Teacher: ")
        self.age = input("Enter the Age of the Teacher: ")
        self.department = input("Enter the Department of the Teacher: ")
        self.__salary = input("Enter the Salary of the Teacher: ")

    def displayInformation(self):
        print(f"Mr {self.name}. age {self.age}. Works under department {self.department} got Remuneration of {self.__salary}")

def main():
    teacher = Teacher("", "", "", "")
    teacher.initialDisplay()
    teacher.inputInformation()
    teacher.initialDisplay()
    teacher.displayInformation()

main()

