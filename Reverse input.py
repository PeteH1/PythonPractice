input_string = input("Type something in and this will reverse it:\n")
count = len(input_string)
reverse_string = ""

while count > 0:
    count -= 1
    reverse_string = reverse_string + input_string[count]

print(reverse_string)
    