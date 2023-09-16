def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even number")
    else:
        print(f"{number} is Odd number")

user_input=int(input("Enter the number: "))
odd_even(user_input)