from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'linear_regression_model.joblib')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get advertisement spending from form
    ad_spend = float(request.form['ad_spend'])
    
    # Make prediction
    prediction = model.predict([[ad_spend]])[0]
    
    return render_template('index.html', prediction=f"Predicted Sales Revenue: ${prediction:.2f}")

application = app

if __name__ == '__main__':
    app.run()
