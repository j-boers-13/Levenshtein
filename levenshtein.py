import sys

def Levenshtein(first,second):
	vowels = ['a','e','o','u','i']
	if len(first) > len(second):
		first, second = second, first
	if len(second) == 0:
		return len(first)
	first_length = len(first) + 1
	second_length = len(second) + 1
	distance_matrix = [[0] * second_length for x in range(first_length)]
	print(distance_matrix)
	print(first,first_length)
	for i in range(first_length):
	   distance_matrix[i][0] = i
	   print(distance_matrix[i][0])
	for j in range(second_length):
		distance_matrix[0][j]=j
	print(distance_matrix)
	for i in range(first_length):
		for j in range(second_length):
			print(distance_matrix)
			if second[j-1] in vowels:
				cost = 0.5
			else:
				cost = 1
			deletion = distance_matrix[i-1][j] + cost
			print('deletion',deletion)
			insertion = distance_matrix[i][j-1] + cost
			print('insertion',insertion)
			if first[i-1] in vowels and second[j-1] in vowels:
				cost = 0.5
			else:
				cost = 1
			substitution = distance_matrix[i-1][j-1]
			if first[i-1] != second[j-1]:
				substitution += cost
				print('substitution',substitution)
			distance_matrix[i][j] = min(insertion, deletion, substitution)
	print(distance_matrix)
	return distance_matrix[first_length-1][second_length-1]
	
	
def main():
	for line in sys.stdin:
		word1 = line.split()[0].lower()
		word2 = line.split()[1].lower()
		print(Levenshtein(word1,word2))
	
main()
