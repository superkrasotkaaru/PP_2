def spy_game(nums):
    # Initialize flags to track the presence of 0, 0, and 7 in order
    has_0 = False
    has_00 = False

    # Iterate through the list
    for num in nums:
        if num == 0 and not has_0:
            # Found the first 0
            has_0 = True
        elif num == 0 and has_0 and not has_00:
            # Found the second 0
            has_00 = True
        elif num == 7 and has_00:
            # Found the 7 after 0 and 0
            return True

    # If the sequence "007" is not found
    return False

# Test cases
print(spy_game([1,2,4,0,0,7,5]))    
print(spy_game([1,0,2,4,0,5,7]))    
print(spy_game([1,7,2,0,4,5,0])) 