# Anemia Prediction using Machine Learning

A machine learning-based web application that predicts whether a person is **Anemic** or **Not Anemic** using hematological parameters.

The project includes data analysis, multiple machine learning classification models, model comparison, a trained Random Forest model, and a Flask-based web application for real-time prediction.

> **Disclaimer:** This project is developed for educational purposes and is not intended to replace professional medical diagnosis.

## Project Overview

Anemia Prediction is a supervised machine learning classification project that analyzes blood-related parameters and predicts the anemia status of an individual.

The web application allows users to enter patient-related parameters and receive a prediction from a trained Random Forest model.

## Features

* User registration and login
* Dataset upload and preview
* Machine learning model comparison
* Anemia prediction through a web interface
* Trained Random Forest model integration
* MySQL database connectivity
* Flask-based web application

## Input Features

The prediction model uses the following inputs:

* Gender
* Hemoglobin
* MCH
* MCHC
* MCV

The application returns one of two predictions:

* **Anemic**
* **Not Anemic**

## Machine Learning Models

The project compares the following classification algorithms:

* Random Forest
* Decision Tree
* Stacking Classifier
* MLP
* SVM
* KNN
* XGBoost
* Gradient Boosting Classifier

### Model Performance

| Model               | Accuracy |
| ------------------- | -------: |
| Random Forest       |   99.69% |
| Decision Tree       |   99.69% |
| Stacking Classifier |   99.69% |
| MLP                 |   96.57% |
| SVM                 |   93.46% |
| KNN                 |   91.59% |
| Gradient Boosting   |   54.74% |
| XGBoost             |   51.58% |

These are the model accuracy values currently used in the application's model comparison functionality.

## Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Preparation
   ↓
Train Multiple Classification Models
   ↓
Evaluate Model Performance
   ↓
Select Trained Model
   ↓
Save Model using Joblib
   ↓
Flask Web Application
   ↓
User Input
   ↓
Anemia Prediction
```

## Technologies Used

### Programming Language

* Python

### Data Science & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

### Web Development

* Flask
* HTML
* CSS

### Database

* MySQL
* MySQL Connector

### Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

## Project Structure

```text
Anemia-Prediction/
│
├── anemia.csv
├── x_train.csv
├── RF.joblib
├── main.ipynb
├── main-ref.ipynb
├── app.py
├── db.sql
├── requirements.txt
├── compario project.zip
└── README.md
```

These files are currently present in the repository.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Srihitha-A/Anemia-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Anemia-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

The application uses MySQL for storing user information.

1. Install MySQL.
2. Create the required database.
3. Execute the SQL commands available in `db.sql`.
4. Configure your MySQL credentials in the application.

## Run the Application

Start the Flask application using:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

The Flask application provides routes for registration, login, dataset upload, model comparison, and prediction.

## Prediction Process

The user provides:

```text
Gender
Hemoglobin
MCH
MCHC
MCV
```

The application converts the gender value into the required numerical format, prepares the input features, loads the trained `RF.joblib` model, and generates the prediction.

```text
User Input
    ↓
Feature Conversion
    ↓
RF.joblib
    ↓
Random Forest Prediction
    ↓
Anemic / Not Anemic
```

## Results

The project demonstrates that several classification algorithms achieved high accuracy on the evaluated dataset, with Random Forest, Decision Tree, and Stacking Classifier reaching approximately **99.69% accuracy** in the application's reported comparison.

Accuracy alone should not be interpreted as clinical performance. Further validation would be required before considering a model for real-world medical use.

## Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing
* Exploratory Data Analysis
* Supervised Machine Learning
* Classification algorithms
* Model comparison
* Model evaluation
* Random Forest
* Model serialization using Joblib
* Flask application development
* MySQL integration
* Integrating a trained ML model into a web application

## Future Improvements

* Perform stronger model validation using cross-validation.
* Add additional evaluation metrics such as ROC-AUC.
* Improve model interpretability.
* Secure database credentials using environment variables.
* Improve input validation and error handling.
* Deploy the application to a cloud platform.
* Add automated testing.

## Disclaimer

This application is an academic machine learning project and is **not a medical diagnostic system**. Predictions should not be used as a substitute for evaluation by a qualified healthcare professional.

