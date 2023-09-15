# Develop a software for bhatbhaateni using dictionary, for-lop, function.

import datetime

heading='''
        Sunway College Bhatbhateni System
              Maitidevi,Kathmandu    
'''

Customer={}

def InitialDisplay(heading):
    print(heading)
   
def initialInformation():
    n = int(input("Enter the number of customers: "))
    customer_data = {}
    # first for loop for different customers
    for i in range(n):
        customer_data[i] = {}
        # input for details
        customer_data[i]['name'] = input(f"Enter the name of customer [{i+1}]: ")
        customer_data[i]['address'] = input(f"Enter the address of customer [{i+1}]: ")
        customer_data[i]['email'] = input(f"Enter the email of customer [{i+1}]: ")
        itemno = int(input(f"Enter the number of items of customer : "))
        customer_data[i]['items'] = {}
        customer_data[i]['total'] = 0
        for j in range(itemno):
            itemname = input(f"Enter the name of item [{j+1}]: ")
            itemprice = int(input(f"Enter the price of item [{j+1}]: "))
            itemqty = int(input(f"Enter the quantity of item [{j+1}]: "))
            print("\n")
            customer_data[i]['items'][j] = {'item_name': itemname,'item_price': itemprice, 'item_qty': itemqty, 'total': itemprice*itemqty}
            customer_data[i]['total'] += itemprice*itemqty
    return customer_data


def calculation(customer_data):
    for i in range(len(customer_data)):
        totalPrice = customer_data[i]['total']
        # discount calculation
        discount = 0
        if totalPrice <= 5000:
            discount = totalPrice * 0.05
        elif totalPrice <= 7000:
            discount = (5000 * 0.05) + (totalPrice - 5000) * 0.08
        elif totalPrice <= 10000:
            discount = (5000 * 0.05) + (2000 * 0.08) + (totalPrice - 7000) * 0.10
        else:
            discount = (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (totalPrice - 10000) * 0.15
        # net amount after discount
        netAmount = totalPrice - discount
        customer_data[i]['net_total'] = netAmount
        customer_data[i]['discount'] = discount
    return customer_data

       
def display_bill(customer_data):
    for i in range(len(customer_data)):
        print("Customer Name: ", customer_data[i]['name'])
        print("Customer Address: ", customer_data[i]['address'])
        print("Customer Email: ", customer_data[i]['email'])
        print("\n")
        print("{:<20} {:>10} {:>15} {:>15}".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
        for j in range(len(customer_data[i]['items'])):
            print("{:<20} {:>10} {:>15} {:>15}".format(customer_data[i]['items'][j]['item_name'], customer_data[i]['items'][j]['item_price'], customer_data[i]['items'][j]['item_qty'], customer_data[i]['items'][j]['total']))
        print("\nDiscount: ", customer_data[i]['discount'])
        print("Net Total: ", customer_data[i]['net_total'])
        print("\n")

def print_bill_to_file(customer_data,heading):
    for i in range(len(customer_data)):
        filename = "bill_"+customer_data[i]['name']+"_"+str(datetime.datetime.now().date())+".txt"
        with open(filename, 'w') as bill_file:
            bill_file.write(heading)
            bill_file.write("Customer Name: "+ customer_data[i]['name']+'\n')
            bill_file.write("Customer Address: "+ customer_data[i]['address']+'\n')
            bill_file.write("Customer Email: "+ customer_data[i]['email']+'\n\n')
            bill_file.write("{:<20} {:>10} {:>15} {:>15}\n".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
            for j in range(len(customer_data[i]['items'])):
                bill_file.write("{:<20} {:>10} {:>15} {:>15}\n".format(customer_data[i]['items'][j]['item_name'], customer_data[i]['items'][j]['item_price'], customer_data[i]['items'][j]['item_qty'], customer_data[i]['items'][j]['total']))
            bill_file.write("\nDiscount: "+ str(customer_data[i]['discount'])+'\n')
            bill_file.write("Net Total: "+ str(customer_data[i]['net_total'])+'\n')
    print("Bills generated and saved successfully.")

def main():
    InitialDisplay(heading)
    customer_data = initialInformation()
    customer_data = calculation(customer_data)
    InitialDisplay(heading)
    display_bill(customer_data)
    print_bill_to_file(customer_data,heading)

if __name__ == "__main__":
    main()







