import multiprocessing
import time
# def sing():
#     for i in range(3):
#         print('唱歌')
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print('跳舞')
#         time.sleep(1)
#
# def main():
#     sing_process = multiprocessing.Process(target=sing)
#     dance_process = multiprocessing.Process(target=dance)
#
#     sing_process.start()
#     dance_process.start()
#
# if __name__ == '__main__':
#     main()



# 进程传参
"""
args：以元组方式传参
kwargs: 以字典方式传参
"""
def sing(num,a):
    for i in range(num):
        print('唱歌')
        time.sleep(a)

def dance(num,name):
    for i in range(num):
        print('%s 跳舞' %name)
        time.sleep(1)

def main():
    sing_process = multiprocessing.Process(target=sing,args=(3,3))
    dance_process = multiprocessing.Process(target=dance,kwargs={"num":3,"name":"xiaoming"})

    sing_process.start()
    dance_process.start()

if __name__ == '__main__':
    main()
#
#




#进程PID

import os

# def sing(num):
#     print(os.getpid())
#     print(os.getppid())
#     for i in range(num):
#         print('唱歌')
#         time.sleep(1)
#
# def dance(name):
#     for i in range(3):
#         print('%s 跳舞' %name)
#         time.sleep(1)
#     print(os.getpid())
#     print(os.getppid())
#
# def main():
#     sing_process = multiprocessing.Process(target=sing,args=(3,))
#     dance_process = multiprocessing.Process(target=dance,kwargs={"name":"xiaoming"})
#
#     sing_process.start()
#     dance_process.start()
#
# if __name__ == '__main__':
#     print("主进程pid：%s" %os.getpid())
#     main()