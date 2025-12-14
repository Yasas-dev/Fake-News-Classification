# Fake News Detection using Logistic Regression + TF-IDF

This project builds a fake news detection model using:
- **WELFake Dataset from kaggle**
- **TF-IDF Vectorization**
- **Logistic Regression**
- **POS Awareness (Part-of-Speech)**
- **Hyperparameter Tuning (GridSearchCV)**
- **Included both unigrams and bigrams**

## How to Use
1. Clone this repository.
2. Add your Kaggle API credentials in the first cell of the notebook.
3. Run the notebook in Google Colab or Jupyter.
4. The model will:
   - Train on a dataset from Kaggle.
   - Evaluate its performance.

## Model Performance

After hyperparameter tuning, the **best model achieved the following results on the test set using bigrams**:  

| Metric         | Value  |
|----------------|--------|
| Test Accuracy  | 0.9639 |
| Test Precision | 0.9593 |
| Test Recall    | 0.9704 |
| Test F1 Score  | 0.9648 |
| Test ROC-AUC   | 0.9937 |

> **Note:** Bigram TF-IDF slightly outperformed unigram TF-IDF in both training and testing metrics.
