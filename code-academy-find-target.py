#given a sorted array of ints and a target int
#find the first and last index positions
#if not found return [-1,-1]

def find_target(arr, target):
    lower = 0
    upper = len(arr)-1
    found = False


    while(lower <= upper and not found):
        mid = (upper + lower) //2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    print(target, "found at", mid);

def step_find(arr, target):
    first = -1
    last = -1

    for idx, val in enumerate(arr):
        if((val == target) and (first == -1)):
            first = idx
            break

    for idx in range(len(arr) -1, -1, -1):
        if arr[idx] == target:
            last = idx
            break
    
    print(f'[{first},{last}]')
arr = [1, 2, 5, 7, 7, 7, 3, 10]
#find_target(arr, 7)

step_find(arr, 8)
