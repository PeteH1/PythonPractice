# Record input & declare "iterations" variable
input_num_str = (input("Enter a number: \n"))
iterations = 0

while int(input_num_str) != 0: # This condition isn't important as long as it returns True
    # Setting variables
    input_num = int(input_num_str)
    r_num = 0
    r_num_str = ""

    # Reverse the input number
    count = len(str(input_num))
    while count > 0:
        count -= 1
        r_num_str = r_num_str + input_num_str[count]

    # Check for a palindrome
    if r_num_str == input_num_str:
        print("Palindrome reached in " + str(iterations) + " iterations.")
        break

    # Add numbers together & print
    r_num = int(r_num_str)
    sum = input_num + r_num
    print(input_num_str + " + " + r_num_str + " = " + str(sum))
    
    # Record iteration
    iterations += 1
    
    # Save sum as new input
    input_num_str = str(sum)
    
input("Press Enter to exit")