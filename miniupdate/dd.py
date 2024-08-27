import threading 
def hello(n):
    for i in range(16):
        print("hello",n)
def world(w):
    for i in range(15):
        print("world",w)
t1 = threading.Thread(target=hello,args=("deva",))
t2 = threading.Thread(target=world,args=("crypt",))
t1.start()
t2.start()
t1.join()
t2.join()
