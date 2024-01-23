class A:
    def displayA(self):
        print("welcome ashoka 1")

class B(A):
    def displayB(self):
        print("welcome ashoka 2")

class C(B):
    def displayC(self):
        print("welcome ashoka 3")


class D(C):
    def displayD(self):
        print("hye")


# l = C()
# l.displayA()
# l.displayB()
# l.displayC()


x = D()
x.displayA()
x.displayB()
x.displayC()
x.displayD()
