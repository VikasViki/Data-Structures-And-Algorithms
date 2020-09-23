Question Link : https://leetcode.com/problems/majority-element-ii/

Approach :

Solution:

```Python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        total_nums = len(nums)
        
        if total_nums == 0:
            return []
        
        first_ele = second_ele = None
        first_ele_count = second_ele_count = 0
        
        for num in nums:
            if num == first_ele:
                first_ele_count += 1
            elif num == second_ele:
                second_ele_count += 1
            elif first_ele_count == 0:
                first_ele = num
                first_ele_count += 1
            elif second_ele_count == 0:
                second_ele = num
                second_ele_count += 1
            else:
                first_ele_count -= 1
                second_ele_count -= 1
                
        major_eles = []
        
        for ele in [first_ele, second_ele]:
            if nums.count(ele) > total_nums // 3:
                major_eles.append(ele)
        
        return major_eles
```
