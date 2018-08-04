n = int(input())
nums = list(map(int, input().split()))
nums.sort()
d = [abs(nums[i]-nums[i-1]) for i in range(1,len(nums))]
print(min(d))