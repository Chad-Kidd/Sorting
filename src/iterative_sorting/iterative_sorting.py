# TO-DO: Complete the selection_sort() function below 
#testing_sorting_list = [78, 1, 3, 0, 75, 86, 106, 78, 48, 7, 10, 97, 24]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    
    return arr          

print(selection_sort(sorting_list)) 
#[0, 1, 3, 7, 10, 24, 48, 75, 78, 78, 86, 97, 106]
###tested in intelliJ WORKS


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for x in range(0, len(arr) -1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
    return arr

print(bubble_sort(sorting_list))    
#[0, 1, 3, 7, 10, 24, 48, 75, 78, 78, 86, 97, 106]
###tested in intelliJ WORKS

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr