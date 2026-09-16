"""
Model Training Pipeline for Prompt Injection & Jailbreak Detection
Trains TF-IDF + Logistic Regression, Linear SVM (Calibrated), and Random Forest.
"""

import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier

SEED = 42

def train_models(train_path="data/processed/train.csv", model_dir="models"):
    """
    Trains text classification models using TF-IDF feature representations
    and serializes vectorizers and trained models to disk.
    """
    if not os.path.exists(train_path):
        raise FileNotFoundError(f"Training data not found at {train_path}. Run preprocess.py first.")

    train_df = pd.read_csv(train_path)
    X_train = train_df["clean_text"]
    y_train = train_df["label"]
    y_train_attack_type = train_df["attack_type"]

    os.makedirs(model_dir, exist_ok=True)

    print(f"[*] Training on {len(train_df)} samples...")

    # 1. TF-IDF Feature Extraction (Word Unigrams + Bigrams)
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True,
        lowercase=True
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    print(f"[+] TF-IDF vocabulary built with {X_train_tfidf.shape[1]} features.")

    # 2. Model 1: Logistic Regression
    print("[*] Training Model 1: Logistic Regression...")
    lr_model = LogisticRegression(C=2.0, max_iter=1000, random_state=SEED)
    lr_model.fit(X_train_tfidf, y_train)

    # 3. Model 2: Linear SVM (Calibrated for probability/confidence score output)
    print("[*] Training Model 2: Calibrated Linear SVM...")
    base_svm = LinearSVC(C=1.0, random_state=SEED)
    svm_model = CalibratedClassifierCV(estimator=base_svm, cv=5)
    svm_model.fit(X_train_tfidf, y_train)

    # 4. Model 3: Random Forest
    print("[*] Training Model 3: Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=150, max_depth=25, random_state=SEED, n_jobs=-1)
    rf_model.fit(X_train_tfidf, y_train)

    # 5. Granular Attack Type Classifier
    print("[*] Training Granular Attack Type Classifier...")
    attack_type_model = LogisticRegression(C=2.0, max_iter=1000, random_state=SEED)
    attack_type_model.fit(X_train_tfidf, y_train_attack_type)

    # 6. Save all artifacts using joblib
    joblib.dump(vectorizer, os.path.join(model_dir, "vectorizer.pkl"))
    joblib.dump(lr_model, os.path.join(model_dir, "logistic_regression.pkl"))
    joblib.dump(svm_model, os.path.join(model_dir, "svm.pkl"))
    joblib.dump(rf_model, os.path.join(model_dir, "random_forest.pkl"))
    joblib.dump(attack_type_model, os.path.join(model_dir, "attack_type_model.pkl"))

    print(f"[+] Successfully trained and saved all models to '{model_dir}/'")

if __name__ == "__main__":
    train_models()
