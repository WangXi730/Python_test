import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.value = 0
        self.name = name
        self.threadID = threadID

    def run(self):
        print('{} strat'.format(self.threadID))
        Task(self.name,self.threadID)
        print('{} end'.format(self.threadID))

def Task(name, threadID):
    value = 1
    while value < 100:
        print("{} {} {}".format(name,threadID,value))
        value += 1
        time.sleep(1)

def main():
    # 创建线程对象
    t1 = myThread(1,'t1')
    t2 = myThread(2,'t2')
    # 开始执行任务
    t1.start()
    t2.start()
    # 等待
    t1.join()
    t2.join()
    # 结束
    print('退出')

if __name__ == '__main__':
    main()

