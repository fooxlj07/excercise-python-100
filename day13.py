from _queue import Empty
from datetime import datetime
from multiprocessing import Process, Value, Queue
from threading import Thread, Lock
from time import sleep
from random import randint


def task(task_name: str):
    start = datetime.now()
    print(f"{task_name.upper()} is started: {start}")
    sleep(randint(5, 10))
    end = datetime.now()
    print(f"{task_name.upper()} is ended: {end}")
    print(f"{task_name.upper()} used: {end - start}")


def run_tasks_seq():
    start = datetime.now()
    print("START:", start)
    print("START:", )
    for i in range(2):
        task(f'TASK {i}')
    end = datetime.now()
    print("END:", end)
    print("TOTAL: ", end - start)


def run_tasks_parallel_1():
    start = datetime.now()
    print("START:", start)
    processes = []
    for i in range(2):
        p = Process(target=task, args=(f'task_{i}',))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    end = datetime.now()
    print("END:", end)
    print("TOTAL: ", end - start)


def run_tasks_parallel_2():
    start = datetime.now()
    print("START:", start)
    processes = []
    for i in range(2):
        p = Process(target=task, args=(f'task_{i}',))
        processes.append(p)
        p.start()
        p.join()

    end = datetime.now()
    print("END:", end)
    print("TOTAL: ", end - start)


def run_tasks_in_thread():
    start = datetime.now()
    print("START:", start)
    processes = []
    for i in range(2):
        t = Thread(target=task, args=(f'task_{i}',))
        processes.append(t)
        t.start()
    for t in processes:
        t.join()

    end = datetime.now()
    print("END:", end)
    print("TOTAL: ", end - start)


from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def test_shared_resources():
    account = Account()
    threads = []
    for i in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("the money inside the account is:", account.balance)


import time
import tkinter
import tkinter.messagebox


def try_single_thread():
    class DownloadThread(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('Message', 'download finished')
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadThread(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'Author is jing li')

    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


def test_single_process():

    total = 0
    number_list = [i for i in range(1, 100000001)]
    start = datetime.now()
    for num in number_list:
        total += num
    print(total)
    end = datetime.now()
    print('Single process has used time:', end - start)


def test_multi_processes():
    def task_handler(curr_list, result_queue):
        t = 0
        for i in curr_list:
            t += i
        result_queue.put(t)

    queue = Queue()
    total = 0
    number_list = [i for i in range(1, 100000001)]
    for num in number_list:
        total += num
    processes = []
    index = 0
    for i in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = datetime.now()
    for p in processes:
        p.join()
    while not queue.empty():
        total += queue.get()
    print(total)
    end = datetime.now()
    print('Multi process has used time:', end - start)


if __name__ == '__main__':
    test_single_process()
    test_multi_processes()
