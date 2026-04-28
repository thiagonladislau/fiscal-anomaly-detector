# Tax Anomaly Detector

A practical project focused on identifying tax inconsistencies using Machine Learning. This project was developed as a hands-on study of the concepts presented in the book **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"** by **Aurélien Géron**.

## Project Overview
This tool simulates a corporate tax environment where invoices are issued with a standard 12% tax rate. By implementing a Linear Regression model, the system can "learn" the tax pattern and identify records that deviate from the rule (anomalies), simulating errors or system glitches.

## Technical Results
After training the model using the `tax_data.csv` dataset, the following results were achieved:

- **Model Coefficient:** 0.1229 (The AI successfully identified the ~12% tax pattern).
- **RMSE (Root Mean Squared Error):** 6.09 (The model has an average error of only 6.09 units per invoice).

## Practical Example (Case Study)
The system identified **Invoice ID 956** as a critical anomaly:
- **Invoice Value:** 14,587.22
- **Actual Tax Found:** 2,625.70 (18% rate)
- **Expected Tax (AI Prediction):** ~1,750.46 (12% rate)

**Result:** The discrepancy was flagged automatically, saving time and avoiding potential fiscal penalties.

## Roadmap
- [x] Initial setup and Git repository
- [x] Data simulation and exploration (Chapter 2 - Hands-On ML)
- [x] Data cleaning and pipeline creation
- [x] Model training for anomaly detection (Linear Regression)
- [ ] Model deployment/automation

## Technologies Used
- **Python 3.12**
- **Pandas** (Data manipulation)
- **Scikit-Learn** (Machine Learning)
- **Matplotlib/Seaborn** (Data Visualization)