
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def generate_mock_risk_score(df):
    """Generates a mock risk score (probability of default) for each loan application."""
    # Simple logic: higher risk for poor credit history, lower income relative to loan amount, etc.
    risk_score = pd.Series(0.0, index=df.index)

    # Factor 1: Credit History (most significant)
    # Lower credit history -> higher risk
    risk_score = risk_score + (1 - df["Credit_History"].fillna(0.5)) * 0.4

    # Factor 2: Income to Loan Amount Ratio
    # Avoid division by zero for LoanAmount, replace with a small epsilon or 1 for safety
    loan_to_income_ratio = df["LoanAmount"] / \
        (df["ApplicantIncome"] + df["CoapplicantIncome"] + 1e-6)
    # Higher ratio -> higher risk, capped
    risk_score = risk_score + np.clip(loan_to_income_ratio * 0.1, 0, 0.3)

    # Factor 3: Education
    risk_score = risk_score + \
        df["Education"].apply(lambda x: 0.05 if x == "Not Graduate" else 0.0)

    # Factor 4: Dependents
    # More dependents -> slightly higher risk
    risk_score = risk_score + \
        df["Dependents"].replace({"3+": "3"}).astype(float) * 0.02

    # Ensure risk score is between 0 and 1
    risk_score = np.clip(risk_score, 0.0, 1.0)

    return risk_score


