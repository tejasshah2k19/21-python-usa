class A:
    a = 12 #
    def add(self):
        self.a = 20
        print("add from A class",self.a)
class C:
    def mul(self):
        print("mul from C")

class B(A,C):
    def sub(self):
        print("sub from B class")


obj = B()

obj.add()
obj.sub()