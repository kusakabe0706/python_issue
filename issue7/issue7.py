def double_value(ans_list):
    ans_list[0] *= 2

inval = int(input("数値を入力："))
data_list = [inval]
double_value(data_list)
print(f"result={data_list[0]}")