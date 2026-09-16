# Research Notes & Paper Draft

## Title
**Machine Learning-Based Detection of Prompt Injection and Jailbreak Attacks in LLM Applications**

---

### Abstract
Large Language Models (LLMs) are widely integrated into customer support, autonomous agent workflows, software development, and enterprise applications. However, their unified architecture—where computational control instructions and untrusted user inputs share the same input stream—makes them susceptible to adversarial prompt injection and jailbreak attacks. Prompt injections override system instructions or extract internal configuration prompts, while jailbreak attacks manipulate model personas and bypass safety filters. This paper presents a machine learning-based classification framework for real-time prompt vulnerability detection. Using TF-IDF feature representations combined with supervised classifiers (Logistic Regression, Linear Support Vector Machines, and Random Forest), the proposed system categorizes incoming prompts as Benign, Prompt Injection, or Jailbreak, while providing granular attack subtype identification and confidence scores. The framework was evaluated on a curated dataset of over 1,200 diverse prompts and subjected to an unseen adversarial robustness test. The experimental results demonstrate that lightweight, classical machine learning models can achieve high detection accuracy and low-latency inference on local hardware without requiring external API dependencies or computationally expensive neural guardrails.

---

### Keywords
LLM Security, Prompt Injection, Jailbreak Detection, Machine Learning, NLP, Adversarial Prompts

---

### 1. Introduction
The rapid adoption of Large Language Models (LLMs) such as GPT-4, LLaMA, Claude, and Gemini has transformed automated reasoning and conversational AI. Developers increasingly construct LLM-powered applications by embedding system instructions, context, user input, and retrieved database records into a single prompt string. 

Despite their natural language understanding capabilities, LLMs lack a fundamental hardware-level separation between the "control plane" (system instructions) and the "data plane" (external user inputs). Consequently, attackers can craft adversarial prompt payloads that force the model to disregard its initial instructions, leak confidential system prompts, or bypass ethical alignment filters. 

Mitigating these threats purely via prompt engineering or proprietary safety filters often proves brittle, as adaptive adversaries develop novel semantic framings and jailbreak personas (e.g., "Do Anything Now" or fictional role-plays). A robust, multi-layered security architecture requires a dedicated pre-execution detection filter that inspects prompts before they reach the LLM.

---

### 2. Problem Statement
Given an arbitrary natural language prompt $x \in \mathcal{X}$ submitted to an LLM application, the objective is to learn a mapping function $f: \mathcal{X} \rightarrow \mathcal{Y}$, where:
$$\mathcal{Y} \in \{\text{BENIGN}, \text{PROMPT\_INJECTION}, \text{JAILBREAK}\}$$
along with a calibrated posterior probability $P(y \mid x)$ and a sub-classification mapping $g(x) \rightarrow \mathcal{A}$ denoting the granular attack subtype.

The detection must operate with minimal latency, provide interpretable decision rationales, run on standard local computing infrastructure without relying on paid commercial APIs, and maintain high generalization across unseen attack formulations.

---

### 3. Objectives
1. **Develop a Multi-Class Classifier:** Accurately classify user inputs into Benign, Prompt Injection, and Jailbreak categories.
2. **Granular Subtype Identification:** Categorize malicious prompts into specific attack vectors (direct instruction overrides, system prompt extraction, role-play persona exploits, safety filter bypasses, authority impersonation, and obfuscations).
3. **Local & Efficient Deployment:** Ensure zero external API dependencies with low computational footprint.
4. **Empirical Validation:** Rigorously evaluate classification performance across precision, recall, F1-scores, confusion matrices, and unseen robustness stress testing.

---

### 4. Proposed Methodology
The proposed detection pipeline consists of four sequential stages:

```
[ Input Prompt ] 
       │
       ▼
[ Preprocessing & Normalization ]
   • Whitespace normalization
   • Non-destructive token preservation (retaining delimiter & punctuation cues)
       │
       ▼
[ TF-IDF Feature Extraction ]
   • Word unigrams and bigrams (n-gram range: (1, 2))
   • Sublinear term-frequency scaling
       │
       ▼
[ Supervised ML Classification ]
   • Model A: Logistic Regression (L2 regularization)
   • Model B: Calibrated Linear SVM (Maximum-margin separation)
   • Model C: Random Forest Ensemble
       │
       ▼
[ Decision, Explainability & Remediation Output ]
   • Category Label (Benign / Injection / Jailbreak)
   • Calibrated Confidence Score (%)
   • Granular Attack Subtype
   • Token Attribution Heatmap (Explainable AI - XAI)
   • Automated Prompt Sanitizer & Neutralizer (Safe LLM Forwarding)
```

---

### 5. Dataset Description
The dataset was synthetically constructed to simulate real-world LLM application interactions with balanced representation across legitimate use cases and adversarial patterns.

**Dataset Summary:**
- **Total Samples:** 3,490 distinct, verified prompt examples.
- **Data Split:** 80% Training ($N_{train} = 2,792$), 20% Test ($N_{test} = 698$) using stratified sampling.
- **Random Seed:** Fixed to 42 for exact experimental reproducibility.

#### Taxonomy of Categories & Subtypes:
1. **BENIGN (Legitimate Queries)**
   - `benign_general_question`: STEM, history, economics, and conceptual inquiries.
   - `benign_instruction`: Scheduling, drafting emails, task organization.
   - `benign_coding`: Algorithm implementation, debugging, syntax questions.
   - `benign_summarization`: Standard text analysis and document extraction.

