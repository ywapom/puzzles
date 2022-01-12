# given arr of ints, and int k, find the kth largest element
import copy
import heapq

tests = {
    'input':{
        'arr':[1,2,4,7,9,9,0,67,3],
        'k': 4
    },
    'output': 7
}


def find_k_largest(arr, k):
    #O(kn) is slow
    myarr = copy.deepcopy(arr)
    for i in range(k-1):
        myarr.remove(max(myarr))
    return max(myarr)

def find_k_largest2(arr, k):
    #O(nlogn)
    myarr = copy.deepcopy(arr)
    n =  len(myarr)
    myarr.sort()
    return myarr[n-k]

def find_kth_heap(arr, k):
    #O(n+klongn)
    #reverse as heapq is by small
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)



result = find_k_largest(tests['input']['arr'], tests['input']['k'])
print(f"result {result}, expected {tests['output']}")

result = find_k_largest2(tests['input']['arr'], tests['input']['k'])
print(f"result {result}, expected {tests['output']}")

result = find_kth_heap(tests['input']['arr'], tests['input']['k'])
print(f"result {result}, expected {tests['output']}")
