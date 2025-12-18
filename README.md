# Fake News Detection using Logistic Regression + TF-IDF

This is an introductory machine learning project designed to classify news articles as real or fake. It serves as a first project to explore the end-to-end process of model training and deployment via a web interface.

## Table of Contents
1. [Model Development](#1-model-development)
   - [Overview](#overview)
   - [How to Use](#how-to-use)
   - [Model Performance](#model-performance)
2. [Web Application](#2-web-application)
   - [Features](#features)
   - [Tech Stack](#tech-stack)
   - [Installation and Setup](#installation-and-setup)

---

## 1. Model Development

This section handles the training and evaluation of the model

This project builds a fake news detection model using:
- **WELFake Dataset from Kaggle**
- **TF-IDF Vectorization** (Unigrams and Bigrams)
- **Logistic Regression**
- **POS Awareness** (Part-of-Speech)
- **Hyperparameter Tuning** (GridSearchCV)

### How to Use
1. Clone this repository.
2. Add your Kaggle API credentials in the first cell of the notebook.
3. Run the notebook in Google Colab or Jupyter.
4. The model will:
   - Train on the dataset from Kaggle.
   - Perform text cleaning and preprocessing.
   - Evaluate its performance and save the model files.

### Model Performance
After hyperparameter tuning, the best model achieved the following results on the test set using bigrams:

| Metric         | Value  |
|----------------|--------|
| Test Accuracy  | 0.9639 |
| Test Precision | 0.9593 |
| Test Recall    | 0.9704 |
| Test F1 Score  | 0.9648 |
| Test ROC-AUC   | 0.9937 |

**Note:** Bigram TF-IDF slightly outperformed unigram TF-IDF in both training and testing metrics.

---

## 2. Web Application

This section handles the deployment of the model into a functional web interface for real-time predictions.

### Features
- **FastAPI Backend**: A Python API for model inference.
- **Interactive UI**: A simple web interface with loading states.
- **Text Preprocessing**: NLTK-based cleaning (lemmatization and stopword removal).

### Tech Stack
- **Backend**: Python (FastAPI, Scikit-Learn, Joblib, NLTK)
- **Frontend**: HTML, CSS, JavaScript 

### Installation and Setup

**1. Clone the repository**
**2. Create a Virtual Environment**
**3. Install Dependencies**
**4. Configure Environment**
**5. Run the application**
