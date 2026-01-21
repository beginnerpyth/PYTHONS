number = int(input("enter the prime number"))
prime_flag = True
for x in range(number):
    if x == 0 or x == 1:
     pass
    elif number % x == 0:
     prime_flag = False
    if prime_flag and number > 1:
        print("number is prime",number)
    else:
        print("number isnot prime",number)