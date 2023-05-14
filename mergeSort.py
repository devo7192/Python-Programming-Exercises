def mergeTwoLists(list1, list2): # Where list1 and list2 are sorted lists
    
    mergedList = []

    i, j = 0, 0
    while (i < len(list1)) and (j < len(list2)):
        if (list1[i] > list2[j]):
            mergedList.append(list2[j])
            j += 1
        elif (list1[i] < list2[j]):
            mergedList.append(list1[i])
            i += 1
        else:   # list1[i] == list2[j]
            mergedList.append(list1[i])
            mergedList.append(list2[j])
            i += 1
            j += 1

    if i < len(list1):
        return mergedList + list1[i:]
    
    if j < len(list2):
        return mergedList + list2[j:]

    return mergedList


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]