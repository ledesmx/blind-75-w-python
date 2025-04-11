# Given an array of strings STRS, group all anagrams together into sublists.
# You may return output in any order.
#
# An anagram is a string that contains the exact same characters as another string,
# but the order of the caracters can be different

def solution(words):
    # Store the basic anagram with the index of the list
    # basic anagram is the sorted word eg. cat -> atc, tac -> atc
    # index if the index of the list within is the list of anagrams
    anagrams = {}
    # Result, list with the lists of anagrams
    res = []
    for word in words:
        # Sort word
        anagram = ''.join(sorted(word))

        # If the anagram is in the map, then get index, and append the word in its lits
        # Otherwise create a new list within the list, and store in the map with its index
        if anagram in anagrams:
            index = anagrams.get(anagram)
            res[index].append(word)
        else:
            anagrams[anagram] = len(anagrams)
            res.append([word])

    return res

input1 = ['act', 'pots', 'tops', 'cat', 'stop', 'hat']
print(solution(input1))

input2 = ['x']
print(solution(input2))

input3 = ['']
print(solution(input3))
