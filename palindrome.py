def palindrome(s):
    
    stack = []
    for char in s:
        stack.append(char)

    for char in s:
        if char != stack.pop():
            return False
    return True

s=input("Enter a input: ")
if palindrome(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")