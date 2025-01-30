# Customer Churn Prediction Model Deployment

## Overview

This repository contains a Customer Churn Prediction model built using the Random Forest algorithm. The model is designed to predict whether a customer will churn or not.

## Contents

### Model

- **Customer Churn Prediction Model:**
  - Implemented using the Random Forest algorithm.

### Deployment Scripts

The repository includes two files for deploying the model:

1. **Flask Deployment:**
   - **File:** `app.py`
   - **Description:** A Flask application for deploying the model.
   - **Instructions:** 
     1. Open your command prompt or terminal.
     2. Navigate to the directory containing `app.py`.
     3. Run the following command to start the Flask server:
        ```bash
        python app.py
        ```
     4. Open your web browser and go to `http://localhost:5000` to view the model in action.

2. **Streamlit Deployment:**
   - **File:** `Streamlit_app.py`
   - **Description:** A Streamlit application for deploying the model.
   - **Instructions:** 
     1. Open your command prompt or terminal.
     2. Navigate to the directory containing `Streamlit_app.py`.
     3. Run the following command to start the Streamlit app:
        ```bash
        streamlit run Streamlit_app.py
        ```
     4. A new browser window will open, or you can navigate to `http://localhost:8501` to view the Streamlit app.

**Check out the live demo and see how it works!** [Live Demo](https://deploy-6myk3saaabd7p9tgag5fw8.streamlit.app/)

## Getting Started

1. **Ensure you have the required dependencies installed.**
   - You can install them using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the desired deployment script:**
   - For Flask: `python app.py`
   - For Streamlit: `streamlit run Streamlit_app.py`

3. **Access the deployed model:**
   - Flask: `http://localhost:5000`
   - Streamlit: `http://localhost:8501`

## Contributing

Feel free to fork the repository and make improvements. If you have any suggestions or issues, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
