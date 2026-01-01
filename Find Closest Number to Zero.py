nums = [-4,-2,1,4,8]

solution = nums[0]

for i in nums:
    if abs(i) < abs(solution):
        solution = i

print(solution)