import queue
from threading import Thread


class Work (Thread):
    def __init__(self,thread_id,func,pq=None,uq=None,stop=None):
        Thread.__init__(self)
        self.func = func
        self.uq = uq
        self.pq = pq
        self.id = thread_id
        self.STOP = stop
    def run(self):
        if self.pq is not None and self.uq is not None:
            self.run_both(self.pq,self.uq)
        elif self.pq is not None:
            self.run_unique(self.pq)
        elif self.uq is not None:
            self.run_unique(self.uq)
        else:
            raise("No item given")

    def run_unique(self,itemqueue):
        while True:
            if self.STOP[0]:
                return
            item = None
            try:
                item = itemqueue.get(timeout=1)
            except queue.Empty:
                return
            try:
                if self.func(item):
                    itemqueue.task_done()
                    self.STOP[0] = True
                    return
            except:
                raise
            itemqueue.task_done()
    def run_both(self,pqueue,uqueue):
        while True:
            if self.STOP[0]:
                return
            username = None
            password = None
            try:
                username = uqueue.get(timeout=1)
            except queue.Empty:
                return
            try:
                for psswd in pqueue:
                    if self.STOP[0]:
                        uqueue.task_done()
                        return
                    if self.func(username,psswd):
                        self.STOP[0] = True
            except:
                raise
            uqueue.task_done()



class BF:
    def __init__(self,func,item1=None,item2=None,thread=10):
        self.username = None
        self.password = None
        self.thread=thread
        if item1 is not None:
            with open(item1,'r') as f:
                self.username = f.read().splitlines()
        if item2 is not None:
            with open(item2,'r') as f:
                self.password = f.read().splitlines()
        self.Execute(func)

    def Execute(self,func):
        uqueue = None
        pqueue = None
        STOP = [False]
        if self.username is not None:
            uqueue = queue.Queue()
            for user in self.username:
                uqueue.put(user)
        if self.password is not None:
            if self.username is not None:
                pqueue = self.password
            else:
                pqueue = queue.Queue()
                for psswd in self.password:
                    pqueue.put(psswd)
        threads = []
        if self.username is not None and self.password is not None:
            for i in range(self.thread):
                worker = Work(i,func,pq=pqueue,uq=uqueue,stop=STOP)
                worker.setDaemon(True)
                worker.start()
                threads.append(worker)
        elif self.username is not None:
            for i in range(self.thread):
                worker = Work(i,func,uq=uqueue,stop=STOP)
                worker.setDaemon(True)
                worker.start()
                threads.append(worker)
        elif self.password is not None:
            for i in range(self.thread):
                worker = Work(i,func,pq=pqueue,stop=STOP)
                worker.setDaemon(True)
                worker.start()
                threads.append(worker)
        else:
            raise Exception('No username/password given')
        if uqueue is not None:
            uqueue.join()
        for thread in threads:
            thread.join()
        print("[*] DONE")


if __name__ == "__main__":
    def a(item1,item2):
        if item1 == "998" and item2 == "700":
            print("[+] Success")
    BF(a,item1="testdic",item2="testdic",thread=100)
