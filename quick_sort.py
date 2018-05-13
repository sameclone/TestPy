def quicksort1(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        greater=[]
        less=[]
        for i in array[1:]:
            if i <=pivot:
                less.append(i)
            else:
                greater.append(i)
        return quicksort1(less)+[pivot]+quicksort1(greater)




print( quicksort1([10, 5, 2, 3]))