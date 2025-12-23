import asyncio
import threading
import time

def bg():
    while True:
        time.sleep(1)
        print(f"logging")
        
async def fetch_orders():
    await asyncio.sleep(3)
    print("order fetched")
    
    
threading.Thread(target=bg , daemon=True).start()

asyncio.run(fetch_orders())            
        
        