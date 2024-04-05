from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__) 

# Loading all the saved models.
dt_model = joblib.load('models/nate_decision_tree.sav')
knn_model = joblib.load('models/nate_knn.sav')
lr_model = joblib.load('models/nate_logistic_regression.sav')
rf_model = joblib.load('models/nate_random_forest.sav')
svm_model = joblib.load('models/SVM_model.sav')
xgb_model = joblib.load('models/XGBoost_model.sav')

loaded_models = {'dt': dt_model,'knn': knn_model,'lr': lr_model,'rf': rf_model,'svm': svm_model,'xgb': xgb_model}

def decode(pred):
    if pred == 1: return 'Customer Exits'
    else: return 'Customer Stays'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/userinput', methods=['GET', 'POST'])
def userinput():
    # Initial rendering.
    result = [{'model':'Decision Tree', 'prediction':' '},
              {'model': 'K-nearest Neighbors', 'prediction': ' '},
              {'model': 'Logistic Regression', 'prediction': ' '},
              {'model': 'Random Forest', 'prediction': ' '},
              {'model': 'SVM', 'prediction': ' '},
              {'model': 'XGBoost', 'prediction': ' '}]
    
    # Created main dictionary.
    maind = {}
    maind['customer'] = {}
    maind['predictions'] = result

    return render_template('userinput.html', maind=maind)


@app.route('/predict', methods=['POST'])
def predict():
    # List values received from index
    values = [x for x in request.form.values()]

    # new_array:input to models
    new_array = np.array(values).reshape(1, -1)
    print(new_array)
    print(values)

    # Key names for customer dictionary custd
    cols = ['CreditScore',
            'Geography',
            'Gender',
            'Age',
            'Tenure',
            'Balance',
            'NumOfProducts',
            'HasCrCard',
            'IsActiveMember',
            'EstimatedSalary']

    # Create customer dictionary
    custd = {}
    for k, v in  zip(cols, values):
        custd[k] = v

    # Convert 1 or 0 to Yes or No    
    yn_val = ['HasCrCard', 'IsActiveMember']
    for val in  yn_val:
        if custd[val] == '1': custd[val] = 'Yes'
        else: custd[val] = 'No'

    # Loop through 'loaded_models' dictionary and saved predictiond to the list.
    predl = []
    for m in loaded_models.values():
        predl.append(decode(m.predict(new_array)[0]))

    result = [
            {'model':'Decision Tree', 'prediction':predl[0]},
            {'model': 'K-nearest Neighbors', 'prediction': predl[1]},
            {'model': 'Logistic Regression', 'prediction': predl[2]},
            {'model': 'Random Forest', 'prediction': predl[3]},
            {'model': 'SVM', 'prediction': predl[4]},
            {'model': 'XGBoost', 'prediction': predl[5]}
            ]

    # Create main dictionary
    maind = {}
    maind['customer'] = custd
    maind['predictions'] = result

    return render_template('userinput.html', maind=maind)


if __name__ == '__main__':
    app.run(debug=True)