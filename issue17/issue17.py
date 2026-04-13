import threading

mutex = threading.Lock()

def add_thread(result_list):
    if result_list is not None:
        with mutex:
            result_list[0] += 1

def main():
    try:
        input_val = int(input("数値を入力:"))
    except ValueError:
        print("数値を入力してください")
        return
    
    data = [input_val]

    thread = threading.Thread(target=add_thread, args=(data,))

    thread.start()

    thread.join()

    print(f"result={data[0]}")

if __name__ == "__main__":
    main()