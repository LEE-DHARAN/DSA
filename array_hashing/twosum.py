from typing import List


def twoSum(nums:List[int],target:int)->List[int]:
    n=len(nums)
    hash_map = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i] 
        hash_map[nums[i]] = i
    return []
result = twoSum([2,3,4,7],9)
print(result)