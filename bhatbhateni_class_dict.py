class SunwayBillSystem:
    def __init__(self):
        self.customer_info = {
            'customerName': None,
            'customerId': None,
            'address': None,
            'items': None,
            'priceList': [],
            'quantityList': [],
            'amountList': [],
            'totalAmount': 0,
            'discountPercentage': None,
            'discountedValue': None,
            'finalAmount': None
        }

    def initialDisplay(self):
        display = '''
        *********************************--*********************************
                            Sunway Bhatbhateni system
                               Maitidevi, Kathmandu
        *********************************--*********************************
        '''
        return display

    def userinput(self):
        self.customer_info['customerName'] = input("Enter the customer Name: ")
        self.customer_info['customerId'] = input("Enter the customer Id: ")
        self.customer_info['address'] = input("Enter the customer Address: ")
        self.customer_info['items'] = int(input('Enter the number of items: '))

        for i in range(self.customer_info['items']):
            price = int(input(f"Enter the price of {i+1} items: Rs."))
            quantity = int(input(f"Enter the quantity of {i+1}: "))
            amount = price * quantity
            self.customer_info['priceList'].append(price)
            self.customer_info['quantityList'].append(quantity)
            self.customer_info['amountList'].append(amount)
            self.customer_info['totalAmount'] += amount

    def calculateDiscount(self):
        totalAmount = self.customer_info['totalAmount']
        if totalAmount <= 500:
            discountPercentage = 1
        elif totalAmount <= 1000:
            discountPercentage = 3
        elif totalAmount <= 1500:
            discountPercentage = 5
        elif totalAmount <= 2000:
            discountPercentage = 8
        else:
            discountPercentage = 10

        discountedValue = (totalAmount * discountPercentage) / 100
        finalAmount = totalAmount - discountedValue

        self.customer_info['discountPercentage'] = discountPercentage
        self.customer_info['discountedValue'] = discountedValue
        self.customer_info['finalAmount'] = finalAmount

    def outputData(self):
        customer_info = self.customer_info
        a = ''
        for i in range(customer_info['items']):
            a += f'''
            {str(i + 1)} product = Rs.{customer_info['priceList'][i]} * {customer_info['quantityList'][i]} items 
            Amount : Rs.{customer_info['amountList'][i]} 
            '''

        display = f'''

        {self.initialDisplay()}
        ------------------------------------------------------------------------------------------------------------------------

        Customer Name : {customer_info['customerName']}
        Customer Id : {customer_info['customerId']}
        Customer Address : {customer_info['address']}
        Total Amount : {str(customer_info['totalAmount'])}
        {a}

        Mr/Mrs. {customer_info['customerName']}, you have purchased {customer_info['items']} items whose total price is {customer_info['totalAmount']} and discount is Rs.{customer_info['discountedValue']} with discount rate {customer_info['discountPercentage']}%. So, You have to pay Rs.{customer_info['finalAmount']}

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
