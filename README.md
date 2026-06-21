# Decodelabs
 This repository contains all four projects completed during the DecodeLabs AI Internship (Batch June 2026).
## Project 1: Rule-Based Chatbot

This project implements a simple rule-based chatbot in Python as part of the DecodeLabs AI Internship (June 2026).

### Features
- Continuous input loop with exit command
- Input sanitization using `.lower()` and `.strip()` for case-insensitive, whitespace-tolerant handling
- Dictionary-based knowledge base with at least 5 predefined intents
- Fallback response for unrecognized inputs
- Clean and minimal code structure for easy readability

### How to Run
1. Navigate to the `project1-chatbot` folder.
2. Run the script:
   ```bash
   python chatbot.py
3. Type messages into the console. Use exit to end the session.


### 2. KNN Classification (Iris Dataset)
- Performs Exploratory Data Analysis (EDA) with pairplots and correlations.
- Preprocessing: feature scaling (standardization) and train-test split.
- Model: K-Nearest Neighbors (KNN) with evaluation (accuracy, F1 score, confusion matrix).
- Hyperparameter tuning: error rate vs K curve to study overfitting/underfitting.
- Insight: petal length and width are most discriminative features.
