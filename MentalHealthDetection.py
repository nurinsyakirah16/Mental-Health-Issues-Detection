from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from datasets import dataset_used
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


x = dataset_used['processed_text']
y = dataset_used['mental_health_label']

# Encode target variable into numerical labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Splitting into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

# Feature vectorization TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize the models
nb_model = MultinomialNB()
dt_model = DecisionTreeClassifier()
lr_model = LogisticRegression()
rf_model = RandomForestClassifier()
xgb_model = XGBClassifier()
knn_model = KNeighborsClassifier()

# Train each model
models = [nb_model, dt_model, lr_model, rf_model, xgb_model, knn_model]

for model in models:
    model.fit(X_train_vectorized, y_train)

# Evaluate each model
for i, model in enumerate(models):
    y_pred = model.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

# Evaluate each model and store metrics
model_metrics = []

for model in models:
    y_pred = model.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    model_metrics.append({
        'Model': type(model).__name__,
        'Accuracy': accuracy,
        'Classification Report': report
    })

# Find the best performing model based on accuracy
best_model_metrics = max(model_metrics, key=lambda x: x['Accuracy'])

# Load the best model for further use
best_model = models[model_metrics.index(best_model_metrics)]
print(best_model)


