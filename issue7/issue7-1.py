def change(t1, t2):
    t1[0], t2[0] = t2[0], t1[0]

input_val1, input_val2 = map(int,input("2つの数値を入力：").split())
print(f"{input_val1}→{input_val2}")

val1 = [input_val1]
val2 = [input_val2]

change(val1, val2)
print(f"{val1[0]}→{val2[0]}")