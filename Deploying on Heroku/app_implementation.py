import json
import requests

# Define the API URL
url = 'http://127.0.0.1:8000/diabetes_prediction'

# Correct input data for person is diabetic
'''

input_data_for_model = {
    'pregnancies': 6,
    'Glucose': 148,
    'BloodPressure': 72,
    'SkinThickness': 35,
    'Insulin': 0,
    'BMI': 33.6,
    'DiabetesPedigreeFunction': 0.627,  # ✅ Fixed spelling
    'Age': 50
}   
 
'''

# correct input data for person in not diabetic
input_data_for_model = {
    'pregnancies': 1,
    'Glucose': 85,
    'BloodPressure': 66,
    'SkinThickness': 29,
    'Insulin': 0,
    'BMI': 26.6,
    'DiabetesPedigreeFunction': 0.351,  # ✅ Fixed spelling
    'Age': 31
}

# Send JSON request properly
response = requests.post(url, json=input_data_for_model)

# Print the API response
print(response.json())  # ✅ .json() ensures correct parsing
