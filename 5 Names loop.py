print("Enter 5 names right now or else I'll come over there and make you enter them")
name1 = input("Name 1:")
name2 = input("Name 2:")
name3 = input("Name 3:")
name4 = input("Name 4:")
name5 = input("Name 5:")

name_list = [name1, name2, name3, name4, name5]

count = 0
while count < 5:
    print(name_list[count] + " is awesome!")
    count += 1

input("Press Enter to exit")