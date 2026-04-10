import sys

inval = int(input("数値を入力してください:"))

if inval > 0:
    print("正の整数")
elif inval < 0:
    print("負の整数")
else:   
    print("ZERO")

if inval == 0:
    print("----------")
elif inval % 2 != 0:
    print("奇数")
else:
    print("偶数")

if inval < 2:
    print("素数ではない")
    sys.exit()

for i in range(2, inval):
    if inval % i == 0:
        print("素数ではない")
        sys.exit()
    
print("素数である")