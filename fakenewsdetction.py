import pandas as pd
#import pip install scikit-learn 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Sample data for illustration
data = {
    'text': [
        'Real news example',
        'Fake news example',
        'Another real news',
        'Yet another fake news',
        'This is a real article',
        'Totally fake claim here',
        'Genuine reporting from agency',
        'Fake news story with lies'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = real, 0 = fake
}
df = pd.DataFrame(data)

# Split the data
train_data, test_data, train_labels, test_labels = train_test_split(
    df['text'], df['label'], test_size=0.25, random_state=42
)

# Vectorize text
vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(train_data)
test_features = vectorizer.transform(test_data)

# Train model
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(train_features, train_labels)

# Predict
predictions = classifier.predict(test_features)

# Evaluation
accuracy = accuracy_score(test_labels, predictions)
report = classification_report(test_labels, predictions, zero_division=0)
conf_matrix = confusion_matrix(test_labels, predictions)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)
print("Confusion Matrix:\n", conf_matrix)
