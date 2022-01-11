#two words with the same frequency of letters
from collections import Counter
def are_anagrams(words):
    if(len(words[0]) != len(words[1])):
        return False;
    return Counter(words[0]) == Counter(words[1])


#without collections:
def IsAnagram(words):
    #if lengths aren't the same return false
    if(len(words[0]) != len(words[1])):
        return False;
    #keep two hashtables with counts of letters -  O(n)
    #or sort the strings and iterate - O(n-log-n)
    wordone = {}
    wordtwo = {}

    for char in words[0]:
        if char in wordone:
            wordone[char]+=1;
        else:
            wordone[char] = 1;

    for char in words[1]:
        if char in wordtwo:
            wordtwo[char]+=1;
        else:
            wordtwo[char] = 1;

    print(wordone, wordtwo)

    if wordtwo == wordone:
        return True;
    return False;

listofwords = [
    ["cat","tac"],
    ["sewer", "sweer"],
    ["brothel", "brothe"],
    ["nameless", "salesmen"],
    ["kick", "kicl"]
]
for lists in listofwords:
    result = IsAnagram(lists);
    print(result, lists);


for lists in listofwords:
    result = are_anagrams(lists);
    print(result, lists);
