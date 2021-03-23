from random import random

def binarySearch(arr, left, right, value):
    med = int((left + right)/2)
    if left == right:
        return -1
    if arr[med] == value:
        return med
    if arr[med] < value:
        return binarySearch(arr, med+1, right, value)
    else:
        return binarySearch(arr, left, med-1, value)


lst = list()
for i in range(100):
    lst.append(int(random() * 100))
lst.sort()
print(binarySearch(lst, 0, 99, 23))
