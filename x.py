def fact(N):
        if N == 1:
                return 1
        res = N*fact(N-1)
        return(res)
print(fact(5))