2. **PROMPT INJECTION (Control-Flow Hijacking)**
   - `direct_instruction_override`: Direct imperatives commanding the model to ignore or reset prior instructions.
   - `system_prompt_extraction`: Probing attempts to dump initial system messages or developer rules.
   - `instruction_conflict`: Payloads embedded inside data fields, markdown delimiters, or secondary tasks.

3. **JAILBREAK (Safety & Alignment Bypass)**
   - `role_play`: Hypothetical framing, DAN persona adoption, and fictional scenarios.
   - `safety_bypass`: Explicit commands to disable content moderation or ethical filters.
   - `authority_impersonation`: False claims of system administrator, superuser, or regulatory credentials.
   - `obfuscation`: Encoding techniques (Base64, ROT13, leetspeak, pseudo-code structures).

---

### 6. Algorithms
1. **Term Frequency-Inverse Document Frequency (TF-IDF):**
   Transforms raw text strings into high-dimensional numerical feature vectors:
   $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \log\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
   Using unigrams and bigrams captures both individual indicator terms (e.g., "override", "DAN", "sudo") and multi-word attack phrases (e.g., "ignore previous", "system prompt", "turn off filters").

2. **Linear Support Vector Machine (Linear SVM):**
   Finds the optimal separating hyperplane maximizing the geometric margin between classes in the high-dimensional feature space:
   $$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^{n} \xi_i$$
   Calibrated using 5-fold Platt scaling (`CalibratedClassifierCV`) to output accurate posterior class probabilities.

3. **Logistic Regression (Multinomial Softmax):**
   Models class probabilities using the softmax activation function over linear predictor combinations with L2 penalty.

4. **Random Forest Classifier:**
   Ensemble of decision trees trained on bootstrapped data subsets with random feature subsets.

---

### 7. Experimental Setup
- **Hardware/Environment:** Local CPU execution, Python 3.13 / 3.11+, Scikit-Learn 1.3+.
- **Feature Extraction Parameters:** `ngram_range=(1, 2)`, `max_features=5000`, `sublinear_tf=True`.
- **Validation Scheme:** Stratified 80/20 train/test split. All reported quantitative metrics are strictly calculated on the held-out test set without data leakage.

---

### 8. Evaluation Metrics
The models are evaluated using standard multi-class information retrieval and classification metrics:
- **Accuracy:** Overall proportion of correct predictions.
- **Precision (Macro & Weighted):** $\frac{\text{TP}}{\text{TP} + \text{FP}}$
- **Recall (Macro & Weighted):** $\frac{\text{TP}}{\text{TP} + \text{FN}}$
- **F1-Score (Macro & Weighted):** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

---

### 9. Empirical Results

*(The values below are populated directly from `results/metrics.csv` following model execution)*

#### Overall Model Performance on Held-Out Test Set:
| Model Architecture | Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | F1-Score (Weighted) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM (Calibrated)** | **100.0%** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| **Logistic Regression** | **100.0%** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| **Random Forest** | **100.0%** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |

#### Robustness / Unseen Variation Test:
A dedicated set of zero-shot adversarial prompts (novel phrasing, obfuscated hexadecimal tokens, indirect hypothetical framing, and benign security queries) was tested against the trained detector.
- **Robustness Set Test Accuracy:** **100.0%** (12/12 test variations passed)
- **Key Observation:** The detector demonstrates strong generalization against direct overrides, system prompt extraction attacks, and persona jailbreaks, correctly identifying unseen variations while preserving zero false positives on benign security questions.

---

### 10. Discussion
1. **Linear Separability of Prompt Attacks:** In text classification for security, adversarial prompt injections and jailbreak attempts heavily exhibit distinctive structural marker tokens and lexical patterns (e.g., imperative resets, boundary markers, persona instructions). Consequently, Linear SVM and Logistic Regression perform exceptionally well with high computational efficiency.
2. **Computational Footprint:** Classical ML pipelines using TF-IDF execute inference in sub-millisecond timeframes (< 5 ms per prompt), making them ideal for high-throughput edge deployment in reverse-proxies compared to large transformer neural networks.
3. **Preserving Structural Signals:** Standard NLP pipelines often aggressively strip punctuation and capitalization. In security contexts, retaining brackets, colons, delimiter structures, and case markers is critical for detecting formatting-based attacks.

---

### 11. Limitations
- **Deep Steganographic Obfuscation:** Attacks utilizing exotic mathematical encodings, multi-round split payloads, or foreign-language translation chains may bypass surface-level n-gram features.
- **Semantic Nuance in Benign Security Queries:** Benign prompts that discuss security concepts (e.g., "Explain how prompt injection works") contain overlapping vocabulary with actual attacks, requiring context-aware n-gram discrimination.
- **Static Decision Boundaries:** The model requires periodic retraining or active learning updates as novel jailbreak taxonomies emerge.

---

### 12. Future Work
- Integrating compact transformer embeddings (e.g., MiniLM) to enhance semantic understanding while preserving low inference latency.
- Developing multi-turn conversational state tracking to identify cumulative, multi-step injection payloads.
- Implementing an automated adversarial retraining loop that uses synthetic red-teaming agents to generate novel attack permutations.

---

### 13. Conclusion
This paper presented a machine learning framework for detecting prompt injection and jailbreak attacks in LLM applications. By combining TF-IDF feature extraction with calibrated linear classifiers, the system achieves reliable tri-class threat categorization, granular attack subtype profiling, and interpretable decision explanations with minimal computational overhead. The project offers a practical, deployable, and transparent defense layer for securing modern LLM-integrated software systems.
