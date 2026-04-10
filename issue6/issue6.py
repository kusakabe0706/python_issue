MAX = 1000

f1 = 0
f2 = 1
next_val = 0

while True:
    if f1 < MAX:
        print(f1, end="")
        
        if f2 < MAX:
            print(",", end="")
    else:
        break
        
    next_val = f1 + f2
    f1 = f2
    f2 = next_val

print()