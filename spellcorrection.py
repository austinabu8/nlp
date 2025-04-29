import nltk
from nltk.corpus import words
from nltk.metrics.distance import edit_distance 
nltk.download('words') 
class SpellCorrector:
    def __init__(self):
        self.word_set = set(words.words()) 
    def correct_spelling(self, input_word):
        if input_word.lower() in self.word_set:
            return input_word  # The word is correctly spelled 
        suggestions = self.get_suggestions(input_word)
        if suggestions:
            return min(suggestions, key=lambda x: edit_distance(input_word, x)) 
        return input_word  # No suggestions found, return the original word 
    def get_suggestions(self, input_word):
        # Generate suggestions based on edit distance
        return [word for word in self.word_set if edit_distance(input_word, word) <= 2] 
if __name__ == "__main__":
    spell_corrector = SpellCorrector() 
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break 
        corrected_word = spell_corrector.correct_spelling(user_input)
        print(f"Corrected word: {corrected_word}")
