# ⭐ TrustCheck-News-Authenticity-Classifier (ML + NLP)
A complete, production-ready Machine Learning + NLP system that classifies news articles as REAL or FAKE using TF-IDF vectorization and Logistic Regression.
This project includes a training pipeline, data preprocessing, model evaluation, model saving, and a full Streamlit web application—all running 100% offline.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python"> <img src="https://img.shields.io/badge/Machine--Learning-sklearn-orange?logo=scikitlearn"> <img src="https://img.shields.io/badge/NLP-TF--IDF-green"> <img src="https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit"> <img src="https://img.shields.io/badge/Status-Production Ready-brightgreen"> </p>

# 📘 Project Overview :-
TrustCheck is a machine learning–based system designed to evaluate the credibility of news articles.
With rising misinformation across the internet, detecting fake news has become critical.

This project builds a lightweight, offline, real-time fake news classifier using:
- TF-IDF vectorization
- Logistic Regression model
- Custom text preprocessing
- Confidence-based predictions
- Interactive Streamlit app
No external APIs. No HuggingFace. No internet dependency.
Everything runs locally on your machine.

# 🎯 Key Features
1. 🚀 Machine Learning & NLP
- Text cleaning (URLs, extra spaces, newline removal)
- TF-IDF word vectorization (uni-grams + bi-grams)
- Logistic Regression classifier with balanced weights
- High accuracy and precise classification
- Model and vectorizer stored using joblib

2.💡 Streamlit Web App
- Clean and modern UI
- Paste any news text → get REAL/FAKE
- Confidence score displayed
- Outputs results inside a DataFrame
- Works fully offline

3. 🧱 Production-Ready
- Structured folders
- Reusable prediction function
- Modular + scalable code
- Ready for deployment

# 🧠 Methodology
1️⃣ Data Preparation
Dataset contains two classes:
1 → Real News
0 → Fake News
Both datasets (real.csv & fake.csv) are merged, cleaned, shuffled, and processed.

2️⃣ Text Preprocessing - Includes:
- Removal of URLs
- Removal of newline characters
- Removal of extra whitespaces
- Combining title + article body
- Regex-based text cleaning

3️⃣ Feature Engineering (TF-IDF)
- Maximum features: 10,000
- N-grams: (1,2)
: Converts text into numerical vectors representing word importance

4️⃣ Model Training - Model used:
- Logistic Regression
- class_weight="balanced"
- max_iter=3000

Chosen for:
- High performance on text classification
- Fast and interpretable
- Low computational requirements

5️⃣ Evaluation - Metrics generated:
- Accuracy
- Precision
- Recall
- F1-score
: The model performs strongly on both classes (Real & Fake).

6️⃣ Saving the Model - Both the classifier and vectorizer are saved using Joblib:
- models/model.joblib
- models/vectorizer.joblib
: These are loaded later in the Streamlit app.

# 🚀 Running the Application
1. Install Dependencies
- pip install -r requirements.txt

2. Run the Streamlit
- streamlit run Streamlit.py
A browser window will open with the TrustCheck interface.

# 🖥️ Streamlit Output Example
Input (Fake News):
- Breaking: NASA confirms aliens visited the White House last night!

Output:
Prediction: FAKE
Confidence: 97%

Input (Real News):
- WASHINGTON (Reuters) – The U.S. Senate approved a new budget framework on Monday.

Output:
- Prediction: REAL
- Confidence: 99%

# 🛠️ Technologies Used : 
- 🐍 Python
- 📚 Scikit-Learn
- 🔤 TF-IDF Vectorizer
- 📘 Pandas
- 🔧 Joblib
- 🧼 Regex
- 🖥️ Streamlit
- 📓 Jupyter Notebook

📈 Potential Enhancements
- Integrate deep learning models (BERT, RoBERTa)
- Add explainability (LIME/SHAP)
- Improve dataset variety
- Add title-only vs full-text prediction options

👤 Author
# AYUSH
Machine Learning • NLP • Artificial Intelligence
- 🔗 GitHub: https://github.com/ayush13-0
- 🔗 LinkedIn: https://www.linkedin.com/in/ayush130

