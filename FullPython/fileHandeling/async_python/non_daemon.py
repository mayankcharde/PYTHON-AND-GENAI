import threading
import time

def monitor_tea_temp():
    while True:
        print(f"monintoring tea temp")
        time.sleep(2)
        
t= threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()
# t.join()
print("main program done ")        