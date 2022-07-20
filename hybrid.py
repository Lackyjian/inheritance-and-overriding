class A():
    def f1(self):
        print("F1")
class B(A):
    def f2(self):
        print("F2")
class C(A):
    def f3(self):
        print("F3")
class D(B,C):
    def f4(self):
        print("F4")
x = D()
x.f1()
x.f2()
x.f3()
x.f4()