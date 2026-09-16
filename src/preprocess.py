"""
Data Preprocessing Pipeline for Prompt Injection & Jailbreak Detection
Handles data cleaning, normalization, and stratified 80/20 train/test splitting.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split

SEED = 42

def clean_text(text):
    """
    Normalizes whitespace and formats text gently while preserving
    critical punctuation and structural tokens useful for attack detection.
    """
    if not isinstance(text, str):
        return ""
    # Strip leading/trailing whitespace and normalize multi-spaces/newlines
    text = " ".join(text.strip().split())
    return text

def preprocess_data(raw_data_path="data/raw/prompts.csv", output_dir="data/processed"):
    """
    Loads raw prompt dataset, applies cleaning, deduplication,
    and performs a stratified 80/20 train-test split.
    """
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"Raw dataset not found at {raw_data_path}. Run generate_dataset.py first.")

    df = pd.read_csv(raw_data_path)
    print(f"[*] Loaded raw data with {len(df)} samples.")

    # 1. Missing value handling
    df = df.dropna(subset=["text", "label"]).reset_index(drop=True)

    # 2. Text normalization
    df["clean_text"] = df["text"].apply(clean_text)

    # 3. Deduplication based on cleaned text
    initial_len = len(df)
    df = df.drop_duplicates(subset=["clean_text"]).reset_index(drop=True)
    print(f"[*] Removed {initial_len - len(df)} duplicate records. Current total: {len(df)}")

    # 4. Stratified 80/20 Train/Test split
    train_df, test_df = train_test_split(
        df,
        test_size=0.20,
        random_state=SEED,
        stratify=df["label"]
    )

    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, "dataset.csv")
    train_path = os.path.join(output_dir, "train.csv")
    test_path = os.path.join(output_dir, "test.csv")

    df.to_csv(full_path, index=False)
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"[+] Full processed dataset saved to: {full_path} ({len(df)} samples)")
    print(f"[+] Training set (80%) saved to:    {train_path} ({len(train_df)} samples)")
    print(f"[+] Test set (20%) saved to:        {test_path} ({len(test_df)} samples)")
    print("\n[*] Stratified Class distribution in Test Set:")
    print(test_df["label"].value_counts(normalize=True).round(3))

    return train_df, test_df

if __name__ == "__main__":
    preprocess_data()
