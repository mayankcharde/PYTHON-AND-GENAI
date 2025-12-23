from multiprocessing import Process
import time


def cpu_heavy():
    print(f"crunching some numbers")
    total = 0
    for i in range(10**9):
        total+=i
        print("done")
        
if __name__ == "__main__":
    start = time.time()
    proccess = [Process(target=cpu_heavy) for _ in range(2)] 
    [p.start() for p in proccess]
    [p.join() for p in proccess]
    print(f"Time taken: {time.time() - start:.2f} seconds")
