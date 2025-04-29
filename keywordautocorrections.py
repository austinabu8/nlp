    import numpy as np 
    class KeyboardAutoCorrector:
    def __init__(self, dictionary):
        self.dictionary = set(word.lower() for word in dictionary) 
    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1) 
        previous_row = np.arange(len(s2) + 1) 
        for i, char1 in enumerate(s1):
            current_row = np.zeros(len(s2) + 1, dtype=int)
            current_row[0] = i + 1 
            for j, char2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (char1 != char2) 
                current_row[j + 1] = min(insertions, deletions, substitutions) 
            previous_row = current_row 
        return previous_row[-1] 
    def auto_correct(self, word):
        word_lower = word.lower() 
        if word_lower in self.dictionary:
            return word  # The word is already in the dictionary 
        corrected_word = self.find_closest_word(word_lower) 
        return corrected_word 
    def find_closest_word(self, word):
        min_distance = float('inf')
        closest_word = word 
        for dictionary_word in self.dictionary:
            distance = self.levenshtein_distance(word, dictionary_word)
            if distance < min_distance:
                min_distance = distance
                closest_word = dictionary_word 
        return closest_word 
if __name__ == "__main__":
    # Example usage with a small dictionary
    word_dictionary = ["python", "programming", "language", "spell", "correction"]
    auto_corrector = KeyboardAutoCorrector(word_dictionary) 
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break 
        corrected_word = auto_corrector.auto_correct(user_input)
        print(f"Corrected word: {corrected_word}")
