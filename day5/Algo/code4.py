nums = [5, 7, 9, 11, 15]

a = nums[0]
n = len(nums)
l = nums[-1]

i = 0
j = len(nums) -1

d = abs(a - l)/n


while i <= j:
    mid = (i+j)//2
    an = a +(mid) *d


    if j-1 == i:
        ans = (nums[i]+nums[j])/2
        break

    if nums[mid] == an:
        i = mid
    else:
        j = mid
    

print("missing number is:", int(ans))