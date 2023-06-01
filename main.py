def merge_vetores(a1, a2):
    merged = a1 + a2
    for i in range(len(merged)):
        min = i
        for j in range(i + 1, len(merged)):
            if merged[j] < merged[min]:
                min = j
        merged[i], merged[min] = merged[min], merged[i]
    return merged
	
a1 = [4, 8, 78, 2, 44, 6]
a2 = [1, 9, 3, 5, 4, 8, 9]
novo = merge_vetores(a1, a2)

for num in novo:
    print(num)