
def genSubset(set_arr, init, current, subset):
    print(current)
    for i in range(init, len(set_arr)):
        current.append(set_arr[i])
        print(i)
        genSubset(set_arr, i + 1, current, subset)
        current.remove(current[-1])
    return


set_arr = input("Enter the no.").split()
curr = []
subset = []
arr = []
genSubset(set_arr, 0, curr, subset, )

A B C E
S F C S
A D E E
