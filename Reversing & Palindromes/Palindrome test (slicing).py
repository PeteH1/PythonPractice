input_string = input("Don't you dare type a palindrome here... \n")
reverse_string = input_string[::-1]

if reverse_string == input_string:
    print("I can't believe you've just done that")
else:
    print("Phew, thank you.")