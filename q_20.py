# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.

class Sum:
    def __init__(self,array_list):
        self.array_list = array_list
    
    def calculation(self):
        nums, result, i=sorted(self.array_list), [],0
        while i < len(nums) - 2:
            j,k = i+1, len(nums) - 1
            while j<k:
                if nums[i] + nums[j] +nums[k] <0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return result

obj1 = Sum([10, -25, -3, 2, 4, -10, 8, -7])
print(obj1.calculation()) 