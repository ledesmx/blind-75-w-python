# Given an array of integers NUMS and and integer TARGET, return the indices I and
# J such that NUMS[I] + NUMS[J] == TARGET and I != J.
# You may assume that every input has exactly one pair of indices I and J that
# satisfy the condition.
# Return the answer with the smller index first.

def solution(nums, target):
    # Order nums
    nums.sort()
    # i = 0, j = len(nums) - 1
    i = 0
    j = len(nums) - 1

    while i < j:
        res = nums[i] + nums[j]
        # Check if nums[i] + nums[j] == target if so -> [i, j]
        if res == target:
            return [i, j]
        # if nums[i] + nums[j] < target, i++ and repeat
        # else j-- and repeat
        if res < target:
            i = i + 1
        else:
            j = j - 1

input1 = [3, 4, 5, 6]
target1 = 7
output1 = [0, 1]
solution1 = solution(input1, target1)
print(f'n={input1}, t={target1}, out={output1}, sol={solution1}, ok?={output1 == solution1}')

input2 = [4, 5, 6]
target2 = 10
output2 = [0, 2]
solution2 = solution(input2, target2)
print(f'n={input2}, t={target2}, out={output2}, sol={solution2}, ok?={output2 == solution2}')

input3 = [5, 5]
target3 = 10
output3 = [0, 1]
solution3 = solution(input3, target3)
print(f'n={input3}, t={target3}, out={output3}, sol={solution3}, ok?={output3 == solution3}')

input4 = [3, 4, 5, 5, 8]
target4 = 10
output4 = [2, 3]
solution4 = solution(input4, target4)
print(f'n={input4}, t={target4}, out={output4}, sol={solution4}, ok?={output4 == solution4}')

input5 = [3, 4, 8, 9, 9, 13, 20]
target5 = 18
output5 = [3, 4]
solution5 = solution(input5, target5)
print(f'n={input5}, t={target5}, out={output5}, sol={solution5}, ok?={output5 == solution5}')
