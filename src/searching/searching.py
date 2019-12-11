# STRETCH: implement Linear Search				
nums = [ 1, 5, 6, 7]

def linear_search(arr, target):
  # TO-DO: add missing code
  for nums in arr:
     if nums == target:
         return True
  return False # not found

print(linear_search(nums, 7)) # True
print(linear_search(nums, 2)) # False
print(linear_search(nums, 9)) # False

# Tested in IntelliJ WORKS
# time complexited = O(n)

# STRETCH: write an iterative implementation of Binary Search 
# start in middle then analyze either side 
# will not work on unsorted lists

##start at middle
##compare val == search_val
## < search low
## > search right
## keep track of cur search arr
# loop until item found 

def binary_search(arr, target):       
    low = 0                           
    high = len(arr)-1                 
                                      
    found = False                     
                                      
    while not found:                  
        middle = (low + high)         
                                      
        if arr[middle] == target:     
            found = True              
        else:                         
            if target < arr[middle]:  
        #search lower half            
              low = middle - 1        
            else:                     
        #search upper half            
              high = middle + 1       
                                      
        # TO-DO: add missing code     
    return found                      
                                      
print(binary_search(nums, 7)) # True 
## Tested in IntelliJ WORKING 
print(binary_search(nums, 2)) # False 
## Tested in IntelliJ NOT WORKING 
print(binary_search(nums, 9)) # False 
## Tested in IntelliJ NOT WORKING 


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
