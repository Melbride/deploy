import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Define options for dropdowns
dropdown_options = {
    'Gender': ['Male', 'Female'],
    'Senior Citizen': ['0', '1'],
    'Partner': ['0', '1'],
    'Dependents': ['0', '1'],
    'Phone Service': ['0', '1'],
    'Online Security': ['0', '1'],
    'Online Backup': ['0', '1'],
    'Device Protection': ['0', '1'],
    'Tech Support': ['0', '1'],
    'Streaming TV': ['0', '1'],
    'Streaming Movies': ['0', '1'],
    'Paperless Billing': ['0', '1'],
    'No Phone Service': ['0', '1'],
    'Fiber Optic': ['0', '1'],
    'No Internet Service': ['0', '1'],
    'Contract: One Year': ['0', '1'],
    'Contract: Two Years': ['0', '1'],
    'Payment Method: Credit Card': ['0', '1'],
    'Payment Method: Electronic Check': ['0', '1'],
    'Payment Method: Mailed Check': ['0', '1']
}

# Define input fields with dropdowns for categorical features
features = {}
for feature, options in dropdown_options.items():
    features[feature] = st.selectbox(feature, options)

# Define input fields for numerical features
numerical_features = {
    'Tenure': 'Number of months with the company',
    'Monthly Charges': 'Amount charged monthly',
    'Total Charges': 'Total amount charged',
    'Encoded Customer ID': 'Numerical unique customer identifier'
}

for feature, placeholder in numerical_features.items():
    features[feature] = st.text_input(feature, placeholder=placeholder, value='')

if st.button("Predict"):
    try:
        # Prepare the input data
        payload = {f'feature{i+1}': features[feature] for i, feature in enumerate(dropdown_options.keys())}
        payload.update({f'feature{i+len(dropdown_options)+1}': features[feature] for i, feature in enumerate(numerical_features)})

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
