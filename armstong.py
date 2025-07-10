def is_armstrong(n):
    original = n
    digits = 0
    temp = n

    while temp > 0:
        digits += 1
        temp //= 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == original


n=int(input("Enter a number: "))

if (is_armstrong(n)==True):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
