number = int(input("Enter input: "))
temp = number
reverse = 0

while(number>0):
    digit = number%10
    reverse = reverse*10+digit
    number = number//10

if temp==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")




def palindrome(number):
    reverse = 0
    temp = number
    
    while number>0:
        digit = number%10
        reverse = reverse *10+digit
        number = number // 10
    
    if temp == reverse:
        return f"{temp} is a Palindrome number"
    else:
        return f"{temp} is not a Palindrome number"

number = int(input("Enter the number: "))
result = palindrome(number)
print(result)