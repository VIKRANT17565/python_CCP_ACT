nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = int(input("target : "))

i = 0
j = len(nums)-1

first = -1
last = -1

while True:
    if first == -1 and nums[i] == target:
        first = i
    
    if last == -1 and nums[j] == target:
        last = j


    if i < len(nums):
        i += 1

    if j >= 0:
        j -= 1

    if i == (len(nums)-1) and j == 0:
        break
    

if first == -1 and last == -1:
    print("Target not in list")

else:
    print("The first occurence of element", target, "is located at index", first)
    print("The last  occurence of element", target, "is located at index", last)