nums = [1, 2, 3, 4, 5, 6, 4]
target = 7
step = 0
t = len(nums)
ans = []
for first_num in sorted(nums):
	for second_num in sorted(nums)[(len(nums) - t):]:
		if first_num + second_num == target:
			ans.append((first_num, second_num))
	t -= 1
ans = list(set(ans))
for x in ans:
	print(x)


		

