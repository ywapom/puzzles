#print dups from list

l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7]

dups = {}

for i in l:
    if i in dups:
        dups[i] = dups[i] + 1
    else:
        dups[i] = 1

for key, value in dups.items():   
    if value >= 2:
        #print("key:",key, "value:",value)
        num_of_pairs = value // 2
        print("There are/is ",num_of_pairs, "pair of", key)



