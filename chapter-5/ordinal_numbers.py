nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        num = "1st"
    elif num == 2:
        num = "2nd"
    elif num == 3:
        num = "3rd"
    else:
        num = str(num) + "th"
    print(num)