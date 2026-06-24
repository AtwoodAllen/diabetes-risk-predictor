Diabetes Risk Prediction Using Machine Learning


A Data Science Graduation Project — Cavendish University Uganda

Project Overview

This project applies machine learning to predict whether a patient is at risk of diabetes based on basic medical measurements. It was developed as a graduation project for the Diploma in Data Science and Analytics at Cavendish University Uganda.

The project delivers three key outputs:


A trained Random Forest classification model
An interactive Power BI dashboard for data visualisation
A live Streamlit web application for real-time predictions

Objectives


Explore and analyse the Pima Indians Diabetes Dataset to identify key risk factors
Clean and prepare the data for machine learning
Build, train, and evaluate a diabetes risk prediction model
Visualise findings using a Power BI dashboard
Deploy a prediction application accessible via web browser



Dataset

Pima Indians Diabetes Dataset — UCI Machine Learning Repository (via Kaggle)

FeatureDescriptionPregnanciesNumber of times pregnantGlucosePlasma glucose concentrationBloodPressureDiastolic blood pressure (mm Hg)SkinThicknessTriceps skin fold thickness (mm)Insulin2-hour serum insulin (mu U/ml)BMIBody mass indexDiabetesPedigreeFunctionGenetic influence scoreAgeAge in yearsOutcomeTarget: 1 = diabetic, 0 = non-diabetic


768 patient records
65.1% non-diabetic, 34.9% diabetic
Source: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database



Tools & Technologies

ToolPurposePythonData analysis and model buildingPandas & NumPyData manipulationMatplotlib & SeabornData visualisationScikit-learnMachine learningStreamlitWeb applicationPower BIInteractive dashboardJupyter NotebookDevelopment environmentGitHubVersion control


 Model Performance

Algorithm: Random Forest Classifier (100 trees)

MetricScoreAccuracy76.6%Precision66.7%Recall69.1%F1 Score67.9%

Confusion Matrix:

Predicted: No DiabetesPredicted: DiabetesActual: No Diabetes80 (TN)19 (FP)Actual: Diabetes17 (FN)38 (TP)

Top predictors: Glucose (0.26), BMI (0.16), Age (0.14), DiabetesPedigreeFunction (0.12)


Live App

The prediction app is deployed and accessible here:

https://diabetes-risk-predictor-gurdylrj7jmxlu4qmtrodj.streamlit.app/

How it works:


Enter 8 patient medical measurements
Click Predict Diabetes Risk
Receive an instant prediction with probability score and recommended actions



Project Structure

diabetes-risk-predictor/
│
├── app.py                  ← Streamlit prediction application
├── diabetes_model.pkl      ← Trained Random Forest model
├── scaler.pkl              ← Fitted StandardScaler
├── requirements.txt        ← Python dependencies
└── README.md               ← Project documentation


 Run Locally

1. Clone the repository

bashgit clone https://github.com/AtwoodAllen/diabetes-risk-predictor.git
cd diabetes-risk-predictor

2. Install dependencies

bashpip install -r requirements.txt

3. Run the app

bashstreamlit run app.py

4. Open in browser

https://diabetes-risk-predictor-gurdylrj7jmxlu4qmtrodj.streamlit.app/


 Key Findings


Glucose had the strongest correlation with diabetes outcome (r = 0.47)
BMI and Age were the second and third most important predictors
Diabetic patients had noticeably higher average glucose levels than non-diabetic patients
The dataset had a mild class imbalance (65/35) which slightly biases predictions toward non-diabetic



Recommendations for Future Work


Apply SMOTE to address class imbalance and improve recall
Test on more diverse and locally relevant patient datasets (e.g. Ugandan health data)
Compare Random Forest against XGBoost and Neural Networks
Deploy the app as a mobile-friendly Progressive Web App
Integrate with hospital management systems for real-time clinical use



 Disclaimer

This application is a decision-support tool only and does not replace clinical diagnosis. All predictions should be validated by a qualified healthcare professional before any medical decisions are made.


 Author

Nassolo Allen Justine
Diploma in Data Science and Analytics
Faculty of Science and Technology
Cavendish University Uganda
Kampala, Uganda | 2026


License

This project is for academic purposes only.