# Use a dictionary comprehension to count the length of each word in a sentence.
# Input: "The quick brown fox jumped over the fence." otuput: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}

sentence = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sentence.split()})