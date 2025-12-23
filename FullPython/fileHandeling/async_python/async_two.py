import asyncio
import time

async def brew(name):
    print(f"brewing {name}")
    await asyncio.sleep(3)
    
    print(f"{name} is ready")
    
async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("lemon chai"),
        brew("ginger chai"),
    )    
    
asyncio.run(main())    