import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('churn.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define feature names
feature_names = [
    'Gender', 'Senior Citizen', 'Partner', 'Dependents',
    'Tenure', 'Phone Service', 'Online Security', 'Online Backup', 'Device Protection',
    'Tech Support', 'Streaming TV', 'Streaming Movies', 'Paperless Billing',
    'Monthly Charges', 'Total Charges', 'No Phone Service', 'Fiber Optic',
    'No Internet Service', 'Contract: One Year', 'Contract: Two Years', 'Payment Method: Credit Card',
    'Payment Method: Electronic Check', 'Payment Method: Mailed Check', 'Encoded Customer ID'
]

# Streamlit app
st.title("Customer Churn Prediction")

# Define input fields with dropdowns where needed
gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('Senior Citizen', [0, 1])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure', min_value=0)
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No Internet Service'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No Internet Service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No Internet Service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No Internet Service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No Internet Service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No Internet Service'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
monthly_charges = st.number_input('Monthly Charges', min_value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0)
no_phone_service = st.selectbox('No Phone Service', [0, 1])
fiber_optic = st.selectbox('Fiber Optic', [0, 1])
no_internet_service = st.selectbox('No Internet Service', [0, 1])
contract_one_year = st.selectbox('Contract: One Year', [0, 1])
contract_two_years = st.selectbox('Contract: Two Years', [0, 1])
payment_method_credit_card = st.selectbox('Payment Method: Credit Card', [0, 1])
payment_method_electronic_check = st.selectbox('Payment Method: Electronic Check', [0, 1])
payment_method_mailed_check = st.selectbox('Payment Method: Mailed Check', [0, 1])
encoded_customer_id = st.number_input('Encoded Customer ID', min_value=0)

# Combine input features into a list
features = [
    gender, senior_citizen, partner, dependents, tenure, phone_service,
    online_security, online_backup, device_protection, tech_support,
    streaming_tv, streaming_movies, paperless_billing, monthly_charges,
    total_charges, no_phone_service, fiber_optic, no_internet_service,
    contract_one_year, contract_two_years, payment_method_credit_card,
    payment_method_electronic_check, payment_method_mailed_check,
    encoded_customer_id
]

# Make prediction when button is clicked
if st.button("Predict"):
    try:
        # Ensure features are in the correct format (e.g., numeric)
        features = [int(x) if isinstance(x, str) and x.isdigit() else float(x) for x in features]

        # Make prediction
        prediction = model.predict([features])[0]

        # Display the result
        output = 'Yes' if prediction == 1 else 'No'
        st.write(f'Will the customer churn? {output}')
    except Exception as e:
        st.write(f"An error occurred: {e}")
