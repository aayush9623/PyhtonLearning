nums = [9,3,7,8,5,4,2]


def sort(nums):
    for i in range(6):
        minpos = i
        for j in range(i,7):
            if nums[j] < nums[minpos]:
                minpos=j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


sort(nums)

print(nums)
