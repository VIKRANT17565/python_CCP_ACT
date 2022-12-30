nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = int(input("target : "))

count = 0
for i in range(len(nums)):
    if nums[i] == target:
        count += 1

print("Target", target, "occurs", count, "times")
