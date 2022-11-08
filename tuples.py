#Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
# Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = sorted(a, key = lambda x: x[1])
print (sorted_list)