class A():
    def f1(self):
        print("F1")
class B(A):
    def f2(self):
        print("F2")
x = B()
x.f1()
x.f2()