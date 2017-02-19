print("Printing first 10 prime numbers")

def is_prime(number):
    if number>0:
        for i in range(2,number):
            if number % i == 0:
                return False
                break
        else:
            return True

k = 0
while k<10:
    for u in range(100):
        if is_prime(u)==True and k<10:
            print(u)
            k += 1
