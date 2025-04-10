# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false

def solution(nums):
    s = set(nums)
    return len(nums) != len(s)

input1 = [1, 2, 3, 4, 1]
input2 = [1, 2, 3, 4, 5]
input3 = [-6, 2, -8, 9, -5, 9]
input4 = [0, 0, 0, 0, 0]
input5 = [1]
print(input1, solution(input1))
print(input2, solution(input2))
print(input3, solution(input3))
print(input4, solution(input4))
print(input5, solution(input5))

