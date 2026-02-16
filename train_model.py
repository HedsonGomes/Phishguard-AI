import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# carregar dataset
df = pd.read_csv("dataset/sms_dataset.csv")

# limpeza de dados
df = df.dropna(subset=["label", "text"])
df = df[df["label"].str.strip() != ""]
df = df[df["text"].str.strip() != ""]

print("Distribuição das classes:")
print(df["label"].value_counts())

X = df["text"]
y = df["label"]

# split estratificado
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# vetorização melhorada
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    max_features=3000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# modelo balanceado
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_vec, y_train)

# avaliação
y_pred = model.predict(X_test_vec)

print("\nRelatório de Classificação:\n")
print(classification_report(y_test, y_pred))

# guardar modelo
joblib.dump(model, "app/model.pkl")
joblib.dump(vectorizer, "app/vectorizer.pkl")

print("\nModelo treinado com sucesso!")

