import schedule
import time
from schedule import Job

def j():
    print("Task executed")

# 每隔一段时间执行一次任务
#schedule.every(10).seconds.do(job)  # 每10秒执行一次

# # 每分钟执行一次任务
# schedule.every().minute.do(job)  # 每分钟执行一次
#
# # 每小时执行一次任务
# schedule.every().hour.do(job)  # 每小时执行一次
#
# # 每天中午12点执行任务
# schedule.every().day.at("12:00").do(job)  # 每天中午12点执行
#
# # 每周一早上8点执行任务
# schedule.every().monday.at("08:00").do(job)  # 每周一早上8点执行


#执行定时任务
# while True:
#     schedule.run_pending()
#     time.sleep(1)

#
# job = schedule.every().minute.do(job)
# # 取消任务
# schedule.cancel_job(job)


from schedule import Job

# 创建一个任务，每隔10秒执行一次，最多执行3次
job = Job(interval=10,retrying=3)
job.do(lambda: print("Task executed"))











