def search_rotated_sorted_array(nums, target):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        if mid_number == target:
            return mid
        
        # Determine which part is sorted
        if nums[lo] <= mid_number:  # Left part is sorted
            if nums[lo] <= target < mid_number:
                hi = mid - 1  # Target is in the left part
            else:
                lo = mid + 1  # Target is in the right part
        else:  # Right part is sorted
            if mid_number < target <= nums[hi]:
                lo = mid + 1  # Target is in the right part
            else:
                hi = mid - 1  # Target is in the left part
    
    return -1  # Target not found

# Example usage:
rotated_array = [15, 18, 2, 3, 6, 12]
target = 3
print(search_rotated_sorted_array(rotated_array, target))  # Output: 3

target = 18
print(search_rotated_sorted_array(rotated_array, target))  # Output: 1

target = 7
print(search_rotated_sorted_array(rotated_array, target))  # Output: -1 (not found)
