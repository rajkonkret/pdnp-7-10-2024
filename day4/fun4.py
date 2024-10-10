# funkcja wewnętrzna, zagnieżdzona
# dekoraatory wykorzustują zasadę funkcji wewnętrznej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun1()  # To jest fun1
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000001D3FF038CC0>
print(type(xFun))  # <class 'function'>
xFun()  # fun2()
# <class 'function'>
# To jest fun2
