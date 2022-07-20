class A():
    def f1(self):
        print("F1")
class B(A):
    def f2(self):
        print("F2")
class C(B):
    def f3(self):
        print("F3")
x = C()
x.f1()
x.f2()
x.f3()