import random

lottery_number = random.randint(10, 99)
print('The lottery number is', lottery_number,'.')

user_input = int(input("(1st) Enter a two-digit number (e.g., 45): "))

# Extract digits from the lottery number and user input
lottery_digit1 = lottery_number // 10
lottery_digit2 = lottery_number % 10
user_digit1 = user_input // 10
user_digit2 = user_input % 10

# Check for the exact match
if user_input == lottery_number:
    prize = 10000
elif (user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2) and \
     (user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2):
    prize = 3000
elif (user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2 \
        or user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2):
    prize = 1000
else:
    prize = 0

# Display the result
print(f"Lottery Number: {lottery_number}")
print(f"Your Number: {user_input}")

if prize > 0:
    print(f"Congratulations! You've won ${prize}.")
else:
    print("Sorry, you didn't win.")









# # 2nd way

# import random

# lottery_number = str(random.randint(10, 99))

# user_input = input("(2nd) Enter a two-digit number (e.g., 45): ")

# if user_input == lottery_number:
#     prize = 10000
# else:
#     # Check for partial matches
#     matched_digits = 0
#     for digit in user_input:
#         if digit in lottery_number:
#             matched_digits += 1

#     if matched_digits == 2:
#         prize = 3000
#     elif matched_digits > 0:
#         prize = 1000
#     else:
#         prize = 0

#     # Display the result
#     print(f"Lottery Number: {lottery_number}")
#     print(f"User Input: {user_input}")

#     if prize > 0:
#         print(f"Congratulations! You've won ${prize}.")
#     else:
#         print("Sorry, you didn't win. Try again!")






# # 5th way

# import random

# # Generate a random two-digit lottery number
# lottery_number = str(random.randint(10, 99))

# # Generate a random two-digit user input
# user_input = input("Enter a two-digit number (e.g., 45): ")

# # Check for an exact match
# if user_input == lottery_number:
#     prize = 10000
# else:
#     # Extract digits from both numbers
#     user_digit1, user_digit2 = int(user_input[0]), int(user_input[1])
#     lottery_digit1, lottery_digit2 = int(lottery_number[0]), int(lottery_number[1])

#     # Check for partial matches
#     if (user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2) and \
#        (user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2):
#         prize = 3000
#     elif user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2 \
#             or user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2:
#         prize = 1000
#     else:
#         prize = 0

# # Display the result
# print(f"Lottery Number: {lottery_number}")
# print(f"User Input: {user_input}")
# if prize > 0:
#     print(f"Congratulations! You've won ${prize}.")
# else:
#     print("Sorry, you didn't win. Try again!")

