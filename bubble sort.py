def bubble_sort(nums):
    nums=list(nums)
    for _ in range(len(nums)-1 ):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] :
                nums[i], nums[i+1]=nums[i+1], nums[i]
    return nums
nums=[20,10,-1]
print(bubble_sort(nums))
