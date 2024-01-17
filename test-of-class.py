def func(a):
    def res(*args):
        print(a)
        return a(*args)
    return res

@func
def f2(a,b):
    return a + b

def main():
    print(f2(1,2))


if __name__ == '__main__':
    main()
