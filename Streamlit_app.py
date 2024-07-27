import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Define input fields based on your feature names
features = {}
for feature in [
    'Gender', 'Senior Citizen', 'Partner', 'Dependents',
    'Tenure', 'Phone Service', 'Online Security', 'Online Backup', 'Device Protection',
    'Tech Support', 'Streaming TV', 'Streaming Movies', 'Paperless Billing',
    'Monthly Charges', 'Total Charges', 'No Phone Service', 'Fiber Optic',
    'No Internet Service', 'Contract: One Year', 'Contract: Two Years', 'Payment Method: Credit Card',
    'Payment Method: Electronic Check', 'Payment Method: Mailed Check', 'Encoded Customer ID'
]:
    features[feature] = st.text_input(feature, '')

if st.button("Predict"):
    try:
        # Prepare the input data
        payload = {f'feature{i+1}': features[feature] for i, feature in enumerate(features)}
        
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
