def scan_thread(callback):
    print("入力待ち")
    local_arr = input()

    if callback is not None:
        callback(local_arr)