from flask import Flask, url_for, redirect, render_template, request, session,flash
import pandas as pd
import numpy as np
import mysql.connector
import joblib
from sklearn.linear_model import LogisticRegression
from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'admin'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suji@1411",
    port="3306",
    database='db'
)

mycursor = mydb.cursor()

def executionquery(query,values):
    mycursor.execute(query,values)
    mydb.commit()
    return

def retrivequery1(query,values):
    mycursor.execute(query,values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index2')
def index2():
    return render_template("index2.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['conformpassword']
        if password == c_password:
            query = "SELECT UPPER(email) FROM user3"
            email_data = retrivequery2(query)
            email_data_list = []
            for i in email_data:
                email_data_list.append(i[0])
            if email.upper() not in email_data_list:
                query = "INSERT INTO user3 (name, email, password) VALUES (%s, %s, %s)"
                values = (name, email, password)
                executionquery(query, values)
                flash("Registration successful!", "success")
                return render_template('login.html', message="Successfully Registered!")
            return render_template('register.html', message="This email ID is already exists!")
        return render_template('register.html', message="Conform password is not match!")
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT UPPER(email) FROM user3"
        email_data = retrivequery2(query)
        email_data_list = []
        for i in email_data:
            email_data_list.append(i[0])
        
        if email.upper() in email_data_list:
            query = "SELECT UPPER(password) FROM user3 WHERE email = %s"
            values = (email,)
            password__data = retrivequery1(query, values)
            if password.upper() == password__data[0][0]:
                global user_email
                user_email = email

                return redirect("/home")
            return render_template('login.html', message= "Invalid Password!!")
        return render_template('login.html', message= "This email ID does not exist!")
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if a file is uploaded
        if 'file' not in request.files:
            return render_template('upload.html', msg="No file part")
        
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg="No selected file")
        
        # If file is present, read the CSV
        try:
            df = pd.read_csv(file)
            dataset = df.head(500)  # Show only the first 100 rows
            columns = dataset.columns.values
            rows = dataset.values.tolist()
            return render_template('upload.html', columns=columns, rows=rows, msg="Dataset Uploaded Successfully")
        except Exception as e:
            return render_template('upload.html', msg=f"Error: {str(e)}")

    # Render the page with the file upload form
    return render_template('upload.html')

@app.route('/model', methods=['POST', 'GET'])
def model():
    if request.method == "POST":
        s = request.form['algo']
        accuracy_map = {
            'RandomForest': 0.9968847352024922,
            'MLP': 0.9657320872274143,
            'StackingClassifier': 0.9968847352024922,
            'SVM': 0.9345794392523364,
            'KNN': 0.9158878504672897,
            'DecisionTree': 0.9968847352024922,
            'XGBoost': 0.5157894736842106,
            'GradientBoostingClassifier': 0.5473684210526316
        }

        if s in accuracy_map:
            acc = accuracy_map[s]
            msg = f'The accuracy obtained by the {s} is: {acc}'
            msg1 = f'The accuracy obtained by the {s} is: {acc * 100:.2f}%'
        else:
            msg = "Please select a valid algorithm."
            msg1 = ""
        return render_template('model.html', msg=msg, msg1=msg1)

    return render_template('model.html')




@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Get form values
        gender = request.form['gender']
        hemoglobin = float(request.form['hemoglobin'])
        mch = float(request.form['mch'])
        mchc = float(request.form['mchc'])
        mcv = float(request.form['mcv'])

        # Convert gender to numeric: Male = 1, Female = 0
        gender_value = 1 if gender.lower() == 'male' else 0

        # Prepare the input list
        input_data = [gender_value, hemoglobin, mch, mchc, mcv]

        # Load model
        model = joblib.load('RF.joblib')

        # Make prediction
        prediction = model.predict([input_data])

        print("Prediction Output:", prediction)

        # Interpret result
        if prediction[0] == 1:
            predicted_label = 'Anemic'
        else:
            predicted_label = 'Not Anemic'

        print("Predicted Label:", predicted_label)

        # Pass prediction to template
        return render_template('prediction.html', prediction=predicted_label)

    return render_template('prediction.html')







if __name__=="__main__":
    app.run(debug=True)