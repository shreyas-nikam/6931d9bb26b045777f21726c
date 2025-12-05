
import streamlit as st
import pandas as pd
import datetime
import io

def main():
    st.markdown("### Step 8: Audit Report & Insights")

    st.markdown("""
    **What you're doing:** As a Risk Manager, you've meticulously worked through the data provenance, quality, bias detection, and risk simulation stages. Now, your final task is to compile all these findings into a comprehensive audit report. This report serves as a definitive assurance case, documenting the model's trustworthiness, compliance, and fairness for both internal stakeholders and regulatory bodies.

    **How this helps:** The audit report is the culmination of your entire risk management process. It provides a clear, defensible summary of the model's adherence to standards, the risks identified, and the mitigation strategies proposed. This document is crucial for regulatory compliance, internal governance, and fostering trust in the automated decision-making system.

    **Underlying concept:** An audit report formally communicates the results of an audit, including findings, conclusions, and recommendations. In the context of ML model risk, it synthesizes technical analyses into a business-relevant narrative, providing transparency and accountability for the model's lifecycle management. It acts as a formal record, supporting the overall model governance framework.
    """)

    st.markdown("#### Comprehensive Model Audit Report Summary")
    st.markdown("""
    **Risk Manager's Action:** Review the automatically generated summary of the audit findings. This consolidates all your decisions and observations from the previous steps, providing a holistic view of the model's risk profile and the actions taken.
    """)

    report_content = io.StringIO()
    report_content.write(f"--- Model Risk Audit Report ---\n")
    report_content.write(f"Date Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
    report_content.write(f"Auditor: Risk_Manager_001\n\n")
    report_content.write(f"## 1. Data Ingestion & Overview\n")
    if st.session_state.raw_data is not None:
        report_content.write(f"  - Initial dataset loaded with {len(st.session_state.raw_data)} records and {len(st.session_state.raw_data.columns)} features.\n")
        report_content.write(f"  - Key features include: {", ".join(st.session_state.raw_data.columns.tolist())}.\n")
        missing_initial = st.session_state.raw_data.isnull().sum().sum()
        if missing_initial > 0:
            report_content.write(f"  - Initial data scan revealed {missing_initial} missing values across features.\n")
        else:
            report_content.write(f"  - No missing values were detected in the initial data scan.\n")
    else:
        report_content.write("  - No raw data was loaded during the audit process.\n")

    report_content.write(f"\n## 2. Data Provenance & Metadata Management\n")
    if not st.session_state.provenance_logs.empty:
        report_content.write(f"  - {len(st.session_state.provenance_logs)} provenance log entries recorded.\n")
        report_content.write(f"  - Last recorded action: {st.session_state.provenance_logs.iloc[-1]["Description"]} by {st.session_state.provenance_logs.iloc[-1]["User"]} on {st.session_state.provenance_logs.iloc[-1]["Timestamp"]}.\n")
    else:
        report_content.write("  - No provenance logs were documented.\n")

    report_content.write(f"\n## 3. Data Quality Audits\n")
    if st.session_state.raw_data is not None:
        missing_after_cleaning_check = st.session_state.cleaned_data.isnull().sum().sum() if st.session_state.cleaned_data is not None else st.session_state.raw_data.isnull().sum().sum()
        if missing_after_cleaning_check == 0 and st.session_state.raw_data.isnull().sum().sum() > 0:
            report_content.write("  - Missing values were successfully addressed during data cleaning.\n")
        elif missing_after_cleaning_check > 0 and st.session_state.raw_data.isnull().sum().sum() > 0:
            report_content.write(f"  - Some missing values still remain after cleaning ({missing_after_cleaning_check} total).\n")
        else:
            report_content.write("  - No significant missing data issues or they were fully resolved.\n")

        # Outlier summary (simple check)
        numerical_cols = st.session_state.raw_data.select_dtypes(include=np.number).columns.tolist()
        outliers_detected = False
        for col in numerical_cols:
            if col in st.session_state.raw_data.columns and not st.session_state.raw_data[col].empty:
                Q1 = st.session_state.raw_data[col].quantile(0.25)
                Q3 = st.session_state.raw_data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                if ((st.session_state.raw_data[col] < lower_bound) | (st.session_state.raw_data[col] > upper_bound)).any():
                    outliers_detected = True
                    break
        if outliers_detected:
            report_content.write("  - Outliers were identified in several numerical features, prompting cleaning actions.\n")
        else:
            report_content.write("  - No significant outliers were detected or they were effectively handled.\n")
    else:
        report_content.write("  - Data quality audits could not be performed due to absence of data.\n")

    report_content.write(f"\n## 4. Data Cleaning and Preprocessing\n")
    if st.session_state.cleaned_data is not None:
        report_content.write(f"  - Data was cleaned and preprocessed, resulting in {len(st.session_state.cleaned_data)} records.\n")
        # Add more details based on actual cleaning steps if possible from session state
        report_content.write("  - Missing values were imputed (strategies varied per feature) and outliers were addressed (e.g., capped or removed).\n")
    else:
        report_content.write("  - Data cleaning and preprocessing were not performed.\n")

    report_content.write(f"\n## 5. Bias Detection & Analysis\n")
    if st.session_state.bias_metrics is not None:
        report_content.write("  - Bias detection performed, focusing on demographic parity and distribution checks.\n")
        for group, metrics in st.session_state.bias_metrics.items():
            report_content.write(f"  - For sensitive attribute '{group}':\n")
            for metric_name, value in metrics.items():
                report_content.write(f"    - {metric_name}: {value:.4f}\n")
        report_content.write("  - Identified potential disparities in loan approval rates across demographic groups, suggesting areas for bias mitigation.\n")
    else:
        report_content.write("  - Bias detection and analysis were not performed or completed.\n")

    report_content.write(f"\n## 6. Risk Simulation & Human Oversight\n")
    if "simulated_results" in st.session_state and st.session_state.simulated_results is not None:
        flagged_count = st.session_state.simulated_results["Flagged_for_Human_Review"].value_counts().get("Yes", 0)
        total_simulated = len(st.session_state.simulated_results)
        review_threshold_used = st.session_state.get("human_review_threshold", "N/A")

        report_content.write(f"  - Risk simulation conducted on {total_simulated} applications.\n")
        report_content.write(f"  - {flagged_count} applications ({flagged_count/total_simulated:.2%}) were flagged for human review based on a Probability of Default threshold of {review_threshold_used}.\n")
        report_content.write("  - This process demonstrated the model's behavior under uncertainty and highlighted the need for human-in-the-loop interventions for high-risk cases.\n")
    else:
        report_content.write("  - Risk simulation was not performed.\n")

    report_content.write(f"\n## 7. Risk Register & Governance\n")
    if not st.session_state.risk_register.empty:
        report_content.write(f"  - {len(st.session_state.risk_register)} risks are currently documented in the Risk Register.\n")
        open_risks = st.session_state.risk_register[st.session_state.risk_register["Status"] == "Open"]
        if not open_risks.empty:
            report_content.write(f"  - {len(open_risks)} risks are currently open and require ongoing monitoring or mitigation.\n")
            report_content.write("  - High-scoring risks identified include: ") 
            high_risk_entries = open_risks[open_risks["Risk Score"] >= 6] # Example for high score
            if not high_risk_entries.empty:
                report_content.write(f"{", ".join(high_risk_entries["Risk Name"].tolist())}.\n")
            else:
                report_content.write("No high-scoring open risks.\n")
        else:
            report_content.write("  - All identified risks are currently closed or in progress.\n")
    else:
        report_content.write("  - The model risk register has no documented entries.\n")

    report_content.write(f"\n## 8. Final Narrative & Conclusion\n")
    report_content.write("""
    The comprehensive audit of the ML loan underwriting model has successfully traced data provenance, assessed data quality, identified potential biases, and simulated model behavior under uncertainty. The findings, documented in the Risk Register, provide a clear path for ongoing model governance and risk mitigation. This process has reinforced the importance of continuous monitoring and human oversight to ensure the model remains trustworthy, compliant, and fair in its automated lending decisions. The institution is now better equipped to manage the risks associated with AI deployment and maintain a strong assurance case.
    \n""")
    
    st.download_button(
        label="Download Full Audit Report (Text)",
        data=report_content.getvalue(),
        file_name=f"ML_Loan_Underwriting_Audit_Report_{datetime.date.today().strftime("%Y%m%d")}.txt",
        mime="text/plain"
    )

    st.markdown("""
    --- 
    **Risk Manager's Final Reflection:** You have successfully completed a full audit cycle for the ML loan underwriting model. The generated report is your testament to ensuring responsible AI. This rigorous process not only highlights areas for improvement but also provides the necessary evidence for regulatory compliance and stakeholder confidence.
    """)

    st.markdown("### Next Steps for Governance:")
    st.markdown("""
    -   **Regular Review:** Schedule periodic audits to reassess data quality, model performance, and bias metrics.
    -   **Mitigation Tracking:** Continuously monitor the status of risks in the Risk Register and the effectiveness of implemented mitigation strategies.
    -   **Policy Updates:** Propose updates to internal policies and procedures based on audit findings to strengthen model governance.
    """)
