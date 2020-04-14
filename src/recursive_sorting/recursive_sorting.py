# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    i = 0
    j = 0

    for num in range (0, elements):
        if i >= len(arrA):
            merged_arr.append(arrB[j])
        elif j >= len(arrB):
            merged_arr.append(arrA[i])
            i += 1
        elif arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        elif arrA[i] > arrB[j]:
            merged_arr.append(arrB[j])
            j += 1

    return merged_arr

# print(merge([2, 4, 9], [8, 3, 7]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
    
        middle = int(len(arr) / 2)
        arrA = merge_sort(arr[:middle])
        arrB = merge_sort(arr[middle:]) 

        arr = merge(arrA, arrB)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
