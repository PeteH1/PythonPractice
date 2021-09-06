test_number = int(input("WeLcOmE tO pEtE's MaGnIfiCeNt PrImE nUmBeR tEsT!!!! <3 <3 <3 \nEnter your number: "))
divisor = 2

if test_number <=2:
    print("NO IT NEEDS TO BE BIGGER THAN 2!!!!!!1!!")

while test_number > divisor:
    remainder = test_number % divisor
    divisor += 1
    if remainder == 0:
        print(str(test_number) + " is not a Prime Number. \nWhat a crushing disappointment :'(")
        break
if divisor >= test_number > 2:
    print(str(test_number) + " is a Prime Number!!! Hooray!! <3")

input("Press Enter to exit")