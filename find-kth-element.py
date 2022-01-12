# given arr of ints, and int k, find the kth largest element

tests = {
    'input':{
        'arr':[1,2,4,7,9,9,0,67,3],
        'k': 4
    },
    'output': 7
}


def find_k_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

result = find_k_largest(tests['input']['arr'], tests['input']['k'])
print(f"result {result}, expected {tests['output']}")
