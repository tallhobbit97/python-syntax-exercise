def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    sev_is_present = False

    for num in nums:
        if num == 7:
            sev_is_present = True
            break
    
    return sev_is_present

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))