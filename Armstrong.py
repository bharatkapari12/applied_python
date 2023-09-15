# number = int(input("Enter: "))
# sum = 0
# order = len(str(number))
# temp=number

# while(number>0):
#     digit = number % 10
#     sum = sum+digit**order
#     number = number//10

# if sum == temp:
#     print(f"{temp} is Armstrong.")
# else:
#     print(f"{temp} is not a Armstrong.")



def check_Armstrong(number):
    sum = 0
    order = len(str(number))
    temp=number

    while(number>0):
        digit = number % 10
        sum = sum+digit**order
        number = number//10

    if sum == temp:
        return f"{temp} is Armstrong."
    else:
        return f"{temp} is not a Armstrong."

number = int(input("Enter: "))
result= check_Armstrong(number)
print(result)
