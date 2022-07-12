nums = [1, 2, 3, 4, 1, 3]
def dup(nums):
    for i in range(0, len(nums)):
                for j in range(1, len(nums)):
                    if nums[i] == nums[j]:
                        return "True"
                        
    
    return "False"
                        
dup(nums) 