arr = [1,1,2,2,2,3,3]
set_arr = set(arr)
print(set_arr)

#leetcode
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        k = 1  # The 1st element is always sorted in elements and unique thats y u didnt care abt index 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
