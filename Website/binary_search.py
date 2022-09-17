import math

items = [2, 4, 5, 1, 21345, 23]

def binary(items, find):
	output = ""
	items.sort()
	while True:
		if len(items) == 0:
			break
		n = math.ceil((len(items)+1)/2)
		if find > items[n]:
			output += f"Pivot is position {n} and item at pivot is {items[n]}.\n{find} > {items[n]} so discard bottom half of set.\n"
			items = items[n:]
		elif find < items[n]:
			output += f"Pivot is position {n} and item at pivot is {items[n]}.\n{find} < {items[n]} so discard bottom half of set.\n" 
			items = items[:n]
		else:
			output += f"Pivot is position {n} and item at pivot is {items[n]}.\n{find} = {items[n]} so item found at this position.\n" 
			break
	print(output)

binary(items, 5)