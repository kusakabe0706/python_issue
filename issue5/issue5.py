inval = int(input("何段？"))
print("--------------------")

for i in range(1, inval + 1):
    spaces = " " * (inval - i)
    stars = "*" * (i * 2 - 1)
    print(spaces + stars)