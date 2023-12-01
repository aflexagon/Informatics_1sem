
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[len(A)-1]
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

n = list(input().split())
print(*QuickSort(n))