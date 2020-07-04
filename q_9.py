# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(start, end, num, list1):
    if end >= start:
        mid = (start+end)//2
        if num == list1[mid]:
            return mid
        elif list1[mid] > num:
            return binary_search(start, mid-1, num, list1)
        else:
            return binary_search(mid+1, end, num, list1)
    else:
        return -1

list1 = [1,3,2,6,7,3]
num = 2
print(sorted(list1))
result = binary_search(0, len(list1)-1, num, list1)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")


