def binarySearch(A, key, low , high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high = mid - 1
            return binarySearch(A, key, low, high)
        elif key > A[mid]:
            low = mid -1
            return binarySearch(A, key, low, high)
