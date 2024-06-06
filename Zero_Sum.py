def find_zero_sum_sublists(nums):
    result = []
    for i in range(len(nums)):
        sum_so_far = 0
        for j in range(i, len(nums)):
            sum_so_far += nums[j]
            if sum_so_far == 0:
                result.append(nums[i:j+1])
    return result

nums = [1, 2, -3, 4, -1, -2, 3, -4]
print(find_zero_sum_sublists(nums))
