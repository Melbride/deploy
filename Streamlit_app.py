import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Define placeholder texts for each input field
placeholders = {
    'Gender': '1 for Male, 0 for Female',
    'Senior Citizen': '1 if Senior Citizen, 0 otherwise',
    'Partner': '1 if Has Partner, 0 otherwise',
    'Dependents': '1 if Has Dependents, 0 otherwise',
    'Tenure': 'Number of months with the company',
    'Phone Service': '1 if Has Phone Service, 0 otherwise',
    'Online Security': '1 if Has Online Security, 0 otherwise',
    'Online Backup': '1 if Has Online Backup, 0 otherwise',
    'Device Protection': '1 if Has Device Protection, 0 otherwise',
    'Tech Support': '1 if Has Tech Support, 0 otherwise',
    'Streaming TV': '1 if Has Streaming TV, 0 otherwise',
    'Streaming Movies': '1 if Has Streaming Movies, 0 otherwise',
    'Paperless Billing': '1 if Paperless Billing, 0 otherwise',
    'Monthly Charges': 'Amount charged monthly',
    'Total Charges': 'Total amount charged',
    'No Phone Service': '1 if No Phone Service, 0 otherwise',
    'Fiber Optic': '1 if Fiber Optic, 0 otherwise',
    'No Internet Service': '1 if No Internet Service, 0 otherwise',
    'Contract: One Year': '1 if on One Year Contract, 0 otherwise',
    'Contract: Two Years': '1 if on Two Years Contract, 0 otherwise',
    'Payment Method: Credit Card': '1 if Payment by Credit Card, 0 otherwise',
    'Payment Method: Electronic Check': '1 if Payment by Electronic Check, 0 otherwise',
    'Payment Method: Mailed Check': '1 if Payment by Mailed Check, 0 otherwise',
    'Encoded Customer ID': 'Numerical unique customer identifier'
}

# Create input fields with placeholders
features = {}
for feature in placeholders:
    features[feature] = st.text_input(feature, placeholder=placeholders[feature])

if st.button("Predict"):
    try:
        # Prepare the input data
        payload = {f'feature{i+1}': features[feature] for i, feature in enumerate(placeholders)}
        
        # Call the Flask API
        response = requests.post('http://localhost:5000/predict', data=payload)
        result = response.json()

        # Display the result
        if 'prediction' in result:
            st.write(f"Prediction: {result['prediction']}")
        else:
            st.write(f"Error: {result['error']}")
    except Exception as e:
        st.write(f"An error occurred: {e}")
