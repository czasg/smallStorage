import time
import datetime


def timed_task(task, day=0, hour=0, minute=0, second=0):
    timer = day*24*60*60 + hour*60*60 + minute*60 + second
    while True:
        print('now is {}'.format(datetime.datetime.now()))
        print('waiting {} seconds...'.format(timer))
        time.sleep(timer)
        task()


    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         if now.minute == 27:
    #             break
    #         print("waiting for time to execute code")
    #         time.sleep(60)
    #     MySpider.cza_run_spider()