def main():
    st.markdown("### Step 6: Risk Simulation & Human Oversight")

    st.markdown("""
    **What you're doing:** As a Risk Manager, you need to assess how robust the model's decisions are under various conditions, especially when there's uncertainty in the input data. This involves simulating potential data fluctuations or errors and observing their impact on loan underwriting outcomes. Crucially, you'll define criteria for flagging cases that require human review, ensuring critical decisions benefit from expert judgment.

    **How this helps:** Risk simulation helps identify scenarios where the model might be vulnerable or make unreliable predictions. By setting up clear human oversight thresholds, you establish a safety net, ensuring that high-stakes decisions are not solely automated and adhere to the institution's risk appetite and ethical guidelines. This proactive approach prevents erroneous decisions and reinforces responsible AI deployment.

    **Underlying concept:** Risk simulation uses techniques like Monte Carlo methods (though simplified here) to model the impact of input variable uncertainty on model outputs. Human oversight integrates expert judgment into automated workflows, typically by setting thresholds (e.g., a "probability of default" score) that trigger manual review for cases falling into critical or ambiguous zones. This balances automation efficiency with human accountability.
    """)

    if st.session_state.cleaned_data is None:
        st.warning(
            "No cleaned data available. Please go to 'Data Cleaning and Preprocessing' to prepare the data.")
        if st.button("Go to Data Cleaning and Preprocessing"):
            st.session_state.current_page = "4. Data Cleaning and Preprocessing"
            st.rerun()
        return

    df_cleaned = st.session_state.cleaned_data.copy()

    st.markdown("#### Configure Simulation Parameters")
    st.markdown("""
    **Risk Manager's Action:** Adjust the sliders below to introduce hypothetical uncertainty into key financial features. Consider scenarios where applicants might slightly misreport income or loan amounts are estimated with a margin of error. Also, set the threshold for what constitutes a "high-risk" loan requiring your personal review.
    """)

    col1, col2 = st.columns(2)

    with col1:
        income_uncertainty_percent = st.slider(
            "Applicant Income Uncertainty (+/- %):",
            min_value=0, max_value=20, value=5, step=1,
            help="Simulate slight fluctuations or errors in reported applicant income."
        )
    with col2:
        loan_amount_uncertainty_percent = st.slider(
            "Loan Amount Uncertainty (+/- %):",
            min_value=0, max_value=20, value=5, step=1,
            help="Simulate slight fluctuations or errors in loan amount requests."
        )

    # Add a mock credit history noise parameter
    credit_history_noise_level = st.slider(
        "Credit History Data Noise (Probability of Falsification/Error):",
        min_value=0.0, max_value=0.1, value=0.01, step=0.005,
        help="Simulate a small probability of error or deliberate falsification in credit history reports."
    )

    st.markdown("#### Human Oversight Thresholds")
    human_review_threshold = st.slider(
        "Probability of Default Threshold for Human Review:",
        min_value=0.0, max_value=1.0, value=0.6, step=0.05,
        help="Loans with a simulated probability of default above this threshold will be flagged for human review."
    )
    st.markdown(r"""
    The **Probability of Default (PD)** threshold for human review, denoted as $T_{HR}$, is a critical governance parameter. If a loan application's simulated risk score (PD) exceeds this threshold, i.e., $PD_{simulated} > T_{HR}$, it automatically triggers a manual review by a human expert. This ensures that high-risk cases, or those with uncertain outcomes, are subjected to closer scrutiny, mitigating potential financial losses and reputational damage. For instance, if $T_{HR} = 0.6$, any loan with a $PD_{simulated}$ greater than $0.6$ is flagged.
    """)

    if st.button("Run Risk Simulation"):
        simulated_df = df_cleaned.copy()

        # Introduce uncertainty into numerical features
        simulated_df["ApplicantIncome"] = simulated_df["ApplicantIncome"] * \
            (1 + np.random.uniform(-income_uncertainty_percent/100,
             income_uncertainty_percent/100, len(simulated_df)))
        simulated_df["LoanAmount"] = simulated_df["LoanAmount"] * (1 + np.random.uniform(
            -loan_amount_uncertainty_percent/100, loan_amount_uncertainty_percent/100, len(simulated_df)))

        # Introduce noise into Credit_History
        if "Credit_History" in simulated_df.columns:
            noise_mask = np.random.rand(
                len(simulated_df)) < credit_history_noise_level
            # Flip 0 to 1, or 1 to 0 for noise. Handle NaN by keeping them NaN or defaulting.
            simulated_df.loc[noise_mask & (
                simulated_df["Credit_History"] == 0.0), "Credit_History"] = 1.0
            simulated_df.loc[noise_mask & (
                simulated_df["Credit_History"] == 1.0), "Credit_History"] = 0.0
            # If Credit_History was NaN and noise_mask is True, it remains NaN here, which is fine.

        # Generate mock risk scores based on the (potentially perturbed) data
        simulated_df["Simulated_Risk_Score"] = generate_mock_risk_score(
            simulated_df)

        # Determine loan status based on a simple threshold for demonstration
        # For simplicity, let's say a low risk score leads to "Y" (Approved), high to "N" (Rejected)
        # This is a mock decision for the purpose of flagging, not a real model prediction.
        simulated_df["Mock_Loan_Status_Predicted"] = np.where(
            simulated_df["Simulated_Risk_Score"] < 0.5, "Y", "N"
        )

        # Flag for human review based on the defined threshold
        simulated_df["Flagged_for_Human_Review"] = np.where(
            simulated_df["Simulated_Risk_Score"] > human_review_threshold, "Yes", "No"
        )

        st.session_state.simulated_results = simulated_df
        st.success("Risk simulation completed successfully!")

        # Update provenance logs for simulation
        new_log_entry = {
            "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Action": "Risk Simulation Executed",
            "Description": f"Simulated with Income Uncertainty: {income_uncertainty_percent}%, Loan Amount Uncertainty: {loan_amount_uncertainty_percent}%, Credit History Noise: {credit_history_noise_level*100}%, Human Review Threshold: {human_review_threshold}",
            "User": "Risk_Manager_001"
        }
        st.session_state.provenance_logs = pd.concat(
            [st.session_state.provenance_logs, pd.DataFrame([new_log_entry])],
            ignore_index=True
        )

    if "simulated_results" in st.session_state and st.session_state.simulated_results is not None:
        st.markdown("#### Simulation Results Overview")
        st.markdown("""
        **Risk Manager's Insight:** Review the impact of the simulated uncertainty on the predicted outcomes and, more importantly, the number of cases flagged for human review. This shows you where the model's automation might need human intervention due to increased risk or uncertainty.
        """)

        # Display counts of flagged cases
        flagged_counts = st.session_state.simulated_results["Flagged_for_Human_Review"].value_counts(
        ).to_frame()
        st.dataframe(flagged_counts.rename(
            columns={"count": "Number of Applications"}))

        fig_flagged, ax_flagged = plt.subplots(figsize=(8, 5))
        sns.countplot(x="Flagged_for_Human_Review",
                      data=st.session_state.simulated_results, palette="coolwarm", ax=ax_flagged)
        ax_flagged.set_title("Applications Flagged for Human Review")
        ax_flagged.set_xlabel("Flagged for Human Review")
        ax_flagged.set_ylabel("Number of Applications")
        st.pyplot(fig_flagged)
        st.markdown(r"""
        The bar chart illustrates the distribution of loan applications that require human review based on the set **Probability of Default Threshold** ($T_{HR}$). A higher number of flagged cases might indicate either an overly conservative threshold or a genuinely higher-risk portfolio under the simulated conditions. This visualization immediately tells the Risk Manager how much manual effort might be required to process the loan applications, highlighting operational risk.
        """)

        st.markdown("#### Sample of Applications Flagged for Human Review")
        flagged_applications = st.session_state.simulated_results[
            st.session_state.simulated_results["Flagged_for_Human_Review"] == "Yes"
        ].head(10)

        if not flagged_applications.empty:
            st.dataframe(flagged_applications[[
                "Loan_ID", "ApplicantIncome", "LoanAmount", "Credit_History",
                "Simulated_Risk_Score", "Mock_Loan_Status_Predicted", "Flagged_for_Human_Review"
            ]].sort_values(by="Simulated_Risk_Score", ascending=False))
            st.markdown("""
            These are example cases that, under the simulated conditions and given your defined human review threshold, have been flagged for your personal oversight. For each of these, you would typically delve deeper into the applicant's full profile to make a final, informed decision.
            """)
        else:
            st.info(
                "No applications were flagged for human review under the current simulation parameters and threshold.")

        st.markdown("""
        --- 
        **Risk Manager's Action:** You have successfully simulated risk and identified cases requiring human oversight. This process validates the model's behavior under stress and reinforces the importance of human-in-the-loop decision-making for high-risk scenarios. This forms a crucial part of your assurance case.
        """)

    st.info("✅ Ready to move forward? Use the sidebar navigation to proceed to **Step 7: Risk Register & Governance**.", icon="ℹ️")
