# number = int(input("Enter the number: "))
# factorial = 1

# if (number<0):
#     print("Error: Factorial of Negative number is not defined or possible.")
# elif (number==0):
#     print(1)
# else:
#     for i in range(1, number+1):
#         factorial = factorial*i
#     print(f"The factorial of {number} is {factorial}")




def check_factorial(number):
    factorial = 1

    if (number<0):
        return "Error: Factorial of Negative number is not defined or possible."
    elif (number==0):
        return 1
    else:
        for i in range(1, number+1):
            factorial = factorial*i
        return factorial

number = int(input("Enter the number: "))
result = check_factorial(number)
print(f"The factorial of {number} is {result}")