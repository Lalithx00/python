def reverse(s):
    num=s
    result = 0
    while num > 0:
        id=num%10
        result = (result * 10 )+ id
        num = num // 10
    return result

s=int(input("Enter a number: "))
print("Reverse:",reverse(s))