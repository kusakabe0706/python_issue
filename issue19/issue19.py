import threading

cond = threading.Condition()

w_id = 0
end = False

def worker1():
    global w_id, end

    while True:
        with cond:
            while w_id != 1 and not end:
                cond.wait()
            
            if end:
                break

            print("スレッド1動作中")

            w_id = 0

def worker2():
    global w_id, end

    while True:
        with cond:
            while w_id != 2 and not end:
                cond.wait()
            
            if end:
                break

            print("スレッド2動作中")

            w_id = 0

def main():
    global w_id, end

    w1 = threading.Thread(target=worker1)
    w2 = threading.Thread(target=worker2)

    w1.start()
    w2.start()

    print("スレッド1を動かす:1, スレッド2を動かす:2, 終了:3")

    while True:
        try:
            input_num = int(input())
        except ValueError:
            input_num = 0

        with cond:
            if input_num == 1:
                w_id = 1
            elif input_num == 2:
                w_id = 2
            elif input_num == 3:
                end = True
            else:
                print("error")
                w_id = 0
            
            cond.notify_all()
        
        if input_num == 3:
            break
    
    w1.join()
    w2.join()

    print("終了")

if __name__ == "__main__":
    main()