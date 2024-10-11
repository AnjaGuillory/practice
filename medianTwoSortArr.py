"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


class Solution:
    
    def checkBaseCases(self, nums1:List[int], nums2: List[int]) -> float:
        # [1][1]
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0]+nums2[0])/2
        # [1,2,3][]
        if len(nums1) > 0 and len(nums2) < 1 and len(nums1) % 2 == 1:
            return float(nums1[len(nums1)//2])
        # [][1,2,3]
        if len(nums1) < 1 and len(nums2) > 0 and len(nums2) % 2 == 1:
            return float(nums2[len(nums2)//2])
        # [1,2,3,4] []
        if len(nums1) > 0 and len(nums2) < 1 and len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
        # [][1,2,3,4]
        if len(nums1) < 1 and len(nums2) > 0 and len(nums2) % 2 == 0:
            return (nums2[len(nums2)//2]+nums2[(len(nums2)//2)-1])/2
        # [1][1,2]
        if len(nums2) < 2:
            if len(nums1) % 2 == 0:
                # [1,3][2]
                if nums1[(len(nums1)//2)-1] < nums2[0] and nums2[0] < nums1[len(nums1)//2]:
                    return nums2[0]
                # [2,3][1]
                elif nums1[(len(nums1)//2)-1] > nums2[0] and nums2[0] < nums1[len(nums1)//2]:
                    nums2.pop(0)
                    nums1.pop()
                # [1,2][3]
                else:
                    nums2.pop(0)
                    nums1.pop(0)
                return self.checkBaseCases(nums1, nums2)
            else:
                return self.checkBaseCases(nums1,[])
        # [1][1,2,3]
        
        # [1,2][1]
        if len(nums1) < 2:
            if len(nums2) % 2 == 0:
                # [2][1,3]
                if nums2[(len(nums2)//2)-1] < nums1[0] and nums1[0] < nums2[len(nums2)//2]:
                    return nums1[0]
                # [1][2,3]
                elif nums2[(len(nums2)//2)-1] > nums1[0] and nums1[0] < nums2[len(nums2)//2]:
                    nums1.pop(0)
                    nums2.pop()
                # [3][1,2]
                else:
                    nums1.pop(0)
                    nums2.pop(0)
                return self.checkBaseCases(nums1, nums2)
            else:
                return self.checkBaseCases([],nums2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if (check := self.checkBaseCases(nums1, nums2)) is not None: 
            return check
            
        num1_median = (
            nums1[len(nums1)//2]
            if len(nums1) % 2 == 1
            else (nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1])/2
        )
        
        num2_median = (
            nums2[len(nums2)//2]
            if len(nums2) % 2 == 1
            else (nums2[len(nums2)//2] + nums2[(len(nums2)//2)-1])/2
        )
            

        if num1_median == num2_median:
            return num1_median

        elif num1_median > num2_median:
            if len(nums1) % 2 == 0:
                if nums1[(len(nums1)//2)-1] < num2_median and num2_median < nums1[len(nums1)//2]:
                    return num2_median
            minimum_off = min(len(nums1)//2, len(nums2)//2)
            return self.findMedianSortedArrays(nums1[:len(nums1)-minimum_off], nums2[minimum_off:])
        
        elif num1_median < num2_median:
            if len(nums2) % 2 == 0:
                if nums2[(len(nums2)//2)-1] < num1_median and num1_median < nums2[len(nums2)//2]:
                    return num1_median
            minimum_off = min(len(nums1)//2, len(nums2)//2)
            return self.findMedianSortedArrays(nums1[minimum_off:], nums2[:len(nums2)-minimum_off])
        else:
            raise Exception("Some shit happened bro")
        
            
            
        
        
        
        
        
        # sorted = []
        # while len(nums1) > 0 and len(nums2) > 0:
        #     if nums1[0] > nums2[0]:
        #         sorted.append(nums2.pop(0))
        #     elif nums2[0] > nums1[0]:
        #         sorted.append(nums1.pop(0))
        #     else:
        #         sorted.append(nums1.pop(0))
        #         sorted.append(nums2.pop(0))
        
        # while len(nums1) > 0:
        #     sorted.append(nums1.pop(0))

        # while len(nums2) > 0:
        #     sorted.append(nums2.pop(0))
        # print(sorted)
        # if len(sorted) % 2 != 0:
        #     return sorted[(len(sorted)//2)]
        # return (sorted[len(sorted)//2] + sorted[(len(sorted)//2)-1])/2
        
    
obj = Solution()

# print(obj.findMedianSortedArrays([3], [-2,-1]))
# print(obj.findMedianSortedArrays([7,9], [5,8,11]))
# print(obj.findMedianSortedArrays([1,3,6,7], [2,3,8,10]))
# print(obj.findMedianSortedArrays([1,2,3], [4,5,6,7]))
print(obj.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17]))
# print(obj.findMedianSortedArrays([1,6,7,8,10], [2,3,4,5,9,11,12,13,14,15,16,17]))

            