# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         ans:list[int] = []
#         indexed_nums = [(i, number) for i , number in enumerate(nums)]
#         sorted_nums = sorted(indexed_nums, key=lambda x:x[1])
#         for index, v in enumerate(sorted_nums):
#             flag:bool = False
#             indice, i = v
#             for j in range(index + 1, len(nums)):
#                 x,y = sorted_nums[j]
#                 if i + y > target:
#                     break
#                 elif i + y == target:
#                     flag = True
#                     ans = [indice, x]
#                     break
#                 else:
#                     pass
#             if flag:
#                 break
#         return ans

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i


a  = Solution

print(a.twoSum(a,[2,3,4,5,6,7,8,11],19))