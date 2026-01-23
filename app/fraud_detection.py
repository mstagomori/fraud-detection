import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/fraud_detection_pipeline.pkl')

st.title("Fraud detection App")
st.markdown("This app detects fraudulent transactions. Fill the details below and click Predict.")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=5000.0, step=100.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=4000.0, step=100.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0, step=100.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=1000.0, step=100.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)

    st.subheader(f"Prediction Result: '{int(prediction[0])}'" )

    if prediction[0] == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")