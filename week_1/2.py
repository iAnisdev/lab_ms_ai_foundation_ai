str = input("Enter a string to check if it is a palindrome: ")


if str == str[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")