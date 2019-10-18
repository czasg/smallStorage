import asyncio, time

"""
运行协程，有三种方法：
asyncio.run(main())  # 单纯的运行协程是不会有异步效果的，这里里能放一个函数
await  # 直接等待一个协程，这样等待也不是异步的，除非是任务
asyncio.create_task()  # 把协程创建为任务
可等待对象有三中类型：协程、任务、Feature
任务：会被排入日程进入异步执行
Feature：是低层级的可等待对象目标是一个异步操作的 最终结果。当一个Feature被等待表示协程将保持知道该Feature操作完毕

并发运行任务
asyncio.gather()
"""
def inner_generator():
    i = 0
    while True:
        i = yield i
        if i > 10:
            raise StopIteration
def outer_generator():
    print("do something before yield")
    from_inner = 0
    from_outer = 1
    g = inner_generator()
    g.send(None) # 执行inner_generator的代码，直到yield
    while 1:
        try:
            from_inner = g.send(from_outer)
            from_outer = yield from_inner  # from_outer会接受send传递过来的值，并继续往下执行代码
        except StopIteration:
            break
def main():
    g = outer_generator()
    g.send(None)  # 这里第一次调用send，必须使用None，调用之后，会从outer_generator的第一行代码开始执行，直到yield
    i = 0
    while 1:
        try:
            i = g.send(i + 1) #会将i+1 传递给outer_generator中的from_outer变量
            print(i)
        except StopIteration:
            break
if __name__ == '__main__':
    main()