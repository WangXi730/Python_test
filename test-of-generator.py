# 生成器
# 生成器函数返回一个生成器对象，生成器对象可以当作iterator使用，每次next的时候，相当于继续执行，直至下一次yield，第一次返回的生成器对象就是第一次执行到yield时，yield后面的值，在生成器函数中，return相当于迭代器中的StopIteration，如果return了值，需要捕捉这个异常
def gen1(n):
    while(n > 0):
        yield n
        n = n - 1
    return

# 迭代器可以与生成器进行一定程度的配合，使得代码更加简洁
class A:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        idx = 0
        while idx < len(self.value):
            yield self.value[idx]
            idx += 1

# 生成器对象会提供一个send函数，用于在生成器函数中调用yield之后进行返回
# 即：如果在生成器函数中进行操作：tmp = yield xxx，且外界在调用 b = a.send(value)的时候，value会赋值给tmp，b则会等待下一次yield
# 调用next(a)等价于调用a.send(None)
def gen2(n):
    while n > 0:
        tmp = yield n
        if tmp != None:
            n = tmp
        n -= 1

def main():
    print('g1')
    for i in gen1(5):
        print(i)
    print('A')
    a = A([1,2,3,4,5,6,78])
    for i in a:
        print(i)
    print('g2')
    a = gen2(5)
    first = next(a)
    print(f'first a is {first}')
    print(f'second a is {a.send(10)}')
    for i in a:
        print(i)

if __name__ == '__main__':
    main()