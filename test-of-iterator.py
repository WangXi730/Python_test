# 两个概念：iterator和iterable
# 其中 iterator 是一个具有状态的类型，且其本身并不需要存储数据，而iterator则是一个类似于container，没有状态，负责存储数据
# iterator需要实现next操作，需要返回当前迭代器指向的值，并且将迭代器往后移动一次，当迭代器无法向后移动时，需要raise一个StopIteration异常
# iterable需要实现iter操作，这个操作返回迭代的第一个对象
# 在python的要求中，建议每个iterator都是一个iterable，遵守这个建议是比较好的，在iterator实现iter操作时，返回自己即可
# 在for loop中，in后面的，必须是一个iterable
# 在下面的例子中，A是iterable，B是A的iterator
class B:
    def __init__(self,value):
        self.value = value
        self.idx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.value) > self.idx:
            self.idx = self.idx + 1
            return self.value[self.idx - 1]
        else:
            raise StopIteration
class A:

    def __init__(self,container):
        self.value = list(container)

    def __iter__(self):
        return B(self.value)

def main():
    a = A({1,2,3,4,5,6,7})
    # b = iter(a)
    # print(next(b))
    # print(next(b))
    for i in a:
        print(i)


if __name__ == '__main__':
    main()
