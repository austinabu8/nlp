# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase and split it into words
words = sentence.lower().split()

# Create a dictionary to store word frequencies
word_count = {}

# Count the occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Display the word frequencies
print("\nWord Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
