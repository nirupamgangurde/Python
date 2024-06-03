def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate `i`

        left, right = i + 1, len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicate `left`

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicate `right`

                left += 1
                right -= 1

            elif s < 0:
                left += 1

            else:
                right -= 1

    return result


# Test the function
print(threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(threeSum([]))  # Output: []
print(threeSum([0]))  # Output: []
