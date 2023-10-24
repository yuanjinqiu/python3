# 示例：统计访问次数
import matplotlib.pyplot as plt
import re

def acc_count():
    with open('access.log','r')as f:
        log_lines = f.readlines()
        access_count = {}
        for line in log_lines:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[([^\]]+)\]', line)
            if match:
                ip = match.group(1)
                if ip in access_count:
                    access_count[ip] += 1
                else:
                    access_count[ip] = 1
        ip_list =  []
        count_list = []
        for ip, count in access_count.items():
            ip_list.append(ip)
            count_list.append(count)

        ip_addresses = ip_list
        access_counts = count_list

        plt.bar(ip_addresses, access_counts)
        plt.xlabel('IP Addresses')
        plt.ylabel('Access Counts')
        plt.title('Access Counts by IP')
        # plt.show()
        name = 'tuu'
        plt.savefig('./' + name)

acc_count()