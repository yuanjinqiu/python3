import psutil
import time
# cpu_usage = psutil.cpu_percent()
# mem_usage = psutil.virtual_memory().percent
#
# print(f"CPU Usage: {cpu_usage}%")
# print(f"Memory Usage: {mem_usage}%")

class get_sys():
    def __init__(self,cpu,mem):
        self.cpu = cpu
        self.mem = mem
    name = "centos"

    def get_cpu(self):
        cpu_usage = psutil.cpu_percent()
        print(f"CPU Usage: {cpu_usage}%")
        print(self.cpu)

cpu1 =get_sys("a")
cpu1.get_cpu()




