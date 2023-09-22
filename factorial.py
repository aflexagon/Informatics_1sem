a = int(input())
def fact(N, depth=0):
        if N == 1:
            return 1
        res = N*fact(N-1,depth+1)
        return res
print(fact(a))
