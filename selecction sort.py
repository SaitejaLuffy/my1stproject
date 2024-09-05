def selsort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
           if nums[j]<nums[minpos]:
              minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

nums=[6,89,934,5,232,2]
selsort(nums)
print(nums)