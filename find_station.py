# given a circular list of gas stations
# where we can go from i to i+1...
# find the index of the station that we can traverse home from (without running out of gas)

# we can only move forward
# tank starts empty
# gas[i] is the amount of gas at station i
# cost[i] is the cost in gas to reach the next station
# answer will be unique
# return -1 if not possible
from collections import deque



tests = {
    'input':{
        'gas':[1,5,3,3,5,3,1,3,4,5],
        'cost':[5,2,2,8,2,4,2,5,1,2]
    },
    'output': 8
}

def find_starting_station(gas, cost, home):
    '''
    return the index of gas that allows circle or -1
    BRUTE FORCE
    '''
    #O(n-squared)
    #S(n) = O(1)
    n = len(gas)
    fuel = 0
    i = home
    started = False
    while i != home or not started:
        started = True
        fuel += gas[i] - cost[i]
        if fuel < 0:
            return False
        i = (i+1)%n
    return True

def find_station(gas, cost):
    #O(n)
    #S(n) =O(n)
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            remaining = 0
    prev_remaining = sum(gas[:candidate])-sum(cost[:candidate])
    if candidate == len(gas) or remaining+prev_remaining < 0:
        return -1
    else:
        return candidate


def gas_station(gas, cost):
    for i in range(len(gas)):
        if find_starting_station(gas, cost, i):
            return i
    return -1

print(find_station(tests['input']['gas'], tests['input']['cost']))
