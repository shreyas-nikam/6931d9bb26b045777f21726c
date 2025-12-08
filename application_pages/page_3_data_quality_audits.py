
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.markdown("### Step 3: Data Quality Audits")

    st.markdown("""
    **What you're doing:** As a Risk Manager, after understanding the data's origin, your next step is to rigorously audit its quality. This means identifying and quantifying issues like missing values and outliers, which can significantly skew model performance and lead to unfair or inaccurate predictions. This step ensures the data's reliability before it's used for any modeling.

    **How this helps:** Identifying data quality issues early prevents the propagation of errors into the model. By understanding where data is incomplete or abnormal, you can make informed decisions about cleaning strategies, ultimately leading to a more robust and trustworthy model that adheres to risk guidelines.

    **Underlying concept:** Data quality auditing involves assessing the accuracy, completeness, consistency, and timeliness of data. Missing value analysis helps identify gaps, while outlier detection uncovers unusual data points that might represent errors or rare, but significant, events.
    """)

    if st.session_state.raw_data is not None:
        df = st.session_state.raw_data.copy()

        st.markdown("#### Missing Values Analysis")
        st.markdown("""
        **Risk Manager's Action:** Review the visual representation of missing values. A high percentage of missing data in critical features can indicate a significant data quality risk that needs immediate attention.
        """)
        missing_data = df.isnull().sum().to_frame(name="Missing Count")
        missing_data["Missing Percentage"] = (
            missing_data["Missing Count"] / len(df)) * 100
        missing_data = missing_data[missing_data["Missing Count"] > 0].sort_values(
            by="Missing Percentage", ascending=False)

        if not missing_data.empty:
            fig_missing, ax_missing = plt.subplots(figsize=(10, 6))
            sns.barplot(x=missing_data.index, y="Missing Percentage",
                        data=missing_data, ax=ax_missing, palette="viridis")
            ax_missing.set_title("Percentage of Missing Values Per Feature")
            ax_missing.set_ylabel("Missing Percentage (%)")
            ax_missing.set_xlabel("Features")
            ax_missing.tick_params(axis='x', rotation=45)
            st.pyplot(fig_missing)
            st.markdown(f"""
            The bar chart above shows the percentage of missing values for each feature. Features with a significant proportion of missing data (e.g., Credit_History, Gender, Married) will require careful handling during the cleaning phase.
            """)
            st.markdown(r"""
            A common threshold for concern is often around $5-10%$ missing data for a single feature. If a feature exceeds this, its utility and reliability might be compromised, influencing model accuracy and fairness. For example, if a feature like Credit_History is $10%$ missing, it means $10%$ of our loan applicants lack this crucial information, potentially leading to biased loan decisions if not handled properly.
            """)
        else:
            st.info("No missing values found in the dataset.")

        st.markdown("#### Outlier Detection (Numerical Features)")
        st.markdown("""
        **Risk Manager's Action:** Examine the box plots for numerical features to identify outliers. Outliers can distort statistical analyses and model training, leading to inaccurate risk assessments. Understanding their presence is key to mitigating their impact.
        """)

        numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
        if "Loan_Amount_Term" in numerical_cols:  # Exclude if it's more categorical than numerical in context
            numerical_cols.remove("Loan_Amount_Term")
        if "Credit_History" in numerical_cols:
            numerical_cols.remove("Credit_History")

        if numerical_cols:
            selected_col = st.selectbox(
                "Select a numerical column to detect outliers:",
                options=numerical_cols,
                key="outlier_column_selector"
            )

            if selected_col:
                st.markdown(f"##### Outliers in `{selected_col}`")
                fig_outlier, ax_outlier = plt.subplots(figsize=(8, 4))
                sns.boxplot(x=df[selected_col],
                            ax=ax_outlier, palette="rocket")
                ax_outlier.set_title(f"Box Plot of {selected_col}")
                st.pyplot(fig_outlier)
                st.markdown(r"""
                The box plot above visualizes the distribution of data for a numerical feature. Points extending significantly beyond the "whiskers" of the box are considered outliers. These often represent extreme values that might be data entry errors or genuine, but unusual, observations. For instance, in `ApplicantIncome`, unusually high incomes might be outliers. These outliers can inflate variance and affect statistical significance, potentially misleading the model's understanding of typical loan applicant behavior.
                Mathematically, outliers are often defined as values that fall below $Q1 - 1.5 \times IQR$ or above $Q3 + 1.5 \times IQR$, where $Q1$ is the first quartile, $Q3$ is the third quartile, and $IQR$ is the Interquartile Range ($Q3 - Q1$).
                """)
        else:
            st.info("No numerical features found for outlier detection.")

        st.markdown("""
        --- 
        **Risk Manager's Insight:** You've now identified critical data quality issues: missing values and outliers. These findings directly inform the necessity of data cleaning and preprocessing steps to ensure the data is fit for model consumption and that model risk is minimized.
        """)

        st.info("✅ Ready to move forward? Use the sidebar navigation to proceed to **Step 4: Data Cleaning and Preprocessing**.", icon="ℹ️")
    else:
        st.warning(
            "Please ingest data first on the 'Data Ingestion & Overview' page.")
        if st.button("Go to Data Ingestion & Overview"):
            st.session_state.current_page = "1. Data Ingestion & Overview"
            st.rerun()
