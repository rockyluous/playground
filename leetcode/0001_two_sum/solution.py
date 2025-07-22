def two_sum(nums, target):
    """Return indices of two numbers that add up to target.

    Uses a dictionary to map numbers to their indices.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    # If no solution is found, though problem guarantees one
    return []


if __name__ == "__main__":
    example = [2, 7, 11, 15]
    target_val = 9
    print(two_sum(example, target_val))
