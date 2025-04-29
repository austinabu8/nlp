import random
from collections import defaultdict

class NextWordPredictor:
    def __init__(self, n):
        self.n = n  # Context size (n words for predicting the next word)
        self.model = defaultdict(list)

    def train_model(self, text):
        words = text.split()
        for i in range(len(words) - self.n):
            context = tuple(words[i:i + self.n])
            next_word = words[i + self.n]
            self.model[context].append(next_word)

    def predict_next_word(self, context):
        if isinstance(context, str):
            context = tuple(context.split())
        possible_next_words = self.model.get(context, [])
        if possible_next_words:
            return random.choice(possible_next_words)
        else:
            return None

if __name__ == "__main__":
    # Example usage
    text_data = "This is a simple example of a next word prediction model. Implementing this model can be educational and fun."
    nwp_model = NextWordPredictor(n=2)  # Use a bigram model (context size = 2 words)
    
    # Train the model
    nwp_model.train_model(text_data)
    
    # Predict the next word given a context
    context = ("word", "prediction")  # tuple of 2 words
    predicted_word = nwp_model.predict_next_word(context)
    if predicted_word:
        print(f"Predicted next word: {predicted_word}")
    else:
        print("No prediction available.")
