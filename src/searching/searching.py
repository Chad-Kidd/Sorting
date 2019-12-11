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

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
