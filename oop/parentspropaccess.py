class P:
    def __init__(self,age):
        print("p(age)")

    def add(self):
        print("add from P class")

class C(P): # C extends P
    def __init__(self):
        print("C()")
        P.__init__(self,12) # parent's parameterized constructor


c = C()
c.add()