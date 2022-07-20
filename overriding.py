class A():
    def f1(self):
        print("F1")
class B(A):
    def f1(self):
        print("F2")
x = B()
x.f1()