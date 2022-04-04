def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10
    print(id(bins[5]), id(bins[6]))
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            bins[e].append(A[j])
            print(bins)
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1


A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
radixsort(A)
print('Sorted Array:',A)
