def check_prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True

number=int(input("Enter: "))
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")