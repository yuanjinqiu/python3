import threading
import time

def sing():
    for i in range(3):
        print('唱歌')
        time.sleep(1)

def dance():
    for i in range(3):
        print('跳舞')
        time.sleep(1)

def main():
    sing_thread = threading.Thread(target=sing)
    # dance_thread = threading.Thread(target=dance,daemon=True)
    #
    sing_thread.start()
    # dance_thread.start()


if __name__ == '__main__':
    main()