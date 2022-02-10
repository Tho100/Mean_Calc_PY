class main:
    def __init__(self, n0,n1,n2,n3):
        self.n0 = n0
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    def find_mean(self):
        self.array = [self.n0,self.n1,self.n2,self.n3]
        mean = sum(self.array)/len(self.array)
        print(mean)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

call = main(a,b,c,d)
call.find_mean()
