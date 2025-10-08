# Fake News Detection Project: Full Script

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load and Explore Dataset
df = pd.read_csv('news.csv')  # Columns: text, label

print(df.head())
print(df.label.value_counts())
sns.countplot(x='label', data=df)
plt.title('Distribution of Real vs Fake News')
plt.show()

# 2. Data Cleaning (Basic example)
df.dropna(subset=['text', 'label'], inplace=True)
df['text'] = df['text'].str.lower()

# 3. Split Data
X = df['text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 4. Text Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = vectorizer.fit_transform(X_train)
tfidf_test = vectorizer.transform(X_test)

# 5. Model Building
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(tfidf_train, y_train)
print(model)

# 6. Model Prediction & Evaluation
y_pred = model.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {score*100:.2f}%")
print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))

# 7. Test with a new news headline
sample_text = "The President announced a new policy to boost renewable energy."
sample_tfidf = vectorizer.transform([sample_text])
sample_pred = model.predict(sample_tfidf)
print('Prediction for sample:', sample_pred[0])

# 8. Save Model (optional)
import joblib
joblib.dump(model, 'fake_news_model.pkl')
print(joblib)

# 9. Load and Use Model (optional)
# loaded_model = joblib.load('fake_news_model.pkl')
# prediction = loaded_model.predict(sample_tfidf)