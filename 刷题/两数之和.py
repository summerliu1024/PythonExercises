# # 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# #
# # 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# #
# # 示例:
# #
# # 给定 nums = [2, 7, 11, 15], target = 9
# #
# # 因为 nums[0] + nums[1] = 2 + 7 = 9
# # 所以返回 [0, 1]
#
# # class Solution:
# #     def twoSum(self, nums, target):
# #
# #         result = list()
# #
# #         for i in nums:
# #             for k in nums:
# #                 if i + k == target:
# #                     result.append(nums.index(i))
# #                     result.append(nums.index(k))
# #
# #         return (list(set(result)))
#
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap = {}
#         for index, num in enumerate(nums):
#             another_num = target - num
#             if another_num in hashmap:
#                 return [hashmap[another_num], index]
#             hashmap[num] = index
#         return None
#
#
# nums = [2, 7, 11, 15]
# import random
#
# target = 6
# sol = Solution()
# print(sol.twoSum(nums, target))

a="k:a|k1:b|k2:3|k3:4"
"""{“k”:1,”k1”:2,”k2”:3,”k3”:4}"""

print(a.split("|"))
my_dict=dict()
for var in a.split("|"):
    print(var)
    key=var.split(":")[0]
    value=var.split(":")[1]
    my_dict[key]=value


print(my_dict)
# import random
# my_list = ["a","a","a",1,2,3,4,5,"A","B","C"]
#
# random.shuffle(my_list)
#
# print(my_list)
# # str1 = ""
# # for i in my_list:
# #     try:
# #         if i.isalnum():
# #             pass
# #     except:
# #         str1 += str(i)
# # print(str1)





# my_dict[key]=value

a = [3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 7, 8, 8, 3]

my_list=list()
for index,nums in enumerate(a):
    # print(index,nums)

    if nums==3:
        my_list.append(index)


print(my_list)
