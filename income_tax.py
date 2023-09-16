class TaxCalculator:
    def __init__(self):
        self.company_name = ''
        self.date = "September 16, 2023"
        self.customers_info = []

    def initial_display(self):
        self.company_name = input("Enter the company name: ")
        display = f'''{self.company_name} TAX Calculator       
        Maitidevi, Kathmandu        
        {self.date}'''
        return display

    def input_info(self):
        num = int(input('Enter the number of customers: '))
        for i in range(num):
            cust_info = []
            name = input('Enter Staff Name: ')
            address = input('Enter the Address: ')
            married_status = input('Married Status(M/U): ')
            monthly_income = int(input('Enter the monthly income: '))
            cust_info.append(name)
            cust_info.append(address)
            cust_info.append(married_status)
            cust_info.append(monthly_income)
            self.customers_info.append(cust_info)
        return num, self.customers_info

    def tax_Unmarried(self, annual_income):
        if annual_income <= 500000:
            tax_per = 1
            income_after_tax = annual_income * 0.01
            annual_income_after_tax = (annual_income - income_after_tax)
        elif annual_income > 500000 and annual_income <= 700000:
            tax_per = 10
            income_after_tax = 500000 * 0.01 + (annual_income - 500000) * 0.1
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 700000 and annual_income <= 1000000:
            tax_per = 20
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (annual_income - 700000) * 0.2
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 1000000 and annual_income <= 2000000:
            tax_per = 30
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (annual_income - 1000000) * 0.3
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 2000000 and annual_income <= 5000000:
            tax_per = 36
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (2000000 - 1000000) * 0.3 + (annual_income - 5000000) * 0.36
            annual_income_after_tax = annual_income - income_after_tax
        else:
            tax_per = 39
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (2000000 - 1000000) * 0.3 + (5000000 - 2000000) * 0.36 + (annual_income - 5000000) * 0.39
            annual_income_after_tax = annual_income - income_after_tax
        
        return annual_income, income_after_tax, annual_income_after_tax

    def tax_married(self, annual_income):
        if annual_income <= 600000:
            tax_per = 1
            income_after_tax = (annual_income * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 600000 and annual_income <= 800000:
            tax_per = 10
            income_after_tax = (600000 * 1) / 100 + ((annual_income - 600000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 800000 and annual_income <= 1100000:
            tax_per = 20
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((annual_income - 800000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 1100000 and annual_income <= 2000000:
            tax_per = 30
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (annual_income - 1100000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 2000000 and annual_income <= 5000000:
            tax_per = 36
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (2000000 - 1100000) * 1) / 100 + ((annual_income - 5000000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        else:
            tax_per = 39
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (2000000 - 1100000) * 1) / 100 + ((5000000 - 2000000) * 36) / 100 + (
                                       (annual_income - 5000000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        
        return annual_income, income_after_tax, annual_income_after_tax

    def tax_calculation(self, status, income):
        yearly_income = income * 12
        if status == 'U' or status == 'u':
            annual_income, income_after_tax, annual_income_after_tax = self.tax_Unmarried(yearly_income)
        elif status == 'M' or status == 'm':
            annual_income, income_after_tax, annual_income_after_tax = self.tax_married(yearly_income)
        return annual_income, income_after_tax, annual_income_after_tax

    def displayInformation(self, name, address, married_status, annual_income, income_after_tax, annual_income_after_tax):
        display = f'''Name: {name}\t\t Address: {address}
        Married Status:{married_status}
        Total Annual Income: {annual_income}
        Tax Income:{income_after_tax}
        Income after tax: {annual_income_after_tax}'''
        return display

    def finalDisplay(self):
        num, customers_info = self.input_info()
        with open('incomeTax_data.txt', 'w', encoding='utf-8') as f:
            for i in range(num):
                annual_income, income_after_tax, annual_income_after_tax = self.tax_calculation(customers_info[i][2], customers_info[i][3])
                value = self.displayInformation(customers_info[i][0], customers_info[i][1], customers_info[i][2], annual_income, income_after_tax, annual_income_after_tax)
                f.write(self.initial_display() + "\n")
                f.write(value + "\n")

def main():
    tax_calculator = TaxCalculator()
    tax_calculator.finalDisplay()

if __name__ == "__main__":
    main()













# class TaxCalculator:
#     def __init__(self):
#         self.company_name = ''
#         self.date = 1
#         self.customers_info = []

#     def initial_display(self):
#         self.company_name = input("Enter the company name: ")
#         heading = f'''       {self.company_name} TAX Calculator       
#         Maitidevi, Kathmandu        
#             {self.date}'''
#         return heading

#     def input_info(self):
#         num = int(input('Enter the number of customers: '))
#         for i in range(num):
#             cust_info = {}
#             cust_info['name'] = input('Enter the name: ')
#             cust_info['address'] = input('Enter the Address: ')
#             cust_info['married_status'] = input('Married Status(M/U): ')
#             cust_info['monthly_income'] = int(input('Enter the monthly income: '))
#             self.customers_info.append(cust_info)
#         return num, self.customers_info

#     def tax_Unmarried(self, annual_income):
#         if annual_income <= 500000:
#             tax_per = 1
#         elif annual_income <= 700000:
#             tax_per = 10
#         elif annual_income <= 1000000:
#             tax_per = 20
#         elif annual_income <= 2000000:
#             tax_per = 30
#         elif annual_income <= 5000000:
#             tax_per = 36
#         else:
#             tax_per = 39

#         income_after_tax = (annual_income * tax_per) / 100
#         annual_income_after_tax = annual_income - income_after_tax
#         return annual_income, income_after_tax, annual_income_after_tax

#     def tax_married(self, annual_income):
#         if annual_income <= 600000:
#             tax_per = 1
#         elif annual_income <= 800000:
#             tax_per = 10
#         elif annual_income <= 1100000:
#             tax_per = 20
#         elif annual_income <= 2000000:
#             tax_per = 30
#         elif annual_income <= 5000000:
#             tax_per = 36
#         else:
#             tax_per = 39

#         income_after_tax = (annual_income * tax_per) / 100
#         annual_income_after_tax = annual_income - income_after_tax
#         return annual_income, income_after_tax, annual_income_after_tax

#     def tax_calculation(self, status, income):
#         yearly_income = income * 12
#         if status == 'U' or status == 'u':
#             annual_income, income_after_tax, annual_income_after_tax = self.tax_Unmarried(yearly_income)
#         elif status == 'M' or status == 'm':
#             annual_income, income_after_tax, annual_income_after_tax = self.tax_married(yearly_income)
#         return annual_income, income_after_tax, annual_income_after_tax

#     def value_print(self, cust_info):
#         return f'''Name: {cust_info['name']}\t\t Address: {cust_info['address']}
#         Married Status:{cust_info['married_status']}
#         Total Annual Income: {cust_info['monthly_income'] * 12}
#         Tax Income:{cust_info['income_after_tax']}
#         Income after tax: {cust_info['annual_income_after_tax']}'''

#     def final_print(self):
#         num, customers_info = self.input_info()
#         with open('tax_data.txt', 'w', encoding='utf-8') as f:
#             for cust_info in customers_info:
#                 annual_income, income_after_tax, annual_income_after_tax = self.tax_calculation(cust_info['married_status'], cust_info['monthly_income'])
#                 cust_info['income_after_tax'] = income_after_tax
#                 cust_info['annual_income_after_tax'] = annual_income_after_tax
#                 value = self.value_print(cust_info)
#                 f.write(self.initial_display() + "\n")
#                 f.write(value + "\n")

# def main():
#     tax_calculator = TaxCalculator()
#     tax_calculator.final_print()

# if __name__ == "__main__":
#     main()










# class IncomeTaxCalculator:
#     def __init__(self, name, income, is_married):
#         self.name = name
#         self.income = income
#         self.is_married = is_married

#     def calculate_tax(self):
#         if not self.is_married:
#             if self.income <= 400000:
#                 tax = self.income * 0.01
#             elif 400001 <= self.income <= 500000:
#                 tax = 4000 + (self.income - 400000) * 0.1
#             elif 500001 <= self.income <= 700000:
#                 tax = 14000 + (self.income - 500000) * 0.2
#             elif 700001 <= self.income <= 2000000:
#                 tax = 54000 + (self.income - 700000) * 0.3
#             else:
#                 tax = 624000 + (self.income - 2000000) * 0.36
#         else:  # Married
#             if self.income <= 450000:
#                 tax = self.income * 0.01
#             elif 450001 <= self.income <= 550000:
#                 tax = 4500 + (self.income - 450000) * 0.1
#             elif 550001 <= self.income <= 750000:
#                 tax = 14500 + (self.income - 550000) * 0.2
#             elif 750001 <= self.income <= 2000000:
#                 tax = 54500 + (self.income - 750000) * 0.3
#             else:
#                 tax = 609500 + (self.income - 2000000) * 0.36
#         return tax


# def main():
#     print("Welcome to the Income Tax Calculator")
#     name = input("Enter your name: ")
#     address = input("Enter your address: ")
#     income = float(input("Enter your income (NPR): "))
#     marital_status = input("Are you married? (yes/no): ").lower()
    
#     if marital_status == "yes":
#         is_married = True
#     else:
#         is_married = False
    
#     calculator = IncomeTaxCalculator(name, income, is_married)
#     tax = calculator.calculate_tax()
    
#     print("\nTax Information:")
#     print(f"Name: {calculator.name}")
#     print(f"Address: {address}")
#     print(f"Income: NPR {income:.2f}")
#     print(f"Marital Status: {'Married' if is_married else 'Unmarried'}")
#     print(f"Income Tax: NPR {tax:.2f}")

# main()

