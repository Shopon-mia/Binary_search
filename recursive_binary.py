def recursive_binary(A,key,low,high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return recursive_binary(A, key, low, mid-1)
        else:
            return recursive_binary(A, key, mid+1, high)

    


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
key = int(input("Enter search number : "))
found = recursive_binary(A,key,0,9)
print("Search number found at : ",found," index")



    