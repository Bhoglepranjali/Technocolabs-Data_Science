import pickle
import numpy as np
import streamlit as st

# Loading the saved Model
model = pickle.load(open('card_model.pkl', 'rb'))

st.title("Simple Credit Card Fraud Detection App")

st.write(""""

    This app predicts the **Fraud Credit Card!**
    """)
st.sidebar.header('User input Features')


def predict_default(features):
    features = np.array(features).astype(np.float64).reshape(1, -1)

    prediction = model.predict(features)
    probability = model.predict_proba(features)
    return prediction, probability


def main():
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">CREDIT CARD DEFAULT PREDICTION</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    LIMIT_BAL = st.sidebar.text_input("Limited Balance (in New Taiwanese (NT) dollar)")
    education_status = ["graduate school", "university", "high school", "others"]
    marital_status = ["Married", "single", "others"]

    payment_status = [
        "account started that month with a zero balance, and never used any credit",
        "account had a balance that was paid in full",
        "at least the minimum payment was made, but the entire balance wasn't paid",
        "payment delay for 1 month",
        "payment delay for 2 month",
        "payment delay for 3 month",
        "payment delay for 4 month",
        "payment delay for 5 month",
        "payment delay for 6 month",
        "payment delay for 7 month",
        "payment delay for 8 month",
    ]

    EDUCATION = education_status.index(st.sidebar.selectbox(
        "Select Education",
        tuple(education_status)
    )) +1

    MARRIAGE = marital_status.index(st.sidebar.selectbox(
        "Marital Status",
        tuple(marital_status)
    )) + 1

    AGE = st.sidebar.text_input("Age (in Years)")

    PAY_1 = payment_status.index(st.selectbox(
        "Last Month Payment Status",
        tuple(payment_status)
    )) - 2

    BILL_AMT1 = st.text_input("Last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT2 = st.text_input("Last 2nd month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT3 = st.text_input("Last 3rd month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT4 = st.text_input("Last 4th month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT5 = st.text_input("Last 5th month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT6 = st.text_input("Last 6th month Bill Amount (in New Taiwanese (NT) dollar)")

    PAY_AMT1 = st.text_input("Amount paid in Last Month (in New Taiwanese (NT) dollar)")
    PAY_AMT2 = st.text_input("Amount paid in Last 2nd Month (in New Taiwanese (NT) dollar)")
    PAY_AMT3 = st.text_input("Amount paid in Last 3rd Month (in New Taiwanese (NT) dollar)")
    PAY_AMT4 = st.text_input("Amount paid in Last 4th Month (in New Taiwanese (NT) dollar)")
    PAY_AMT5 = st.text_input("Amount paid in Last 5th Month (in New Taiwanese (NT) dollar)")
    PAY_AMT6 = st.text_input("Amount paid in Last 6th Month (in New Taiwanese (NT) dollar)")

    if st.button('predict'):

        features = [LIMIT_BAL, EDUCATION, MARRIAGE, AGE, PAY_1, BILL_AMT1, BILL_AMT2 ,BILL_AMT3, BILL_AMT4, BILL_AMT5,
                    BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]
        prediction, probability = predict_default(features)

        # print(prediction)
        # print(probability[:,1][0])

        if prediction[0] == 1:

                # counselling_html = """
                #     <div style = "background-color: #f8d7da; font-weight:bold;padding:10px;border-radius:7px;">
                #         <p style = 'color: #721c24;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
                #     </div>
                # """
                # st.markdown(counselling_html, unsafe_allow_html=True
            st.success("This account will be defaulted with a probability of {}%.".format(round(np.max(probability) * 100, 2)))
        else:
            st.success("This account will be Not defaulted with a probability of {}%.".format(round(np.max(probability) * 100, 2)))


if __name__ == '__main__':
    main()













































