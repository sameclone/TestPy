def sum(arr):
    total=0
    for x in arr:
        total+=x
    return total


def sum_recursive(array):
    if array==[]:
        return 0
    return array[0]+sum_recursive(array[1:])


def counter(array):
    if array==[]:
        return 0
    return 1+counter(array[1:])

def maxx(array):
    if len(array)==2:
        if array[0] > array[1]:
            return array[0]
        else:
            return array[1]
    else:
        sub_max = maxx(array[1:])
        if sub_max > array[0]:
            return sub_max
        return array[0]

print(sum([1,2,3,4]))
print(sum_recursive([1,2,3,4]))
print(counter([1,2,3,4]))
print(maxx([1,2,3,4]))