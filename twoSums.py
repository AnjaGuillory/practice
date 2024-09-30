"""
Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

Constraints:
    Each input will have exactly one solution.
    You may not use the same element twice.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums: List[int], target: int) -> List[int]:
    pass

Hints:
    Can you do it in one pass with a hash map?
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    num_map =  {}

    for ind in range(len(nums)):
        if target - nums[ind] in num_map:
            return [ind, num_map[target - nums[ind]]]
        else:
            num_map[nums[ind]] = ind
    return []

print(two_sum([15, 2, 11, 7, 5, -5, 8, 15], 10))