N = int(input())#посл-ть Фиббоначи начинается с 0, считаю с 0
N = N - 1
def f(N,depth = 0):
        if N == 0:
                return(1)
        elif N ==1:
                return(1)
        res = f(N-2,depth+1)+f(N-1,depth+1)
        print(f'on step {depth} fact = {res}')
        return(res)
print(f(N))
