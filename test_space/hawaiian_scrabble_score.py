def hawaiian(text):
	lowercase = text.lower()
	points = {"a": 1, "k": 2, "o": 2, "i": 3, "n": 3, "e": 4, "u": 5, "h": 6, "l": 7, "m": 8, "p": 8, "w": 9}
	total = 0
	for char in lowercase:
		if char not in points:
			return -1
		else:
			total += points[char]
	return total
