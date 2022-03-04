class A:
    def get1(self):
        print("Am Class A")


class B:
    def get2(self):
        print("Am Class B")


class C(A, B):
    def put(self):
        print("Am inherit both A & B")


obj = C()
obj.get1()
obj.get2()
obj.put()
