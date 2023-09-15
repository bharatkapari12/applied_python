class Student:
    def __init__(self):
        self.iukl_code = ""
        self.name_surname = ""
        self.address = ""
        self.phone_number = ""
        self.gender = ""
        self.email = ""
        self.grade = ""
        self.admission_amount = 0
        self.discount_amount = 0

    # Getter methods
    def get_iukl_code(self):
        return self.iukl_code

    def get_name_surname(self):
        return self.name_surname

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_gender(self):
        return self.gender

    def get_email(self):
        return self.email

    def get_grade(self):
        return self.grade

    def get_admission_amount(self):
        return self.admission_amount

    def get_discount_amount(self):
        return self.discount_amount

    # Setter methods
    def set_iukl_code(self, code):
        self.iukl_code = code

    def set_name_surname(self, name):
        self.name_surname = name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone):
        self.phone_number = phone

    def set_gender(self, gender):
        self.gender = gender

    def set_email(self, email):
        self.email = email

    def set_grade(self, grade):
        self.grade = grade

    def set_admission_amount(self, amount):
        self.admission_amount = amount

    def set_discount_amount(self, discount):
        self.discount_amount = discount

    # Method to input student information
    def input_student_information(self):
        self.name_surname = input("Enter Student's Name (in name_surname format): ")
        self.iukl_code = input("Enter IUKL Code: ")
        self.address = input("Enter Address: ")
        self.phone_number = input("Enter Phone Number: ")
        self.gender = input("Enter Gender: ")
        self.email = input("Enter Email: ")
        self.grade = input("Enter Grade: ")

    # Method to display student information
    def display_student_information(self):
        print("IUKL Code:", self.iukl_code)
        print("Name:", self.name_surname)
        print("Address:", self.address)
        print("Phone Number:", self.phone_number)
        print("Gender:", self.gender)
        print("Email:", self.email)
        print("Grade:", self.grade)
        print("Admission Amount:", self.admission_amount)
        print("Discount Amount:", self.discount_amount)

    # Method to register a new student
    def register_student(self):
        self.input_student_information()
        if float(self.grade) > 80:
            self.set_discount_amount(60)
            self.set_admission_amount(100 - self.get_discount_amount())
            print("New student has been registered.")
            print("Sending notification to admin@iukl.com.np: New student registered.")
        elif float(self.grade) > 70:
            self.set_discount_amount(50)
            self.set_admission_amount(100 - self.get_discount_amount())
            print("New student has been registered.")
            print("Sending notification to admin@iukl.com.np: New student registered.")
        elif float(self.grade) > 60:
            self.set_discount_amount(40)
            self.set_admission_amount(100 - self.get_discount_amount())
            print("New student has been registered.")
            print("Sending notification to admin@iukl.com.np: New student registered.")
        else:
            self.set_discount_amount(20)
            self.set_admission_amount(100 - self.get_discount_amount())
            print("New student has been registered.")
            print("Sending notification to admin@iukl.com.np: New student registered.")


# Example usage:
student1 = Student()
student1.register_student()
print("\nStudent Information:")
student1.display_student_information()
