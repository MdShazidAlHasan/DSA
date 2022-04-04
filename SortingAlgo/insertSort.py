def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1]> cvalue:
          A[position] = A[position-1]

          print(f'position: {position} cvalue: {cvalue} list: {A}')
          position = position -1
        A[position] = cvalue
        print(f'final -----> position: {position} cvalue: {cvalue} list: {A}')


a = [1, 2, 5, 4, 0, 3 ]
insertionSort(a)
print(a)
