# Given two strings S and T, return true if the two strings are anagrams
# of each other, otherwise return false.

# An anagram is a string that contains the exact same characters ad another
# string, but the order of the characters can be different

def solution(words):
   s = set(words[0])
   t = set(words[1])
   diff = s.symmetric_difference(t)
   return False if diff else True

input1 = ['racecar', 'carrace']
input2 = ['jar', 'jam']
input3 = ['evil', 'vile']
input4 = ['night', 'thing']
input5 = ['thing', 'think']
print(input1, solution(input1))
print(input2, solution(input2))
print(input3, solution(input3))
print(input4, solution(input4))
print(input5, solution(input5))
