def linearSearch(A, key):
    position = 0
    flag = False

    while position < len(A) and not flag:
        print("Searching")
        if A[position] == key:
            print(A[position])
            flag = True
        else:
            position += 1
    return flag

print(linearSearch([7, 9 ,15, 9], 9))
