class A():
    def f1(self):
        print("F1")
class B():
    def f2(self):
        print("F2")
class C(A,B):
    def f3(self):
        print("F3")
x = C()
x.f1()
x.f2()
x.f3()