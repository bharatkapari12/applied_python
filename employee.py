# Construct a class Employee with attributes like emp_id, emp_name, emp_salary, and
# emp_department and methods like calculate_emp_salary, emp_assign_department, and
# print_employee_details.
# Sample Employee Data:
# "RAHUL", "E7876", 50000, "ACCOUNTING"
# "PRAKASH", "E7499", 45000, "RESEARCH"
# "ADAM", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is
# the number of hours worked by the employee. If the number of hours worked is more than 50,
# the method computes overtime and adds it to the salary. Overtime is calculated as following
# formula:
# overtime = hours_worked – 50
# Overtime amount = (overtime * (salary / 50))

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        overtime = hours_worked - 50
        overtime_amount = (overtime * (self.emp_salary / 50))
        total_salary = self.emp_salary + overtime_amount
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")


employee_1 = Employee("E7876", "RAHUL", 50000, "ACCOUNTING")
employee_2 = Employee("E7499", "PRAKASH", 45000, "RESEARCH")
employee_3 = Employee("E7900", "ADAM", 50000, "SALES")
employee_4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

print(employee_1.emp_name)
print(employee_1.calculate_emp_salary(60))
employee_1.emp_assign_department("FINANCE")
employee_1.print_employee_details()






class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            return self.emp_salary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            return self.emp_salary + overtime_amount

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

# Sample Employee Data
employee1 = Employee("RAHUL", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("PRAKASH", "E7499", 45000, "RESEARCH")
employee3 = Employee("ADAM", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# Example Usage
employee1.print_employee_details()
employee1.assign_department("HR")
employee1.print_employee_details()
print("Employee 1 Salary for 60 hours worked:", employee1.calculate_emp_salary(60))


# print(employee1.emp_name)
# print(employee1.calculate_emp_salary(60))
# employee1.assign_department("FINANCE")
# employee1.print_employee_details()