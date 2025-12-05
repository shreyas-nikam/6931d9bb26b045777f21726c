
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
        risk_name = st.text_input("Risk Name (e.g., 'Gender Bias in Loan Approval'):")
        category = st.selectbox(
            "Category:",
            options=["Data Quality", "Bias", "Model Performance", "Compliance", "Operational"],
            index=0,
            key="risk_category"
        )
        description = st.text_area("Description of the Risk:")
        likelihood = st.selectbox(
            "Likelihood:",
            options=["Low", "Medium", "High"],
            index=0,
            key="risk_likelihood"
        )
        impact = st.selectbox(
            "Impact:",
            options=["Low", "Medium", "High"],
            index=0,
            key="risk_impact"
        )
        mitigation_strategy = st.text_area("Proposed Mitigation Strategy:")
        status = st.selectbox(
            "Status:",
            options=["Open", "In Progress", "Closed"],
            index=0,
            key="risk_status"
        )
        owner = st.text_input("Owner (e.g., 'Head of Model Risk'):", value="Risk_Manager_001")

        submitted = st.form_submit_button("Add Risk to Register")
        if submitted:
            if risk_name and description and mitigation_strategy:
                # Map likelihood and impact to numerical values for score calculation
                likelihood_map = {"Low": 1, "Medium": 2, "High": 3}
                impact_map = {"Low": 1, "Medium": 2, "High": 3}
                
                risk_score = likelihood_map[likelihood] * impact_map[impact]

                new_risk_entry = {
                    "Risk ID": risk_id,
                    "Risk Name": risk_name,
                    "Category": category,
                    "Description": description,
                    "Likelihood": likelihood,
                    "Impact": impact,
                    "Risk Score": risk_score,
                    "Mitigation Strategy": mitigation_strategy,
                    "Status": status,
                    "Owner": owner,
                    "Date Identified": datetime.datetime.now().strftime("%Y-%m-%d")
                }
                st.session_state.risk_register = pd.concat(
                    [st.session_state.risk_register, pd.DataFrame([new_risk_entry])],
                    ignore_index=True
                )
                st.success(f"Risk '{risk_name}' added to the register with Risk Score: {risk_score}!")
                st.dataframe(st.session_state.risk_register)

                # Update provenance logs
                new_log_entry = {
                    "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Action": "Risk Register Update",
                    "Description": f"Added risk '{risk_name}' (ID: {risk_id}) with score {risk_score}.",
                    "User": "Risk_Manager_001"
                }
                st.session_state.provenance_logs = pd.concat(
                    [st.session_state.provenance_logs, pd.DataFrame([new_log_entry])],
                    ignore_index=True
                )
            else:
                st.warning("Please fill in all required fields (Risk Name, Description, Mitigation Strategy).")

    st.markdown("""
    --- 
    **Risk Manager's Insight:** By maintaining a detailed risk register, you're not just identifying problems; you're actively contributing to the institution's robust model governance framework. This documentation is crucial for internal reviews and external regulatory compliance, demonstrating a proactive approach to managing AI-related risks.
    """)

    if st.button("Proceed to Audit Report & Insights"):
        st.session_state.current_page = "8. Audit Report & Insights"
        st.rerun()
