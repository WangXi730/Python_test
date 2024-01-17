import asyncio
import time

# 使用async关键词定义coroutine function
# 当运行一个coroutine function的时候，并不会运行这个function里面的代码，而是会返回一个coroutine object
# 要运行一个coroutine function里面的代码，需要把coroutine转化为task，交给event loop，等待event loop调度执行
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def say_after2(delay,what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():

    # await后面可以跟future（task继承自future）或者coroutine
    print(time.strftime('%X'))

    await say_after(1,'hello')
    await say_after(2,'world')

    print(time.strftime('%X'))

    # 但如果提前将coroutine变成task，就可以看到，等待时间是一起等待的
    task1 = asyncio.create_task(say_after(1,'hello'))
    task2 = asyncio.create_task(say_after(2,'world'))

    print(time.strftime('%X'))

    await task1
    await task2

    print(time.strftime('%X'))
    
    # 使用 ans = await task是可以接收task运行的结果的，res是一个future
    # 使用 asyncio.gather()可以把多个task的返回结果组织成一个list
    # asyncio.gather()会把参数中的所有coroutine转化为task再传入
    
    print(time.strftime('%X'))
    
    ans = await asyncio.gather(say_after2(1,'hello'),say_after2(2,'world'))
    
    print(f'{ans}')
    
    print(time.strftime('%X'))
    



if __name__ == '__main__':
    coro = main() #这里并不会执行main，而是会返回一个coroutine object
    asyncio.run(coro)
