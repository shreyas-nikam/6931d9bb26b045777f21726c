
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: ML Model Risk Auditing")
st.divider()

st.markdown("""
### Welcome, Risk Manager!

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

# Initialize session state for data if not already present
if "raw_data" not in st.session_state:
    st.session_state.raw_data = None
if "cleaned_data" not in st.session_state:
    st.session_state.cleaned_data = None
if "metadata" not in st.session_state:
    st.session_state.metadata = pd.DataFrame(
        columns=["Attribute", "Description", "Source", "Last Updated", "Provenance Log"]
    )
if "provenance_logs" not in st.session_state:
    st.session_state.provenance_logs = pd.DataFrame(
        columns=["Timestamp", "Action", "Description", "User"]
    )
if "bias_metrics" not in st.session_state:
    st.session_state.bias_metrics = None


page = st.sidebar.selectbox(
    label="Navigation",
    options=[
        "1. Data Ingestion & Overview",
        "2. Data Provenance & Metadata Management",
        "3. Data Quality Audits",
        "4. Data Cleaning and Preprocessing",
        "5. Bias Detection & Analysis",
        "6. Risk Simulation & Human Oversight",
        "7. Risk Register & Governance",
        "8. Audit Report & Insights"
    ]
)

if page == "1. Data Ingestion & Overview":
    from application_pages.page_1_data_ingestion import main
    main()
elif page == "2. Data Provenance & Metadata Management":
    from application_pages.page_2_data_provenance import main
    main()
elif page == "3. Data Quality Audits":
    from application_pages.page_3_data_quality_audits import main
    main()
elif page == "4. Data Cleaning and Preprocessing":
    from application_pages.page_4_data_cleaning import main
    main()
elif page == "5. Bias Detection & Analysis":
    from application_pages.page_5_bias_detection import main
    main()
elif page == "6. Risk Simulation & Human Oversight":
    from application_pages.page_6_risk_simulation import main
    main()
elif page == "7. Risk Register & Governance":
    from application_pages.page_7_risk_register import main
    main()
elif page == "8. Audit Report & Insights":
    from application_pages.page_8_audit_report import main
    main()
