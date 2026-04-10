import sys

count = 0
total = 0
ave = 0
inval = int(input("数値を入力(0で終了)："))

if inval == 0:
    print("終了")
    sys.exit()

while(1):
    if inval != 0:
        total += inval
        count += 1
    elif inval == 0:
        ave = total / count
        print(f"平均={ave}")
        sys.exit()
    
    inval = int(input("数値を入力(0で終了)："))