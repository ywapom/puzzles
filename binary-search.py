arr = [1, 2, 5, 7, 3, 10]

def search(arr, target):
    lower = 0
    upper = len(arr)-1
    found = False

    while (lower <= upper and not found):
        mid =  (upper + lower) // 2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                upper = mid-1
            else:
                lower = mid+1
    return found

print(search(arr, 10))
