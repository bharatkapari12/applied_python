class TemperatureTracker:
    def __init__(self):
        self.company_name = ''
        self.num_days = 0
        self.temperatures = []
        self.temperature_categories = {
            'very hot': 0, 'pleasant day': 0, 'very cold': 0}

    def initial_display(self):
        self.company_name = input("Enter the company name: ")
        print(f"{self.company_name}\n----------Temperature Report-----------\n")

    def input_data(self):
        self.num_days = int(input("How many days to record: "))
        for day in range(1, self.num_days + 1):
            temperature = int(input(f"Temperature day [{day}]: "))
            self.temperatures.append(temperature)

    def category_check(self, temperature):
        if temperature >= 85:
            return 'very hot'
        elif temperature < 85 and temperature >= 60:
            return 'pleasant day'
        else:
            return 'very cold'

    def generate_report(self):
        print("\nDaily Temperature Report")
        for day, temperature in enumerate(self.temperatures, start=1):
            category = self.category_check(temperature)
            print(
                f"Temperature day [{day}] = {temperature} Celsius ({category})")
            self.temperature_categories[category] += 1
        
        # Average Calculation
        average_temperature = sum(self.temperatures) / self.num_days
        print(f"The average temperature for {self.num_days} days = {average_temperature:.2f} Celsius")
        print(f"Number of very hot days: {self.temperature_categories['very hot']} day/s")
        print(f"Number of pleasant days: {self.temperature_categories['pleasant day']} day/s")
        print(f"Number of very cold days: {self.temperature_categories['very cold']} day/s")


def main():
    tt = TemperatureTracker()
    tt.initial_display()
    tt.input_data()
    tt.generate_report()


main()


# class TemperatureTracker:
#     def __init__(self):
#         self.company_name = ''
#         self.company_address = ''
#         self.num_days = 0
#         self.temperature_readings = []    # list define
#         self.temperature_categories = {'very_hot': 0, 'pleasant': 0, 'very_cold': 0}   # default dectionary
#         self.temperature_range = {'very_hot': range(85, 101), 'pleasant': range(60, 85), 'very_cold': range(0, 60)}

#     def initialDisplay(self, company_name, company_address):
#         self.company_name = company_name
#         self.company_address = company_address
#         print(f'{self.company_name}\n----------Temperature Record Management System-----------\n{self.company_address}\n')

#     def InputInformation(self):
#         self.num_days = int(input('How many days to record? '))
#         print('\nPlease enter temperature readings for each day:')
#         for i in range(self.num_days):
#             temperature = int(input(f'Temperature day [{i+1}] = '))
#             self.temperature_readings.append(temperature)

#     def calculateTemperature(self):
#         total_temperature = sum(self.temperature_readings)
#         average_temperature = round(total_temperature / self.num_days)
#         for temp in self.temperature_readings:
#             for category, temp_range in self.temperature_range.items():
#                 if temp in temp_range:
#                     self.temperature_categories[category] += 1
#                     break
#         return average_temperature

#     def CategoryCheck(self, temp):
#         if temp in self.temperature_range['very_hot']:
#             return 'very_hot'
#         elif temp in self.temperature_range['pleasant']:
#             return 'pleasant'
#         else:
#             return 'very_cold'

#     def displayInformation(self):
#         print(f'Daily Temperatures Report')
#         for i, temp in enumerate(self.temperature_readings):
#             category = self.CategoryCheck(temp)
#             print(f'Temperature day [{i+1}] = {temp} Celsius {category} ')
#         print(f'The average Temp for {self.num_days} days = {self.calculateTemperature()} Celsius')


#     def finalDisplay(self):
#         print(f'\nNumber of hot days = {self.temperature_categories["very_hot"]} day/s')
#         print(f'Number of pleasant days = {self.temperature_categories["pleasant"]} day/s')
#         print(f'Number of cold days = {self.temperature_categories["very_cold"]} day/s')


# #  functional call
# tt = TemperatureTracker()
# tt.initialDisplay('UniCampus', 'Kathmandu Nepal')
# tt.InputInformation()
# tt.displayInformation()
# tt.finalDisplay()
