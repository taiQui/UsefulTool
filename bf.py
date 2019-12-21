import requests
from threading import Thread

def BF(function,STEP=120,nbThread=10,filename=None):
    class ExecuteThread(Thread):
        def __init__(self,liste,elemtofind=None):
            Thread.__init__(self)
            self.liste = liste
            #self.etf = elemtofin
        def run(self):
            for i in self.liste:
                function(i)

    # if file to read ##
    with open(filename) as f:
        file = f.read().split('\n')
    # Liste de thread
    tl = []
    min = 0
    max = STEP
    step = STEP
    end = False
    while not end:
        if len(tl) < nbThread :
            tl.append(ExecuteThread(file[min:max]))
            tl[-1].start()
            min += STEP
            max += STEP
        end = True
        i = 0
        while i <len(tl):
            if not tl[i].is_alive():
                tl = tl[:i]+tl[i+1:]
            else:
                end = False
                i+=1
####### EXEMPLE #########
# Exemple with brute web auth !
# def a(elem):
#     for i in liste:
#         sess = requests.Session()
#         sess.get('http://google.com')
#         data = {"a":elem}
#         r = sess.post('http://google.com',data=data)
#         if "yolo" in r.text:
#             print("yolo")
#         else:
#             print("fail")
#
# BF(a,filename="yolo")
