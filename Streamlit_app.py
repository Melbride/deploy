import streamlit as st
import pickle

# Load the trained model
try:
    with open('churn.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'churn.pkl' is in the correct directory.")
    model = None
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    model = None

# Define feature names and encoding mappings
feature_names = [
    'Gender', 'Senior Citizen', 'Partner', 'Dependents',
    'Tenure', 'Phone Service', 'Online Security', 'Online Backup', 'Device Protection',
    'Tech Support', 'Streaming TV', 'Streaming Movies', 'Paperless Billing',
    'Monthly Charges', 'Total Charges', 'No Phone Service', 'Fiber Optic',
    'No Internet Service', 'Contract: One Year', 'Contract: Two Years', 'Payment Method: Credit Card',
    'Payment Method: Electronic Check', 'Payment Method: Mailed Check', 'Encoded Customer ID'
]

gender_map = {'Male': 0, 'Female': 1}
yes_no_map = {'Yes': 1, 'No': 0}
service_map = {'No Internet Service': 0, 'No': 1, 'Yes': 2}

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

# Prepare the feature vector with placeholders for missing features
features = [
    gender_map.get(gender, 0),  # Default value if key is not found
    senior_citizen,
    yes_no_map.get(partner, 0),
    yes_no_map.get(dependents, 0),
    tenure,
    yes_no_map.get(phone_service, 0),
    service_map.get(online_security, 0),
    service_map.get(online_backup, 0),
    service_map.get(device_protection, 0),
    service_map.get(tech_support, 0),
    service_map.get(streaming_tv, 0),
    service_map.get(streaming_movies, 0),
    yes_no_map.get(paperless_billing, 0),
    monthly_charges,
    total_charges,
    no_phone_service,
    fiber_optic,
    no_internet_service,
    contract_one_year,
    contract_two_years,
    payment_method_credit_card,
    payment_method_electronic_check,
    payment_method_mailed_check,
    encoded_customer_id
]

# Ensure the length of features matches the model expectation
expected_length = 26  # Update this if your model expects a different number
if len(features) < expected_length:
    features.extend([0] * (expected_length - len(features)))  # Add default values if needed

# Make prediction when button is clicked
if st.button("Predict"):
    if model is not None:
        try:
            # Make prediction
            prediction = model.predict([features])[0]

            # Display the result
            output = 'Yes' if prediction == 1 else 'No'
            st.write(f'Will the customer churn? {output}')
        except Exception as e:
            st.write(f"An error occurred during prediction: {e}")
    else:
        st.write("Model is not loaded. Please check the model file.")
