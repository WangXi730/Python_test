# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 定义一个装饰器函数
def add_tag(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
# 定义一个类装饰器
def my_class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            print("This is a new method added to the class")

    return NewClass

@my_class_decorator
class A:
    @add_tag
    def public_method(self):
        print("This is a public method")
    def _private_method(self):
        print("This is a private method")

def main():
    a = A()
    a.public_method()
    a._private_method()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
