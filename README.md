### end to end Medical insurance cost prediction project

📌 Project Overview

The Medical Insurance Cost Prediction project aims to estimate an individual's medical insurance charges based on demographic and lifestyle factors such as age, gender, BMI, smoking habits, and region.
By building this model, insurance companies can better assess risks and individuals can get insights into how their lifestyle choices affect insurance costs.

🎯 Objective

Develop an end-to-end machine learning pipeline to predict medical insurance costs.

Implement a modular project structure for scalability and maintainability.

Demonstrate industry-standard ML workflow: data ingestion → transformation → model training → evaluation.

📊 Dataset

Source: Kaggle – Medical Cost Personal Dataset

Features:

age – Age of the individual

sex – Gender (male, female)

bmi – Body Mass Index

children – Number of dependents

smoker – Smoking status (yes, no)

region – Residential area (northeast, northwest, southeast, southwest)

charges – Medical insurance cost (Target Variable)

🛠️ Tech Stack

Languages & Libraries

Python (3.x)

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Joblib / Pickle

Workflow & Tools

Modular Python scripting

Logging & Exception Handling

Version Control (Git & GitHub)

Virtual Environment

📂 Project Structure
MedicalInsuranceCostPrediction/
│
├── data/                     # Raw dataset
├── notebooks/                # Jupyter notebooks for EDA & experiments
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   ├── prediction_pipeline.py
│   ├── utils.py
│
├── artifacts/                # Saved models & preprocessing objects
├── requirements.txt          # Required packages
├── README.md                 # Project documentation
└── app.py       

📈 Workflow

Data Ingestion – Load dataset from source and split into train/test sets.

Data Transformation – Handle missing values, encode categorical variables, and scale numerical features.

Model Training – Train multiple regression models (Linear Regression, Random Forest, etc.) and select the best based on performance metrics.

Evaluation – Evaluate using MAE, MSE, RMSE, and R² Score.

🔍 Exploratory Data Analysis (EDA)

Distribution of numerical features

Correlation heatmap

Impact of smoking on insurance charges

BMI vs. charges relationship

📊 Model Performance
aquired 96% accuracy using the xg boost regressor 

💡 Key Learnings

Implementing a clean and modular end-to-end ML project structure.

Applying feature engineering and data preprocessing techniques.

Model selection & hyperparameter tuning for better performance.

Understanding the relationship between lifestyle choices and medical expenses.
