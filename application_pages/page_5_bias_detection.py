
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_demographic_parity(df, sensitive_attr, target_column, positive_outcome):
    """Calculate demographic parity metrics for a given sensitive attribute."""
    if sensitive_attr not in df.columns or target_column not in df.columns:
        return None

    # Filter out rows with missing values in sensitive_attr or target_column
    df_filtered = df[[sensitive_attr, target_column]].dropna()

    if df_filtered.empty:
        return None

    # Calculate approval rates for each group
    approval_rates = {}
    for group in df_filtered[sensitive_attr].unique():
        group_data = df_filtered[df_filtered[sensitive_attr] == group]
        approval_rate = (group_data[target_column] ==
                         positive_outcome).sum() / len(group_data)
        approval_rates[group] = approval_rate

    if len(approval_rates) < 2:
        return None

    # Calculate demographic parity difference
    dpd = max(approval_rates.values()) - min(approval_rates.values())

    return {
        "Approval Rates": approval_rates,
        "Demographic Parity Difference": dpd
    }


def main():
    st.markdown("### Step 5: Bias Detection & Analysis")

    st.markdown("""
    **What you're doing:** As a Risk Manager, a critical aspect of auditing ML models is to detect and analyze potential biases in the data. Biases can lead to unfair outcomes for certain demographic groups (e.g., based on gender, education, or other protected characteristics), leading to ethical and regulatory concerns. This step helps quantify these disparities.

    **How this helps:** Identifying data bias early allows for intervention strategies, such as re-sampling, re-weighting, or incorporating fairness constraints into model training. This ensures that the model operates equitably and complies with non-discrimination regulations, significantly reducing reputational and legal risks.

    **Underlying concept:** **Bias detection** in ML focuses on identifying systematic and unfair discrimination against certain groups. **Demographic parity** is a fairness metric that requires the probability of a positive outcome (e.g., loan approval) to be the same across different demographic groups. If $P(\\text{outcome}=Y | \\text{group}=A) \\approx P(\\text{outcome}=Y | \\text{group}=B)$, then demographic parity is satisfied. **Distributional analysis** compares feature distributions across groups to identify underlying disparities that might lead to bias.
    """)

    if st.session_state.cleaned_data is None:
        st.warning(
            "No cleaned data available. Please go to 'Data Cleaning and Preprocessing' to prepare the data.")
        if st.button("Go to Data Cleaning and Preprocessing"):
            st.session_state.current_page = "4. Data Cleaning and Preprocessing"
            st.rerun()
        return

    df_cleaned = st.session_state.cleaned_data.copy()

    st.markdown("#### Select Sensitive Attribute for Bias Analysis")
    st.markdown("""
    **Risk Manager's Action:** Choose a demographic or sensitive attribute (protected characteristic) to analyze for potential bias. This could be Gender, Education, or other categorical features that might be subject to discriminatory practices.
    """)

    # Identify categorical columns that could be sensitive attributes
    categorical_cols = df_cleaned.select_dtypes(
        include=["object", "category"]).columns.tolist()

    # Remove Loan_ID if present
    if "Loan_ID" in categorical_cols:
        categorical_cols.remove("Loan_ID")
    if "Loan_Status" in categorical_cols:
        categorical_cols.remove("Loan_Status")

    if not categorical_cols:
        st.error("No categorical features available for bias analysis.")
        return

    # Default to Gender if available, otherwise first categorical column
    default_sensitive_attr = "Gender" if "Gender" in categorical_cols else categorical_cols[0]
    default_index = categorical_cols.index(
        default_sensitive_attr) if default_sensitive_attr in categorical_cols else 0

    selected_sensitive_attr = st.selectbox(
        "Select Sensitive Attribute:",
        options=categorical_cols,
        index=default_index,
        key="sensitive_attr"
    )

    st.markdown(
        "#### Loan Approval Rates by Sensitive Attribute (Demographic Parity)")
    st.markdown("""
    **Risk Manager's Action:** Examine the approval rates across different groups of the selected sensitive attribute. Significant disparities might indicate potential bias that could be perpetuated by the model.
    """)

    # Target column and positive outcome
    target_column = "Loan_Status"
    positive_outcome = "Y"  # Assuming "Y" means approved

    if target_column not in df_cleaned.columns:
        st.error(
            f"Target column '{target_column}' not found in the cleaned data.")
        return

    bias_metrics_result = calculate_demographic_parity(
        df_cleaned, selected_sensitive_attr, target_column, positive_outcome)

    if bias_metrics_result is None:
        st.warning(
            f"Unable to calculate demographic parity for '{selected_sensitive_attr}'. Please check if the data contains valid values.")
    else:
        approval_rates = bias_metrics_result["Approval Rates"]
        dpd = bias_metrics_result["Demographic Parity Difference"]

        st.markdown(f"**Approval Rates by {selected_sensitive_attr}:**")
        st.dataframe(pd.DataFrame({"Approval Rate": approval_rates}).T)

        st.metric(
            label=f"Demographic Parity Difference (max_rate - min_rate) for '{selected_sensitive_attr}'",
            value=f"{dpd:.4f}",
            delta=None,
            delta_color="inverse"
        )

        st.markdown(r"""
        **Demographic parity** is achieved when the proportion of positive outcomes (e.g., loan approvals) is roughly equal across different groups of a sensitive attribute. The **Demographic Parity Difference** quantifies this:
        $$ DPD = \max_{g \in G} P(\text{Outcome}=Y| \text{Group}=g) - \min_{g \in G} P(\text{Outcome}=Y| \text{Group}=g) $$
        A DPD close to zero indicates better demographic parity. A large difference (e.g., greater than $0.1$) suggests a significant disparity that might indicate bias. For instance, if the approval rate for 'Male' applicants is $0.70$ and for 'Female' applicants is $0.55$, the DPD would be $0.15$, which is a notable disparity warranting further investigation.
        """)

        # Visualize approval rates
        fig_parity, ax_parity = plt.subplots(figsize=(10, 6))
        sns.barplot(x=list(approval_rates.keys()), y=list(
            approval_rates.values()), ax=ax_parity, palette="pastel")
        ax_parity.set_title(
            f"Loan Approval Rates by {selected_sensitive_attr}")
        ax_parity.set_xlabel(selected_sensitive_attr)
        ax_parity.set_ylabel("Approval Rate")
        ax_parity.set_ylim(0, 1)

        # Add value labels on bars
        for i, (group, rate) in enumerate(approval_rates.items()):
            ax_parity.text(
                i, rate + 0.02, f"{rate:.3f}", ha='center', va='bottom', fontsize=10)

        st.pyplot(fig_parity)
        plt.close(fig_parity)

        # Store bias metrics in session state
        if "bias_metrics" not in st.session_state:
            st.session_state.bias_metrics = {}

        st.session_state.bias_metrics[selected_sensitive_attr] = {
            "Approval Rates": approval_rates,
            "Demographic Parity Difference": dpd
        }

        # Update provenance logs
        import datetime
        new_log_entry = {
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Action": "Bias Detection & Analysis",
            "Description": f"Calculated demographic parity for '{selected_sensitive_attr}'. DPD: {dpd:.4f}",
            "User": "Risk_Manager_001"
        }
        st.session_state.provenance_logs = pd.concat(
            [st.session_state.provenance_logs, pd.DataFrame([new_log_entry])],
            ignore_index=True
        )

    st.markdown("#### Conditional Distribution of Key Numerical Features")
    st.markdown("""
    **Risk Manager's Action:** Analyze how numerical features (like income or loan amount) are distributed across different groups of the sensitive attribute. Disparities in these distributions can reveal underlying inequalities that the model might learn and perpetuate.
    """)

    # Identify numerical columns
    numerical_cols = df_cleaned.select_dtypes(
        include=np.number).columns.tolist()

    # Exclude Loan_ID if numeric
    if "Loan_ID" in numerical_cols:
        numerical_cols.remove("Loan_ID")

    # Exclude binary/categorical numerical features (Credit_History, etc.)
    # Keep only continuous numerical features with more than 10 unique values
    continuous_numerical_cols = []
    for col in numerical_cols:
        # More than 10 unique values suggests continuous data
        if df_cleaned[col].nunique() > 10:
            continuous_numerical_cols.append(col)

    numerical_cols = continuous_numerical_cols

    # Remove Loan_Amount from numerical features
    if "Loan_Status" in numerical_cols:
        numerical_cols.remove("Loan_Status")
    if "LoanAmount" in numerical_cols:
        numerical_cols.remove("LoanAmount")
    if "Loan_Amount" in numerical_cols:
        numerical_cols.remove("Loan_Amount")

    if numerical_cols:
        # Default to ApplicantIncome if available
        default_numerical_feature = "ApplicantIncome" if "ApplicantIncome" in numerical_cols else numerical_cols[
            0]
        default_num_index = numerical_cols.index(
            default_numerical_feature) if default_numerical_feature in numerical_cols else 0

        selected_numerical_feature = st.selectbox(
            "Select Numerical Feature to Analyze:",
            options=numerical_cols,
            index=default_num_index,
            key="numerical_feature"
        )

        # Create box plot for the selected numerical feature by sensitive attribute
        df_plot = df_cleaned[[selected_sensitive_attr,
                              selected_numerical_feature]].dropna()

        if not df_plot.empty:
            fig_dist, ax_dist = plt.subplots(figsize=(10, 6))
            sns.boxplot(x=selected_sensitive_attr, y=selected_numerical_feature,
                        data=df_plot, ax=ax_dist, palette="light:b", dodge=False)
            ax_dist.set_title(
                f"Distribution of {selected_numerical_feature} by {selected_sensitive_attr}")
            ax_dist.set_xlabel(selected_sensitive_attr)
            ax_dist.set_ylabel(selected_numerical_feature)
            st.pyplot(fig_dist)
            plt.close(fig_dist)

            # Calculate and display summary statistics by group
            st.markdown(
                f"**Summary Statistics of {selected_numerical_feature} by {selected_sensitive_attr}:**")
            summary_stats = df_plot.groupby(selected_sensitive_attr)[
                selected_numerical_feature].describe()
            st.dataframe(summary_stats)

            st.markdown(f"""
            **Interpretation:** If, for instance, the median `{selected_numerical_feature}` for 'Female' applicants is consistently lower and less spread out than for 'Male' applicants, it suggests an income disparity that the model might exploit, even if unintentionally. This disparity could lead to a biased prediction if not properly addressed.
            """)
        else:
            st.info(
                f"No valid data available for '{selected_numerical_feature}' and '{selected_sensitive_attr}'.")
    else:
        st.info("No numerical features available for distribution checks.")

    st.markdown("""
    --- 
    **Risk Manager's Insight:** You have now completed a critical assessment of potential biases in the loan application data. The identified disparities in approval rates or feature distributions highlight areas where the model might exhibit unfair behavior. These insights are crucial for developing mitigation strategies and ensuring responsible AI deployment.
    """)

    st.info("✅ Ready to move forward? Use the sidebar navigation to proceed to **Step 6: Risk Simulation & Human Oversight**.", icon="ℹ️")
