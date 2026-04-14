import threading
from thread18 import scan_thread

cond = threading.Condition()

is_ready = False
res_arr = ""

def cb(ans):
    global is_ready, res_arr

    with cond:
        res_arr = ans
        is_ready = True

        cond.notify_all()

def main():
    thread = threading.Thread(target=scan_thread, args=(cb,))
    thread.start()

    with cond:
        while not is_ready:
            cond.wait()

    print(f"result={res_arr}")

    thread.join()

if __name__ == "__main__":
    main()