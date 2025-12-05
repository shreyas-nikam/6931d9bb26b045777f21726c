
import streamlit as st
import pandas as pd
import datetime

def main():
    st.markdown("### Step 7: Risk Register & Governance")

    st.markdown("""
    **What you're doing:** As a Risk Manager, after identifying potential biases and simulating various risk scenarios, it's crucial to formally document these risks, assess their severity, and propose concrete mitigation strategies. This step involves updating the institutional **Risk Register**, a central repository for tracking and managing all identified risks related to the ML model. This ensures a transparent and accountable governance framework.

    **How this helps:** A well-maintained risk register provides a comprehensive overview of all model-related risks, their potential impact, and the planned actions to control them. This systematic approach allows for proactive risk management, facilitates compliance reporting, and informs strategic decisions to enhance model trustworthiness and reduce overall organizational exposure.

    **Underlying concept:** A risk register is a key tool in enterprise risk management, providing a structured way to identify, analyze, and monitor risks. Governance refers to the framework of rules, practices, and processes by which an organization is directed and controlled. For ML models, this includes establishing clear responsibilities, audit trails, and decision-making protocols to ensure ethical and compliant AI deployment.
    """)

    # Initialize risk_register in session_state if it doesn't exist
    if "risk_register" not in st.session_state:
        st.session_state.risk_register = pd.DataFrame(
            columns=[
                "Risk ID", "Risk Name", "Category", "Description",
                "Likelihood", "Impact", "Risk Score", "Mitigation Strategy",
                "Status", "Owner", "Date Identified"
            ]
        )

    st.markdown("#### Current Model Risk Register")
    st.markdown("""
    **Risk Manager's Action:** Review the existing entries in the risk register. These might include risks identified during data quality audits, bias detection, or the risk simulation phase. Your role is to ensure all relevant risks are captured and adequately assessed.
    """)

    if not st.session_state.risk_register.empty:
        st.dataframe(st.session_state.risk_register)
    else:
        st.info("The risk register is currently empty. Add new risk entries below.")

    st.markdown("#### Add New Risk Entry")
    st.markdown("""
    **Risk Manager's Action:** Use the form below to document any newly identified risks or to elaborate on existing ones. Be precise in your description, assign appropriate likelihood and impact, and propose clear, actionable mitigation strategies. This structured documentation is vital for governance and accountability.
    """)

    with st.form("new_risk_form"):
        risk_id = st.text_input("Risk ID:", value=f"MR_{len(st.session_state.risk_register) + 1:03d}")
        risk_name = st.text_input("Risk Name (e.g., 