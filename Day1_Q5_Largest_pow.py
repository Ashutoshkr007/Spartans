def largestPower(num):
    n = int(num)
    k = 0
    while n >= 1:
        if pow(2, k) >= n:
            if pow(2, k) > n:
                k -= 1
            x = pow(2, k)
            break
        k += 1
    print(x)


num = int(input("Enter a no.: "))
largestPower(num)