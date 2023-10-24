import psutil

def color(a,b,c):
    print("\33[1;{};40m{}:{}G\33[0m".format(a,b,c))

def mem():
    mem = psutil.virtual_memory()
    total = int(mem.total/1024/1024/1024)
    used =  int(mem.used/1024/1024/1024)
    Mem_free =  int(mem.free/1024/1024)
    color(32,"总内存:",total)
    color(33, "使用内存:", used)
    color(34, "剩余内存:", Mem_free)


def disk():
    disk =  psutil.disk_usage('/')
    print(disk)

#CPU
import psutil as p
cpu_info = psutil.cpu_times()
print(p.cpu_count())
print(p.cpu_percent())
print(p.cpu_stats())
print(p.cpu_times_percent())



#内存
#磁盘
#网络
net = psutil.net_if_addrs()


#进程
import psutil as p
def get_process():
    pid_num = p.pids() #获取进程的pid
    print(pid_num)
    print(len(pid_num))
    for i in range(2,len(pid_num)):
        pro = p.Process(pid_num[i])
        print(pro)
        print(pro.pid)
        print(pro.name())
        print(pro.username())
        print(pro.status())
        print(pro.exe())
        print(pro.ppid())
        print(pro.children())
        print(pro.create_time())









