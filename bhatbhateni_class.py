class SunwayBillSystem:
    def __init__(self):
        self.customerId = None
        self.customerName = None
        self.address = None
        self.items = None
        self.priceList = []
        self.quantityList = []
        self.amountList = []
        self.totalAmount = 0
        self.discountPercentage = None
        self.discountedValue = None
        self.finalAmount = None

    def initialDisplay(self):
        display = '''
        *********************************--*********************************
        Sunway Bhatbhateni system
        Maitidevi, Kathmandu
        *********************************--*********************************
        '''
        return display

    def userinput(self):
        self.customerName = input("Enter the customer Name: ")
        self.customerId = input("Enter the customer Id: ")
        self.address = input("Enter the customer Address: ")
        self.items = int(input('Enter the number of items: '))

        for i in range(self.items):
            price = int(input(f"Enter the price of {i+1} items: Rs."))
            quantity = int(input(f"Enter the quantity of {i+1}: "))
            amount = price * quantity
            self.priceList.append(price)
            self.quantityList.append(quantity)
            self.amountList.append(amount)
            self.totalAmount += amount

    def calculateDiscount(self):
        if self.totalAmount <= 500:
            self.discountPercentage = 1
            self.discountedValue = self.totalAmount * 0.01
            self.finalAmount = self.totalAmount - self.discountedValue

        elif self.totalAmount > 500 and self.totalAmount <= 1000:
            self.discountPercentage = 3
            self.discountedValue = 500 * 0.01 + (self.totalAmount - 500) * 0.03
            self.finalAmount = self.totalAmount - self.discountedValue
            
        elif self.totalAmount > 1000 and self.totalAmount <= 1500:
            self.discountPercentage = 5
            self.discountedValue = 500 * 0.01 + (1000 - 500) * 0.03 + (self.totalAmount - 1000) * 0.05
            self.finalAmount = self.totalAmount - self.discountedValue

        elif self.totalAmount > 1500 and self.totalAmount <= 2000:
            self.discountPercentage = 8
            self.discountedValue = 500 * 0.01 + (1000 - 500) * 0.03 + (1500 - 1000) * 0.05 + (self.totalAmount - 1500) * 0.08
            self.finalAmount = self.totalAmount - self.discountedValue
            
        else:
            self.discountPercentage = 10
            self.discountedValue = 500 * 0.01 + (1000 - 500) * 0.03 + (1500 - 1000) * 0.05 + (2000 - 1500) * 0.08 + (
                self.totalAmount - 2000) * 0.1
            self.finalAmount = self.totalAmount - self.discountedValue

    def outputData(self):
        a = ''
        for i in range(self.items):
            a += f'''
            {str(i + 1)} product = Rs.{self.priceList[i]} * {self.quantityList[i]} items 
            Amount : Rs.{self.amountList[i]} 
            '''

        display = f'''

        {self.initialDisplay()}
        ------------------------------------------------------------------------------------------------------------------------

        Customer Name : {self.customerName}
        Customer Id : {self.customerId}
        Customer Address : {self.address}
        Total Amount : {str(self.totalAmount)}
        {a}

        Mr/Mrs. {self.customerName}, you have purchased {self.items} items whose total price is {self.totalAmount} and discount is Rs.{self.discountedValue} with discount rate {self.discountPercentage}%. So, You have to pay Rs.{self.finalAmount}

        ------------------------------------------------------------------------------------------------------------------------

        '''
        print(display)
        return display

    def saveToFile(self, file_path):
        with open(file_path, 'a') as file:
            file.write(self.outputData())


number_of_users = int(input("Enter the number of users: "))

for _ in range(number_of_users):
    bill_system = SunwayBillSystem()
    bill_system.userinput()
    bill_system.calculateDiscount()
    bill_system.outputData()
    bill_system.saveToFile('sunway_bill_text.txt')
