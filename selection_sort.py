def findSmallest(arr):
    smalest=arr[0]
    smalest_index=0
    for i in range(1, len(arr)):
        if arr[i]<smalest:
            smalest=arr[i]
            smalest_index=i
    return smalest_index

def selectionSort(arr):
    newArr=[]
    for i in range( len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([ 5, 3, 6, 2, 10, 10, 11]))

