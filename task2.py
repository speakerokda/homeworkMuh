nums = [10, 3]
UnicNums = sorted(list(set(nums)), reverse = 1)
if len(UnicNums) > 1:
	print(UnicNums[1])
else:
	print('Второго по величине элемента нет')