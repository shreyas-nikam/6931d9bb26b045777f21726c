
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.markdown("### Step 4: Data Cleaning and Preprocessing")

    st.markdown("""
    **What you're doing:** As a Risk Manager, after identifying data quality issues, your next crucial task is to clean and preprocess the data. This involves making strategic decisions about handling missing values and outliers to ensure the data is suitable for model training. These decisions directly impact the model's fairness, accuracy, and compliance.

    **How this helps:** By thoughtfully cleaning the data, you remove noise and inconsistencies that could lead to biased outcomes or poor model performance. This step is vital for building a reliable and defensible machine learning model, thereby mitigating significant model risk.

    **Underlying concept:** Data cleaning transforms raw data into a usable format, often involving imputation for missing values and methods to address outliers. Preprocessing techniques standardize or normalize data, preparing it for algorithms, ensuring that the model learns from high-quality, representative data.
    """)

    if st.session_state.raw_data is None:
        st.warning(
            "No raw data available. Please go to 'Data Ingestion & Overview' to load the data.")
        return

    df = st.session_state.raw_data.copy()

    st.markdown("#### Raw Data Sample (Before Cleaning)")
    st.dataframe(df.head())

    st.markdown("#### Missing Value Imputation")
    st.markdown("""
    **Risk Manager's Action:** Decide on the best strategy to handle missing values for each feature. Imputing with the median for numerical data helps maintain the distribution, while using the mode for categorical data ensures the most frequent category is preserved. Your choices here can impact the representativeness of the data and, consequently, the model's fairness and accuracy.
    """)

    # Identify columns with missing values
    missing_cols = df.columns[df.isnull().any()].tolist()
    imputation_strategies = {}

    for col in missing_cols:
        col_type = df[col].dtype
        if pd.api.types.is_numeric_dtype(col_type):
            options = ["Median", "Mean", "Remove Rows"]
            default_index = options.index("Median")  # Use index for default
        else:
            options = ["Mode", "Remove Rows"]
            default_index = options.index("Mode")  # Use index for default

        strategy = st.selectbox(
            f"Select imputation strategy for **`{col}`**:",
            options=options,
            index=default_index,
            key=f"impute_{col}"
        )
        imputation_strategies[col] = strategy

    st.markdown(r"""
    For numerical features like `LoanAmount`, replacing missing values with the **median** avoids skewing the distribution with extreme values that a mean might introduce. If the data for `ApplicantIncome` is missing, using the median ensures that the imputed values are typical for the dataset. For categorical features such as `Gender` or `Married`, using the **mode** (most frequent category) is a common strategy to maintain the overall distribution of categories. Removing rows with missing values can lead to data loss and potential sampling bias if missingness is not random.
    """)

    st.markdown("#### Outlier Handling (Numerical Features)")
    st.markdown("""
    **Risk Manager's Action:** Configure how to handle outliers in numerical features. Outliers, if not addressed, can disproportionately influence model training, leading to erroneous predictions. Capping them to a certain threshold ensures extreme values don't dominate the model's learning, while preserving data points that might still carry some information.
    """)

    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    if "Loan_Amount_Term" in numerical_cols:
        # Often treated as categorical
        numerical_cols.remove("Loan_Amount_Term")

    outlier_handling_strategy = st.selectbox(
        "Select outlier handling strategy:",
        options=["None", "Cap Outliers (IQR Method)",
                 "Remove Outliers (IQR Method)"],
        index=1,  # Default to capping
        key="outlier_strategy"
    )

    iqr_multiplier = 1.5
    if outlier_handling_strategy in ["Cap Outliers (IQR Method)", "Remove Outliers (IQR Method)"]:
        iqr_multiplier = st.slider(
            "IQR Multiplier for Outlier Detection:",
            min_value=1.0, max_value=3.0, value=1.5, step=0.1,
            key="iqr_multiplier"
        )
        st.markdown(r"""
        The Interquartile Range (IQR) method defines outliers as values falling outside $[Q1 - k \times IQR, Q3 + k \times IQR]$, where $Q1$ is the first quartile, $Q3$ is the third quartile, $IQR = Q3 - Q1$, and $k$ is the multiplier (typically $1.5$ for mild outliers, $3.0$ for extreme outliers). A lower multiplier (e.g., $1.5$) will identify more points as outliers, potentially cleaning more aggressively, while a higher multiplier (e.g., $3.0$) will be more conservative.
        """)

    if st.button("Apply Cleaning and Preprocessing"):
        cleaned_df = df.copy()
        log_entries = []

        # Apply missing value imputation
        for col, strategy in imputation_strategies.items():
            if strategy == "Median":
                median_val = cleaned_df[col].median()
                cleaned_df[col].fillna(median_val, inplace=True)
                log_entries.append(
                    f"Imputed missing values in `{col}` with median ({median_val}).")
            elif strategy == "Mean":
                mean_val = cleaned_df[col].mean()
                cleaned_df[col].fillna(mean_val, inplace=True)
                log_entries.append(
                    f"Imputed missing values in `{col}` with mean ({mean_val}).")
            elif strategy == "Mode":
                mode_val = cleaned_df[col].mode()[0]
                cleaned_df[col].fillna(mode_val, inplace=True)
                log_entries.append(
                    f"Imputed missing values in `{col}` with mode ({mode_val}).")
            elif strategy == "Remove Rows":
                initial_rows = len(cleaned_df)
                cleaned_df.dropna(subset=[col], inplace=True)
                rows_removed = initial_rows - len(cleaned_df)
                log_entries.append(
                    f"Removed {rows_removed} rows with missing values in `{col}`.")

        # Apply outlier handling
        if outlier_handling_strategy != "None":
            for col in numerical_cols:
                Q1 = cleaned_df[col].quantile(0.25)
                Q3 = cleaned_df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - iqr_multiplier * IQR
                upper_bound = Q3 + iqr_multiplier * IQR

                if outlier_handling_strategy == "Cap Outliers (IQR Method)":
                    num_capped_lower = (cleaned_df[col] < lower_bound).sum()
                    num_capped_upper = (cleaned_df[col] > upper_bound).sum()
                    cleaned_df[col] = np.where(
                        cleaned_df[col] < lower_bound, lower_bound, cleaned_df[col])
                    cleaned_df[col] = np.where(
                        cleaned_df[col] > upper_bound, upper_bound, cleaned_df[col])
                    if num_capped_lower > 0 or num_capped_upper > 0:
                        log_entries.append(
                            f"Capped {num_capped_lower} lower and {num_capped_upper} upper outliers in `{col}` using IQR multiplier {iqr_multiplier}.")
                elif outlier_handling_strategy == "Remove Outliers (IQR Method)":
                    initial_rows = len(cleaned_df)
                    cleaned_df = cleaned_df[~(
                        (cleaned_df[col] < lower_bound) | (cleaned_df[col] > upper_bound))]
                    rows_removed = initial_rows - len(cleaned_df)
                    if rows_removed > 0:
                        log_entries.append(
                            f"Removed {rows_removed} rows containing outliers in `{col}` using IQR multiplier {iqr_multiplier}.")

        st.session_state.cleaned_data = cleaned_df.reset_index(drop=True)
        st.success("Data cleaning and preprocessing applied successfully!")

        # Update provenance logs
        current_provenance_logs = st.session_state.provenance_logs.copy()
        for entry in log_entries:
            new_log_entry = {
                "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Action": "Data Cleaning & Preprocessing",
                "Description": entry,
                "User": "Risk_Manager_001"
            }
            current_provenance_logs = pd.concat(
                [current_provenance_logs, pd.DataFrame([new_log_entry])],
                ignore_index=True
            )
        st.session_state.provenance_logs = current_provenance_logs

    if st.session_state.cleaned_data is not None:
        st.markdown("#### Cleaned Data Sample (After Preprocessing)")
        st.dataframe(st.session_state.cleaned_data.head())

        st.markdown("#### Comparison: Missing Values Before vs. After Cleaning")
        missing_before = df.isnull().sum()
        missing_after = st.session_state.cleaned_data.isnull().sum()

        comparison_df = pd.DataFrame({
            "Before Cleaning": missing_before,
            "After Cleaning": missing_after
        }).loc[missing_before > 0]

        if not comparison_df.empty:
            st.dataframe(comparison_df)
        else:
            st.info(
                "No missing values were present or all were successfully handled.")

        st.markdown(
            "#### Comparison: Descriptive Statistics (Numerical Features)")
        st.markdown("""
        **Risk Manager's Insight:** Observe how the descriptive statistics (mean, max, min, std) for numerical features have changed after outlier handling. Significant changes might indicate effective outlier mitigation, leading to a more stable dataset for modeling. However, be cautious that overly aggressive cleaning can remove valuable information.
        """)
        st.dataframe(pd.concat([df[numerical_cols].describe().add_prefix("Raw_"),
                                st.session_state.cleaned_data[numerical_cols].describe().add_prefix("Cleaned_")], axis=1))

    st.markdown("""
    --- 
    **Risk Manager's Insight:** You've successfully applied data cleaning strategies, addressing missing values and outliers. This refined dataset is now more robust and less prone to introducing biases or errors into the model. These steps are crucial for maintaining the integrity of the model audit trail.
    """)

    st.info("✅ Ready to move forward? Use the sidebar navigation to proceed to **Step 5: Bias Detection & Analysis**.", icon="ℹ️")
