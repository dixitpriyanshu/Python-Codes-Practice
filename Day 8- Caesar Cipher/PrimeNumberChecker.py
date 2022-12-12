# def prime_checker(number):
#     is_Prime=True
#     for i in range(2,number):
#         if number%i==0:
#             is_Prime=False
#     if is_Prime:
#         print("It's a prime number.")
#     else:    
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

import math

def prime_checker(number):
    sqrt = math.ceil(math.sqrt(number))
    for i in range(2,sqrt):
        if number%i==0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")        


n = int(input("Check this number: "))
prime_checker(number=n)

