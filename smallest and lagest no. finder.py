def find_min_max_in_rotated_array(nums):
    lo = 0
    hi = len(nums) - 1
    
    # Function to find the index of the minimum element
    def find_min_index(nums, lo, hi):
        while lo <= hi:
            if nums[lo] <= nums[hi]:
                return lo

            mid = (lo + hi) // 2
            next_idx = (mid + 1) % len(nums)
            prev_idx = (mid - 1 + len(nums)) % len(nums)

            if nums[mid] <= nums[next_idx] and nums[mid] <= nums[prev_idx]:
                return mid
            elif nums[mid] <= nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
    
    min_index = find_min_index(nums, lo, hi)
    min_value = nums[min_index]
    max_index = (min_index - 1 + len(nums)) % len(nums)
    max_value = nums[max_index]
    
    return min_value, max_value

# Example usage:
rotated_array = [15, 18, 2, 3, 6, 12]
min_value, max_value = find_min_max_in_rotated_array(rotated_array)
print("Minimum value:", min_value)  # Output: 2
print("Maximum value:", max_value)  # Output: 18
