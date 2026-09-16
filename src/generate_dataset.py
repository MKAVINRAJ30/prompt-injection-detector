"""
Dataset Generator for Prompt Injection & Jailbreak Attack Detection
Compiles ~3,000+ labeled research samples across Benign, Injection, and Jailbreak categories.
"""

import os
import sys
import random
import pandas as pd

# Ensure module import resolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_benign import get_benign_samples
from data_injection import get_injection_samples
from data_jailbreak import get_jailbreak_samples

SEED = 42
random.seed(SEED)

def generate_dataset():
    print("[*] Generating comprehensive multi-class research dataset...")
    
    benign_data = get_benign_samples()
    injection_data = get_injection_samples()
    jailbreak_data = get_jailbreak_samples()

    print(f"[*] Compiled {len(benign_data)} Benign samples")
    print(f"[*] Compiled {len(injection_data)} Prompt Injection samples")
    print(f"[*] Compiled {len(jailbreak_data)} Jailbreak & Cyber Harm samples")

    all_data = benign_data + injection_data + jailbreak_data
    df = pd.DataFrame(all_data)

    # Deduplicate and shuffle
    initial_len = len(df)
    df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)
    df = df.sample(frac=1.0, random_state=SEED).reset_index(drop=True)

    os.makedirs("data/raw", exist_ok=True)
    raw_path = "data/raw/prompts.csv"
    df.to_csv(raw_path, index=False)

    print(f"\n[+] Total Unique Samples: {len(df)} (Deduplicated from {initial_len})")
    print("\n[+] Main Category Distribution:")
    print(df["label"].value_counts())
    print("\n[+] Granular Attack Type Distribution:")
    print(df["attack_type"].value_counts())
    print(f"\n[+] Saved complete dataset to: {raw_path}")
    return df

if __name__ == "__main__":
    generate_dataset()
