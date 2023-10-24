import  psutil
import os


class systeminfo():

    def get_cpu(self):
        print(psutil.cpu_stats())
    def get_mem(self):
        print(psutil.virtual_memory())
    def get_disk(self):
        print(psutil.disk_usage('/'))

compute =systeminfo()
compute.get_cpu()
compute.get_mem()
