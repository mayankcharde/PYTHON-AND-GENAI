from multiprocessing import Process, Value


def increment(counter):
    for _ in range(10000):
        with counter.ge_lock():
            counter.value+=1
            
if __name__ == "__main__":
    counter = Value('i', 0)
    proccesses = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in proccesses]
    [p.join() for p in proccesses]
    
    print("final counter value:", counter.value)            