# Given an int array length 2, return True if it contains a 2 or a 3.


def has23(nums):
    # return (2 in nums) or (3 in nums)
    if 2 in nums:
        return True
    elif 3 in nums:
        return True
    else:
        return False


print(has23([2, 5]))  # → True
print(has23([4, 3]))  # → True
print(has23([4, 5]))  # → False

