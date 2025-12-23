import asyncio

async def brew_chai():
    print("brewing tea")
    await asyncio.sleep(2)
    print("chai is ready")
    
asyncio.run(brew_chai())    