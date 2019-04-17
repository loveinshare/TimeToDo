import datetime
# 定义一个queue 新增加时间后进行时间排序y

import time
import queue
import threading

def TASK_SORT_TIME():
    pass


class Task():
    def __init__(self, _time, _func):
        self.time = _time
        self.func = _func

datetime.datetime
class time_to_do():
    def __init__(self):
        self.alive = True
        self.taskL = []
        self.taskQ = queue.Queue()

    def get_task(self):
        while self.alive:
            if self.taskQ.empty():
                time.sleep()
            else:
                self.taskL.append(self.taskQ.get())
                self.taskL.sort(TASK_SORT_TIME)
    def main_loop(self):
        while self.alive:
            now=datetime.datetime.now()
            if self.taskL[0].time < now:
                self.taskL[0].func()
                self.taskL.pop(0)
            else:
                time.sleep(0.1)
