
import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.markdown("### Step 1: Data Ingestion & Overview")

    st.markdown("""

As a **Risk Manager** at a leading financial institution, your critical role is to ensure the integrity, fairness, and compliance of machine learning models used in sensitive areas like loan underwriting. Automated decisions, while efficient, carry inherent risks, including potential biases, lack of transparency, and non-compliance with regulatory standards. Your mission in this lab is to conduct a thorough **data provenance and risk audit** of an ML loan underwriting model.

This application will guide you step-by-step through an end-to-end narrative, allowing you to:

1.  **Ingest and Understand Data**: Begin by examining the raw loan application data, understanding its initial state, and identifying potential areas of concern.
2.  **Manage Data Provenance**: Document and trace the lineage of data to ensure its reliability and accountability throughout the model lifecycle.
3.  **Audit Data Quality**: Identify and address issues like missing values and outliers that can compromise model performance and fairness.
4.  **Perform Data Cleaning and Preprocessing**: Apply transformations and cleaning strategies to prepare data for model training, ensuring it meets quality standards.
5.  **Detect and Analyze Bias**: Uncover and quantify potential biases in the data that could lead to unfair lending decisions, focusing on demographic parity.
6.  **Simulate Risk and Implement Human Oversight**: Evaluate model robustness under uncertainty and identify scenarios requiring human intervention.
7.  **Establish Risk Register & Governance**: Log identified risks and propose mitigation strategies to maintain model accountability.
8.  **Generate an Audit Report**: Compile all findings, analyses, and recommendations into a comprehensive report for stakeholders and regulatory bodies.

Your journey through these stages will build a robust assurance case, evidencing the model's trustworthiness, compliance, and fairness, ultimately mitigating model risk for the institution.
""")

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
            missing_indices = np.random.choice(
                df.index, int(num_records * 0.05), replace=False)
            df.loc[missing_indices, col] = np.nan

        st.session_state.raw_data = df.copy()

    st.markdown("#### Raw Loan Application Data Sample")
    st.dataframe(st.session_state.raw_data.head())

    st.markdown("#### Dataset Summary Statistics")
    st.write(st.session_state.raw_data.describe(include='all'))

    st.markdown("#### Missing Values Overview")
    missing_data = st.session_state.raw_data.isnull().sum().to_frame(name="Missing Count")
    missing_data["Missing Percentage"] = (
        missing_data["Missing Count"] / len(st.session_state.raw_data)) * 100
    st.dataframe(missing_data[missing_data["Missing Count"] > 0].sort_values(
        by="Missing Percentage", ascending=False))

    st.markdown("""
    --- 
    **Risk Manager's Action:** You have now reviewed the initial state of the data. Notice the presence of missing values and various data types. This preliminary check helps you anticipate the next steps in data preparation and identify potential data quality risks.
    """)

    # Navigation to the next stage
    st.info("✅ Ready to move forward? Use the sidebar navigation to proceed to **Step 2: Data Provenance & Metadata Management**.", icon="ℹ️")
