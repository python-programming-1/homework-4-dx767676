# Part 1
def format_str(aList):
	length = len(aList)
	formatted = ''
	if length > 1:
		for i in range(length - 1):
			formatted += aList[i]+', '
		formatted += 'and '+aList[-1]+'.'
	else:
		formatted = aList[-1]+'.'
	return formatted

vegetables = ['carrot', 'lettuce', 'onion', 'radish']
print(format_str(vegetables))
print()

# Part 2
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

image = ''
for i in range(len(grid[0])):
	for j in range(len(grid)):
		image += grid[j][i]
	print(image)
	image = ''


