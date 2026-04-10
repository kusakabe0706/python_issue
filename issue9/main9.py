from func9 import double_value

def main():
    # 1. 入力を受け取る
    input_num = int(input("数値を入力\n"))

    # 2. 関数を呼び出し、戻り値で上書きする（ポインタの代わり）
    input_num = double_value(input_num)

    # 3. 結果を表示する
    print(input_num)

if __name__ == "__main__":
    main()