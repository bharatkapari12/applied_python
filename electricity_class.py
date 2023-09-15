class ElectricityBillCalculator:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units
        self.base_cost = 100
        self.additional_cost_per_unit = 5

    def calculate_total_cost(self):
        if self.units <= 100:
            total_cost = self.base_cost
        else:
            additional_units = self.units - 100
            additional_cost = additional_units * self.additional_cost_per_unit
            total_cost = self.base_cost + additional_cost
        return total_cost


# Get number of customers
try:
    num_customers = int(input("Enter the number of customers: "))

    if num_customers <= 0:
        print("Number of customers should be greater than 0.")
    else:
        # Open a file for writing console output
        with open("electricity_bills.txt", "w") as file:
            for i in range(num_customers):
                customer_name = input(f"Enter the name of customer {i + 1}: ")
                consumed_units = float(
                    input(f"Enter the number of units consumed by {customer_name}: "))

                if consumed_units >= 0:
                    # Create an instance of the ElectricityBillCalculator class
                    bill_calculator = ElectricityBillCalculator(
                        customer_name, consumed_units)

                    # Calculate the electricity bill using the object's method
                    bill_amount = bill_calculator.calculate_total_cost()

                    # Display the calculated bill amount
                    output = f"{customer_name}'s Electricity Bill Amount: {bill_amount}\n"
                    print(output)

                    # Write output to the file
                    file.write(output)
                else:
                    print(
                        f"Invalid input. Units consumed by {customer_name} should be a non-negative number.")
except ValueError:
    print("Invalid input. Please enter a valid number of customers.")
