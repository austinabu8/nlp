import nltk


from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required NLTK data (only needed once)


def get_pos_tags(text):
    words = word_tokenize(text)  # Tokenize text into words
    pos_tags = pos_tag(words)  # Get part of speech for each word
    return pos_tags

# Example usage:
text = input("Enter your text: ")
pos_result = get_pos_tags(text)

# Print result
for word, pos in pos_result:
    print(f"{word}: {pos}")
