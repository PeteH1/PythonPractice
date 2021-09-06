number = int(input("Enter a number: \n"))
iterations = 0

while str(number) != str(number)[::-1]:
    number = number + int(str(number)[::-1])
    iterations += 1
    print(number)
print("Palindrome reached in " + str(iterations) + " iterations.")

input("Press Enter to exit")