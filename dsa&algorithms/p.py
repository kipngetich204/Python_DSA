arr=[38,27,43,3,9,82,10,12,2,43,3454,56,576,76,7,68,78,7,86,78,657,56,876,8,768,67,6,556,68,876,8,7,876,876,8678,79,87,976,876,97,9789,76,6]
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1






def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2

    left =merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left,right)


def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j< len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while i <  len(left):
        result.append(left[i])
        i+=1

    while j < len(right):
        result.append(right[j])
        j+=1

    return result
print(merge_sort(arr))

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(arr))