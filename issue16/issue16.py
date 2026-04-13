import sys

print("計算式を入力")

input_data = input().split()

if len(input_data) != 3:
    print("エラー")
    

try:
    input_val1 = int(input_data[0])
    operator = input_data[1]
    input_val2 = int(input_data[2])
except ValueError:
    print("エラー")
    sys.exit()

match operator:
    case '+':
        ans = input_val1 + input_val2
    case '-':
        ans = input_val1 - input_val2
    case '*':
        ans = input_val1 * input_val2
    case '/':
        if input_val2 == 0:
            print("0では割れません")
            sys.exit()
        ans = input_val1 / input_val2
    case _:
        print("エラー")
        sys.exit()
    
print(f"result={ans}")