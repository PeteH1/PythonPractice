input_string = input("Don't you dare type in a palindrome... \n")
count = len(input_string)
reverse_string = ""

while count > 0:
    count -= 1
    reverse_string = reverse_string + input_string[count]

if input_string == reverse_string:
    print("Wow okay just ignore me then")
else:
    print("Phew, for a minute there I thought you were going to type in a palindrome")
    