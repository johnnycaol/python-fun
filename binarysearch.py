def binarySearch(items, left, right, target):
    if right >= left:
        # Find the mid point of the left and right
        mid = left + (right-left)/2
        
        if items[mid] == target:# If equals to the target, return the index
            return mid
        elif items[mid] > target:
            return binarySearch(items, left, mid-1, target)
        else:
            return binarySearch(items, mid+1, right, target)
    else:
        # target does not exist in items
        return False
    

items = ['111', '222', '333']
print(binarySearch(items, 0, len(items)-1, '222'))