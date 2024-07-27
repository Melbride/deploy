import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Define input fields with descriptions and placeholders
descriptions = {
    'Gender': 'Enter 1 for Male, 0 for Female',
    'Senior Citizen': 'Enter 1 if the customer is a senior citizen, 0 otherwise',
    'Partner': 'Enter 1 if the customer has a partner, 0 otherwise',
    'Dependents': 'Enter 1 if the customer has dependents, 0 otherwise',
    'Tenure': 'Number of months the customer has been with the company',
    'Phone Service': 'Enter 1 if the customer has phone service, 0 otherwise',
    'Online Security': 'Enter 1 if the customer has online security, 0 otherwise',
    'Online Backup': 'Enter 1 if the customer has online backup, 0 otherwise',
    'Device Protection': 'Enter 1 if the customer has device protection, 0 otherwise',
    'Tech Support': 'Enter 1 if the customer has tech support, 0 otherwise',
    'Streaming TV': 'Enter 1 if the customer has streaming TV, 0 otherwise',
    'Streaming Movies': 'Enter 1 if the customer has streaming movies, 0 otherwise',
    'Paperless Billing': 'Enter 1 if the customer has paperless billing, 0 otherwise',
    'Monthly Charges': 'The amount charged monthly to the customer',
    'Total Charges': 'The total amount charged to the customer',
    'No Phone Service': 'Enter 1 if the customer has no phone service, 0 otherwise',
    'Fiber Optic': 'Enter 1 if the customer has fiber optic internet, 0 otherwise',
    'No Internet Service': 'Enter 1 if the customer has no internet service, 0 otherwise',
    'Contract: One Year': 'Enter 1 if the customer is on a one-year contract, 0 otherwise',
    'Contract: Two Years': 'Enter 1 if the customer is on a two-year contract, 0 otherwise',
    'Payment Method: Credit Card': 'Enter 1 if the payment method is credit card, 0 otherwise',
    'Payment Method: Electronic Check': 'Enter 1 if the payment method is electronic check, 0 otherwise',
    'Payment Method: Mailed Check': 'Enter 1 if the payment method is mailed check, 0 otherwise',
    'Encoded Customer ID': 'A unique identifier for the customer (numerical)'
}

# Create input fields with descriptions and placeholders
features = {}
for feature in descriptions:
    features[feature] = st.text_input(feature, '', help=descriptions[feature])

if st.button("Predict"):
    try:
        # Prepare the input data
        payload = {f'feature{i+1}': features[feature] for i, feature in enumerate(descriptions)}
        
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
