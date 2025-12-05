
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.markdown("### Step 1: Data Ingestion & Overview")

    st.markdown("""
    **What you're doing:** As a Risk Manager, your first task is to get a foundational understanding of the raw loan application data. This involves reviewing its structure, content, and initial statistics to identify any immediate anomalies or areas that might require closer scrutiny during the audit process.

    **How this helps:** This initial data review is crucial for establishing the baseline for your audit. By understanding the raw state of the data, you can better track transformations, identify data quality issues, and ultimately build a robust case for model trustworthiness.

    **Underlying concept:** Data ingestion and initial exploration are fundamental steps in any data-driven workflow, providing the necessary context for subsequent analysis and model development. It ensures that the data being used is understood and relevant to the business problem.
    """)

    # Generate synthetic loan data
    if st.session_state.raw_data is None:
        num_records = 1000
        data = {
            "Loan_ID": [f"L{i:04d}" for i in range(num_records)],
            "Gender": np.random.choice(["Male", "Female"], num_records, p=[0.6, 0.4]),
            "Married": np.random.choice(["Yes", "No"], num_records, p=[0.7, 0.3]),
            "Dependents": np.random.choice(["0", "1", "2", "3+"], num_records, p=[0.5, 0.2, 0.15, 0.15]),
            "Education": np.random.choice(["Graduate", "Not Graduate"], num_records, p=[0.75, 0.25]),
            "Self_Employed": np.random.choice(["Yes", "No"], num_records, p=[0.15, 0.85]),
            "ApplicantIncome": np.random.randint(1500, 7000, num_records),
            "CoapplicantIncome": np.random.randint(0, 3000, num_records),
            "LoanAmount": np.random.randint(90, 700, num_records),
            "Loan_Amount_Term": np.random.choice([12, 36, 60, 120, 180, 240, 360, 480], num_records, p=[0.01, 0.02, 0.02, 0.05, 0.1, 0.08, 0.6, 0.12]),
            "Credit_History": np.random.choice([0.0, 1.0, np.nan], num_records, p=[0.1, 0.8, 0.1]),
            "Property_Area": np.random.choice(["Urban", "Semiurban", "Rural"], num_records, p=[0.35, 0.35, 0.3]),
            "Loan_Status": np.random.choice(["Y", "N"], num_records, p=[0.7, 0.3]),
        }

        df = pd.DataFrame(data)
        # Introduce some missing values intentionally for demonstration
        for col in ["Gender", "Married", "Dependents", "Self_Employed", "LoanAmount", "Credit_History"]:
            missing_indices = np.random.choice(df.index, int(num_records * 0.05), replace=False)
            df.loc[missing_indices, col] = np.nan

        st.session_state.raw_data = df.copy()

    st.markdown("#### Raw Loan Application Data Sample")
    st.dataframe(st.session_state.raw_data.head())

    st.markdown("#### Dataset Summary Statistics")
    st.write(st.session_state.raw_data.describe(include='all'))

    st.markdown("#### Missing Values Overview")
    missing_data = st.session_state.raw_data.isnull().sum().to_frame(name="Missing Count")
    missing_data["Missing Percentage"] = (missing_data["Missing Count"] / len(st.session_state.raw_data)) * 100
    st.dataframe(missing_data[missing_data["Missing Count"] > 0].sort_values(by="Missing Percentage", ascending=False))

    st.markdown("""
    --- 
    **Risk Manager's Action:** You have now reviewed the initial state of the data. Notice the presence of missing values and various data types. This preliminary check helps you anticipate the next steps in data preparation and identify potential data quality risks.
    """)

    # Navigation to the next stage
    if st.button("Proceed to Data Provenance & Metadata Management"):
        st.session_state.current_page = "2. Data Provenance & Metadata Management"
        st.rerun()
