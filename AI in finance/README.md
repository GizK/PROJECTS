# **AI in Finance: Credit Risk Classification**
*Machine Learning • Explainable AI • Ethical Credit Scoring • XGBoost • SHAP*

This project explores how AI can classify credit risk into **Low**, **Average**, and **High** categories using four machine learning algorithms.  
It focuses on the balance between **accuracy**, **fairness**, and **explainability**, which is essential for responsible AI in financial services.

---

## **Project Features**
- Multi‑class credit risk classification using four algorithms  
- Leak‑free preprocessing pipeline with OneHotEncoder and ColumnTransformer  
- Hyperparameter tuning using RandomizedSearchCV  
- Confusion Matrix and ROC‑AUC evaluation  
- SHAP explainability for transparent model decisions  
- Ethical and regulatory reflection (GDPR Article 22, EU AI Act)  
- Comparison of interpretability vs performance across models  

---

## **Project Description**
- Credit scoring is a supervised classification task used by lenders to assess borrower reliability.  
- Traditional models are interpretable but limited in capturing non‑linear financial behaviour.  
- Advanced models such as XGBoost and Neural Networks offer higher accuracy but reduced transparency.  
- This project evaluates Logistic Regression, KNN, XGBoost, and Neural Networks under the same preprocessing and evaluation pipeline.  
- SHAP is used to explain model predictions and ensure fairness and accountability.  
- The goal is to demonstrate that high‑performing and explainable AI is achievable in finance.

---

## **Technologies & Methods Used**
- Python (scikit‑learn, XGBoost, SHAP)  
- OneHotEncoder + ColumnTransformer  
- StratifiedKFold cross‑validation  
- RandomizedSearchCV hyperparameter tuning  
- Confusion Matrix, ROC‑AUC, F1‑score, Recall  
- SHAP global feature importance  
- Ethical AI frameworks (GDPR, EU AI Act)  

---

## **Model Performance Summary**
- Logistic Regression: strong interpretability, high accuracy, perfect recall for high‑risk borrowers  
- KNN: simple and intuitive, but sensitive to scaling and less stable  
- Neural Network: high learning capability, strong accuracy, lower explainability  
- XGBoost: highest accuracy, perfect ROC‑AUC, excellent handling of non‑linear patterns, SHAP‑explainable  

---

## **My Contribution ( XGBoost + SHAP)**
- Implemented the XGBoost model with a leak‑free preprocessing pipeline  
- Performed hyperparameter tuning using RandomizedSearchCV  
- Generated confusion matrix, ROC‑AUC curves, and SHAP visualisations  
- Interpreted feature importance and SHAP impact for transparency  
- Connected results to fairness, accountability, and regulatory compliance  
- Demonstrated how XGBoost + SHAP can achieve both accuracy and explainability  

---

## **What I Learned**
- How to build and evaluate multi‑class machine learning models  
- How to design preprocessing pipelines that prevent data leakage  
- How to tune hyperparameters effectively  
- How to interpret confusion matrices and ROC‑AUC curves  
- How SHAP provides transparent explanations for model decisions  
- How to compare interpretability vs performance across algorithms  
- How ethical AI principles apply to financial decision‑making  

---

## **Ethical & Professional Reflection**
- Fairness: SHAP ensures transparent reasoning behind credit decisions  
- Transparency: Supports GDPR Article 22 and EU AI Act requirements  
- Accountability: Pipeline design ensures reproducibility and auditability  
- Trust: Explainable models increase user and regulator confidence  
- Professional responsibility: Emphasises safe, bias‑aware deployment of AI in finance  

