# 正負判定用
def print_pos(n): print("正の整数")
def print_neg(n): print("負の整数")
def print_zero(n): print("ZERO")

# 奇数偶数判定用
def print_even(n): print("偶数")
def print_odd(n): print("奇数")
def print_z(n): print("------------")

# 素数判定用
def prime(n): print("素数である")
def not_prime(n): print("素数ではない")


# 入力を受け取る
input_num = int(input("数値を入力："))

# 関数をそのままリスト（配列）に格納する（これがテーブルになります）
table_1 = [print_pos, print_neg, print_zero]
table_2 = [print_even, print_odd, print_z]
table_3 = [prime, not_prime]

is_not_prime = 0

# --- 正負判定 ---
if input_num > 0:
    judge1 = 0
elif input_num < 0:
    judge1 = 1
else:
    judge1 = 2

# テーブルから関数を取り出して、カッコをつけて呼び出す
table_1[judge1](input_num)


# --- 奇数偶数判定 ---
if input_num == 0:
    judge2 = 2
elif input_num % 2 != 0:
    judge2 = 1
else:
    judge2 = 0

table_2[judge2](input_num)


# --- 素数判定 ---
if input_num < 2:
    is_not_prime = 1

# 2 から input_num の直前まで繰り返す
for i in range(2, input_num):
    if input_num % i == 0:
        is_not_prime = 1
        break 

table_3[is_not_prime](input_num)