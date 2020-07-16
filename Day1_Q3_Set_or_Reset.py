
def isSet(num):
    n = int(num)
    arr = []
    k = 0
    while n >= 1:
        if len(arr) < k:
            arr.append(0)
        if pow(2, k) >= n:
            if pow(2, k) > n:
                k -= 1
            else:
                arr.append(0)
            x = pow(2, k)
            n -= x
            arr[k] = 1
            k = 0
        k += 1
    print("The index value must be less tha or equal to", len(arr))
    index = int(input("Enter the position :"))
    print("Binary of given no. is:", arr[::-1])
    if index > len(arr):
        print("I warned you Position is out of Bounds")
    else:
        if arr[index-1] == 1:
            print("Binary value at", index, "is set or 1")
        else:
            print("Binary value at", index, "is reset or 0")


num = int(input("Enter a no.: "))
isSet(num)
