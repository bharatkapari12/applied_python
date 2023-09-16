def initial_display():
    company_name = input("Enter the company name: ")
    print(f"{company_name}\n----------Temperature Report-----------\n")

def input_data():
    num_days = int(input("How many days to record: "))
    temperatures = []

    for day in range(1, num_days + 1):
        temperature = int(input(f"Temperature day [{day}]: "))
        temperatures.append(temperature)

    return num_days, temperatures

def calculateTemperature(temperatures):
    total_temperature = sum(temperatures)
    average_temperature = (total_temperature / len(temperatures))
    return average_temperature

def category_check(temperature):
    if temperature >= 85:
        return 'very hot'
    elif 60 <= temperature < 85:
        return 'pleasant day'
    else:
        return 'very cold'

def displayInformation(num_days, temperatures):
    temperature_categories = {'very hot': 0, 'pleasant day': 0, 'very cold': 0}

    print("\nDaily Temperature Report")
    for day, temperature in enumerate(temperatures, start=1):
        category = category_check(temperature)
        print(f"Temperature day [{day}] = {temperature} Celsius ({category})")
        temperature_categories[category] += 1

    average_temperature = calculateTemperature(temperatures)

    print(f"The average temperature for {num_days} days = {average_temperature} Celsius")
    print(f"Number of very hot days: {temperature_categories['very hot']} day/s")
    print(f"Number of pleasant days: {temperature_categories['pleasant day']} day/s")
    print(f"Number of very cold days: {temperature_categories['very cold']} day/s")

def main():
    initial_display()
    num_days, temperatures = input_data()
    displayInformation(num_days, temperatures)

if __name__ == "__main__":
    main()
