id: 6931d9bb26b045777f21726c_user_guide
summary: AI Design and Deployment Lab 3 - Clone User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: ML Model Risk Auditing - A User Guide for Risk Managers

## Introduction to ML Model Risk Auditing with QuLab
Duration: 00:05:00

<aside class="positive">
This introductory step sets the stage for your journey as a Risk Manager. It highlights the critical importance of auditing ML models in finance and outlines the comprehensive steps you'll take using QuLab.
</aside>

As a **Risk Manager** at a leading financial institution, your role is paramount in safeguarding the integrity, fairness, and compliance of machine learning models. Automated decisions, while efficient, come with inherent risks, such as potential biases, lack of transparency, and non-compliance with stringent regulatory standards. This codelab will guide you through an **end-to-end data provenance and risk audit** of an ML loan underwriting model using the QuLab application.

This application is designed to provide you with a hands-on experience in managing model risk by walking you through several key stages:

1.  **Ingest and Understand Data**: Start by examining raw loan application data to understand its initial state and identify potential concerns.
2.  **Manage Data Provenance**: Trace and document the lineage of data, ensuring its reliability and accountability throughout the model lifecycle.
3.  **Audit Data Quality**: Pinpoint and address issues like missing values and outliers that could compromise model performance and fairness.
4.  **Perform Data Cleaning and Preprocessing**: Apply necessary transformations and cleaning strategies to prepare data for model training.
5.  **Detect and Analyze Bias**: Uncover and quantify potential biases in the data that might lead to unfair lending decisions, focusing on demographic parity.
6.  **Simulate Risk and Implement Human Oversight**: Evaluate model robustness under uncertainty and identify scenarios requiring human intervention.
7.  **Establish Risk Register & Governance**: Log identified risks and propose mitigation strategies to maintain model accountability.
8.  **Generate an Audit Report**: Compile all findings, analyses, and recommendations into a comprehensive report for stakeholders and regulatory bodies.

Your journey through these stages will empower you to build a robust assurance case, demonstrating the model's trustworthiness, compliance, and fairness, thereby significantly mitigating model risk for your institution.

Let's begin your audit! You can navigate through the different stages using the sidebar on the left.

## 1. Data Ingestion & Overview
Duration: 00:05:00

<aside class="positive">
In this first operational step, you'll perform a crucial initial assessment of the raw data. Understanding the data's fundamental characteristics is the bedrock of any effective audit.
</aside>

**What you're doing:** As a Risk Manager, your first task is to gain a foundational understanding of the raw loan application data. This involves reviewing its structure, content, and initial statistics to identify any immediate anomalies or areas that might require closer scrutiny during the audit process.

**How this helps:** This initial data review is crucial for establishing the baseline for your audit. By understanding the raw state of the data, you can better track transformations, identify data quality issues, and ultimately build a robust case for model trustworthiness.

**Underlying concept:** Data ingestion and initial exploration are fundamental steps in any data-driven workflow, providing the necessary context for subsequent analysis and model development. It ensures that the data being used is understood and relevant to the business problem.

Upon arriving at this page, the application automatically generates a synthetic dataset representing raw loan application data.

You will see:

*   **Raw Loan Application Data Sample**: A quick preview of the first few rows of the dataset. This allows you to inspect the features (columns) and their types at a glance.
*   **Dataset Summary Statistics**: This section provides statistical summaries for all features. For numerical columns, you'll see counts, mean, standard deviation, min, max, and quartiles. For categorical columns, you'll see unique counts and the most frequent value. This helps you understand the distribution and range of values in your dataset.
*   **Missing Values Overview**: A table showing features with missing values, their count, and percentage. This is a critical initial check for data quality.

<aside class="positive">
<b>Risk Manager's Action:</b> You have now reviewed the initial state of the data. Notice the presence of missing values and various data types. This preliminary check helps you anticipate the next steps in data preparation and identify potential data quality risks.
</aside>

Review these initial views to get a sense of the data's completeness and overall structure. Once you are done, click the "Proceed to Data Provenance & Metadata Management" button to move to the next stage.

## 2. Data Provenance & Metadata Management
Duration: 00:07:00

<aside class="positive">
This step is about documenting the journey of your data. A robust provenance trail is essential for regulatory compliance and ensuring that data used in ML models is reliable and auditable.
</aside>

**What you're doing:** As a Risk Manager, it's critical to understand where your data comes from, how it's been transformed, and who has accessed or modified it. This step involves documenting the data's lineage and managing its metadata, which are essential for auditability and compliance.

**How this helps:** A clear provenance trail helps in tracing back any anomalies or errors to their source, ensuring data integrity and providing a strong evidentiary basis for regulatory audits. Robust metadata management enhances data understanding and reusability.

**Underlying concept:** Data provenance is the record of the origins and history of a piece of data. Metadata management involves creating and maintaining descriptive information about the data. Together, they form the foundation for data governance and trust in analytical results.

On this page, you will find:

*   **Existing Metadata**: While not fully implemented for dynamic input in this example, in a real scenario, this would display key attributes of the dataset, such as column descriptions, data sources, and update times.
*   **Provenance Logs**: This table shows a chronological record of actions taken on the data. Initially, it might be empty or contain basic loading information.

**Document Data Lineage:**
You are presented with a form to add new entries to the **Provenance Log**.

*   **Describe the data action or lineage event**: Enter a description of an action you've taken or observed. For instance, you could note "Initial data load from core banking system" or "Schema validation performed."
*   **Your Name/User ID**: Input your identifier for accountability.

<aside class="positive">
<b>Risk Manager's Action:</b> Document any significant actions taken on the data, its source, or any transformations. This log is crucial for maintaining a verifiable audit trail. Fill in the description and your name, then click "Add to Provenance Log."
</aside>

After adding an entry, you will see the updated provenance logs. This ensures every significant step in the data's journey is recorded and attributable.

<aside class="positive">
<b>Risk Manager's Insight:</b> By maintaining meticulous logs, you are building an undeniable record of data handling, which is paramount for justifying model decisions and meeting regulatory requirements.
</aside>

Once you are satisfied with your provenance documentation, click the "Proceed to Data Quality Audits" button.

## 3. Data Quality Audits
Duration: 00:10:00

<aside class="positive">
This is where you systematically inspect your data for imperfections. Detecting and understanding data quality issues is fundamental to preventing errors and biases from propagating into your machine learning model.
</aside>

**What you're doing:** As a Risk Manager, after understanding the data's origin, your next step is to rigorously audit its quality. This means identifying and quantifying issues like missing values and outliers, which can significantly skew model performance and lead to unfair or inaccurate predictions. This step ensures the data's reliability before it's used for any modeling.

**How this helps:** Identifying data quality issues early prevents the propagation of errors into the model. By understanding where data is incomplete or abnormal, you can make informed decisions about cleaning strategies, ultimately leading to a more robust and trustworthy model that adheres to risk guidelines.

**Underlying concept:** Data quality auditing involves assessing the accuracy, completeness, consistency, and timeliness of data. Missing value analysis helps identify gaps, while outlier detection uncovers unusual data points that might represent errors or rare, but significant, events.

If you haven't loaded data in the first step, you will be prompted to do so. Otherwise, you will see two main sections:

#### Missing Values Analysis

<aside class="positive">
<b>Risk Manager's Action:</b> Review the visual representation of missing values. A high percentage of missing data in critical features can indicate a significant data quality risk that needs immediate attention.
</aside>

This section presents a bar chart showing the percentage of missing values for each feature.

*   The chart clearly highlights which features have the most missing information.
*   A common threshold for concern is often around $5-10\%$ missing data for a single feature. If a feature exceeds this, its utility and reliability might be compromised, influencing model accuracy and fairness. For example, if a feature like `Credit_History` is $10\%$ missing, it means $10\%$ of our loan applicants lack this crucial information, potentially leading to biased loan decisions if not handled properly.

#### Outlier Detection (Numerical Features)

<aside class="positive">
<b>Risk Manager's Action:</b> Examine the box plots for numerical features to identify outliers. Outliers can distort statistical analyses and model training, leading to inaccurate risk assessments. Understanding their presence is key to mitigating their impact.
</aside>

For each numerical feature, a box plot is displayed.

*   The box plot visualizes the distribution of data for a numerical feature. Points extending significantly beyond the "whiskers" of the box are considered outliers. These often represent extreme values that might be data entry errors or genuine, but unusual, observations. For instance, in `ApplicantIncome`, unusually high incomes might be outliers. These outliers can inflate variance and affect statistical significance, potentially misleading the model's understanding of typical loan applicant behavior.
*   Mathematically, outliers are often defined as values that fall below $Q1 - 1.5 \times IQR$ or above $Q3 + 1.5 \times IQR$, where $Q1$ is the first quartile, $Q3$ is the third quartile, and $IQR$ is the Interquartile Range ($Q3 - Q1$).

<aside class="positive">
<b>Risk Manager's Insight:</b> You've now identified critical data quality issues: missing values and outliers. These findings directly inform the necessity of data cleaning and preprocessing steps to ensure the data is fit for model consumption and that model risk is minimized.
</aside>

Once you have thoroughly reviewed the data quality, click "Proceed to Data Cleaning and Preprocessing" to fix these issues.

## 4. Data Cleaning and Preprocessing
Duration: 00:12:00

<aside class="positive">
This step is where you actively improve the data's quality based on your audit findings. Your decisions here directly influence the model's reliability, fairness, and compliance.
</aside>

**What you're doing:** As a Risk Manager, after identifying data quality issues, your next crucial task is to clean and preprocess the data. This involves making strategic decisions about handling missing values and outliers to ensure the data is suitable for model training. These decisions directly impact the model's fairness, accuracy, and compliance.

**How this helps:** By thoughtfully cleaning the data, you remove noise and inconsistencies that could lead to biased outcomes or poor model performance. This step is vital for building a reliable and defensible machine learning model, thereby mitigating significant model risk.

**Underlying concept:** Data cleaning transforms raw data into a usable format, often involving imputation for missing values and methods to address outliers. Preprocessing techniques standardize or normalize data, preparing it for algorithms, ensuring that the model learns from high-quality, representative data.

First, you'll see a sample of the **Raw Data** before any cleaning.

#### Missing Value Imputation

<aside class="positive">
<b>Risk Manager's Action:</b> Decide on the best strategy to handle missing values for each feature. Imputing with the median for numerical data helps maintain the distribution, while using the mode for categorical data ensures the most frequent category is preserved. Your choices here can impact the representativeness of the data and, consequently, the model's fairness and accuracy.
</aside>

For each column identified with missing values in the previous step, you will see a dropdown menu to select an imputation strategy:

*   **Numerical Features (e.g., `LoanAmount`)**: Options typically include "Median", "Mean", or "Remove Rows".
*   **Categorical Features (e.g., `Gender`)**: Options typically include "Mode" or "Remove Rows".

For numerical features like `LoanAmount`, replacing missing values with the **median** avoids skewing the distribution with extreme values that a mean might introduce. If the data for `ApplicantIncome` is missing, using the median ensures that the imputed values are typical for the dataset. For categorical features such as `Gender` or `Married`, using the **mode** (most frequent category) is a common strategy to maintain the overall distribution of categories. Removing rows with missing values can lead to data loss and potential sampling bias if missingness is not random.

#### Outlier Handling (Numerical Features)

<aside class="positive">
<b>Risk Manager's Action:</b> Configure how to handle outliers in numerical features. Outliers, if not addressed, can disproportionately influence model training, leading to erroneous predictions. Capping them to a certain threshold ensures extreme values don't dominate the model's learning, while preserving data points that might still carry some information.
</aside>

You will select a strategy for handling outliers in numerical features:

*   **None**: Do nothing to outliers.
*   **Cap Outliers (IQR Method)**: Extreme values are replaced with a predefined upper or lower bound.
*   **Remove Outliers (IQR Method)**: Rows containing outliers are removed from the dataset.

If you choose a capping or removal strategy, you can adjust the **IQR Multiplier** using a slider (typically between 1.0 and 3.0). The Interquartile Range (IQR) method defines outliers as values falling outside $[Q1 - k \times IQR, Q3 + k \times IQR]$, where $Q1$ is the first quartile, $Q3$ is the third quartile, $IQR = Q3 - Q1$, and $k$ is the multiplier (typically $1.5$ for mild outliers, $3.0$ for extreme outliers). A lower multiplier (e.g., $1.5$) will identify more points as outliers, potentially cleaning more aggressively, while a higher multiplier (e.g., $3.0$) will be more conservative.

After selecting your strategies, click the "Apply Cleaning and Preprocessing" button.

Once applied, you will see:

*   **Cleaned Data Sample**: A preview of the data after your selected cleaning steps.
*   **Comparison: Missing Values Before vs. After Cleaning**: A table showing how many missing values were present before and after your cleaning actions, demonstrating the effectiveness of your chosen strategies.
*   **Comparison: Descriptive Statistics (Numerical Features)**:
    <aside class="positive">
    <b>Risk Manager's Insight:</b> Observe how the descriptive statistics (mean, max, min, std) for numerical features have changed after outlier handling. Significant changes might indicate effective outlier mitigation, leading to a more stable dataset for modeling. However, be cautious that overly aggressive cleaning can remove valuable information.
    </aside>

<aside class="positive">
<b>Risk Manager's Insight:</b> You've successfully applied data cleaning strategies, addressing missing values and outliers. This refined dataset is now more robust and less prone to introducing biases or errors into the model. These steps are crucial for maintaining the integrity of the model audit trail.
</aside>

Click "Proceed to Bias Detection & Analysis" to continue.

## 5. Bias Detection & Analysis
Duration: 00:15:00

<aside class="negative">
Bias in ML models can lead to unfair and discriminatory outcomes, especially in sensitive applications like loan underwriting. This step allows you to proactively identify and understand these biases, which is crucial for ethical AI and regulatory compliance.
</aside>

**What you're doing:** As a Risk Manager, your role extends to ensuring fairness. This step is dedicated to uncovering and quantifying potential biases within the cleaned data that could lead to unfair lending decisions. You will specifically focus on evaluating demographic parity, ensuring that model outcomes are equitable across different sensitive groups.

**How this helps:** Identifying biases early allows for targeted mitigation strategies, preventing the deployment of models that could lead to discriminatory practices. This is vital for ethical AI, maintaining public trust, and complying with anti-discrimination regulations.

**Underlying concept:** Bias detection involves using statistical methods and fairness metrics to assess whether a model or its underlying data exhibits prejudice against certain demographic groups. **Demographic parity** is a fairness metric where the proportion of individuals receiving a positive outcome (e.g., loan approval) should be roughly equal across different demographic groups.

You will begin by configuring the bias analysis:

*   **Select Sensitive Attribute**: Choose a categorical feature from your data (e.g., `Gender`, `Education`, `Property_Area`) that represents a sensitive demographic characteristic.
*   **Select Favorable Outcome**: Specify which value in the `Loan_Status` column represents a favorable outcome (e.g., "Y" for approved loans).

After selecting these parameters, click "Analyze Bias". The application will then compute and display:

#### Approval Rate Disparity

This section will show the percentage of loan approvals for each category within your chosen sensitive attribute. For example, if you chose "Gender", it would display the approval rate for "Male" vs. "Female".

*   A significant difference in approval rates between groups suggests a potential for algorithmic bias. If the approval rate for "Female" applicants is significantly lower than for "Male" applicants, it indicates a disparity that could lead to unfair lending decisions.

#### Feature Distribution Analysis

For numerical features, the application will display distribution plots (e.g., histograms or kernel density estimates) for each group within the sensitive attribute. For example, if "Gender" is the sensitive attribute, you might see the distribution of `ApplicantIncome` for "Male" vs. "Female" applicants.

*   <aside class="positive">
    <b>Risk Manager's Action:</b> Compare these distributions carefully. If the income distribution for 'Female' applicants is consistently lower and less spread out than for 'Male' applicants, it suggests an income disparity that the model might exploit, even if unintentionally. This disparity could lead to a biased prediction if not properly addressed.
    </aside>

<aside class="positive">
<b>Risk Manager's Insight:</b> You have now completed a critical assessment of potential biases in the loan application data. The identified disparities in approval rates or feature distributions highlight areas where the model might exhibit unfair behavior. These insights are crucial for developing mitigation strategies and ensuring responsible AI deployment.
</aside>

Click "Proceed to Risk Simulation & Human Oversight" to continue your audit.

## 6. Risk Simulation & Human Oversight
Duration: 00:10:00

<aside class="positive">
This step moves beyond historical data to explore the model's behavior under future uncertainties. By simulating various scenarios, you can uncover vulnerabilities and strategically embed human judgment where it's most needed.
</aside>

**What you're doing:** As a Risk Manager, you need to assess how robust the model's decisions are under various conditions, especially when there's uncertainty in the input data. This involves simulating potential data fluctuations or errors and observing their impact on loan underwriting outcomes. Crucially, you'll define criteria for flagging cases that require human review, ensuring critical decisions benefit from expert judgment.

**How this helps:** Risk simulation helps identify scenarios where the model might be vulnerable or make unreliable predictions. By setting up clear human oversight thresholds, you establish a safety net, ensuring that high-stakes decisions are not solely automated and adhere to the institution's risk appetite and ethical guidelines. This proactive approach prevents erroneous decisions and reinforces responsible AI deployment.

**Underlying concept:** Risk simulation uses techniques like Monte Carlo methods (though simplified here) to model the impact of input variable uncertainty on model outputs. Human oversight integrates expert judgment into automated workflows, typically by setting thresholds (e.g., a "probability of default" score) that trigger manual review for cases falling into critical or ambiguous zones. This balances automation efficiency with human accountability.

You will configure the simulation parameters:

#### Configure Simulation Parameters

<aside class="positive">
<b>Risk Manager's Action:</b> Adjust the sliders below to introduce hypothetical uncertainty into key financial features. Consider scenarios where applicants might slightly misreport income or loan amounts are estimated with a margin of error. Also, set the threshold for what constitutes a "high-risk" loan requiring your personal review.
</aside>

*   **Applicant Income Uncertainty (+/- %)**: Simulate a percentage fluctuation in reported applicant income.
*   **Loan Amount Uncertainty (+/- %)**: Simulate a percentage fluctuation in requested loan amounts.
*   **Credit History Data Noise (Probability of Falsification/Error)**: Introduce a small probability that a credit history record might be flipped (good to bad, or bad to good).

#### Human Oversight Thresholds

*   **Probability of Default Threshold for Human Review**: This slider allows you to set a threshold for the mock risk score generated by the application.
    The **Probability of Default (PD)** threshold for human review, denoted as $T_{HR}$, is a critical governance parameter. If a loan application's simulated risk score (PD) exceeds this threshold, i.e., $PD_{simulated} > T_{HR}$, it automatically triggers a manual review by a human expert. This ensures that high-risk cases, or those with uncertain outcomes, are subjected to closer scrutiny, mitigating potential financial losses and reputational damage. For instance, if $T_{HR} = 0.6$, any loan with a $PD_{simulated}$ greater than $0.6$ is flagged.

Click "Run Risk Simulation". The application will generate mock risk scores and flag applications for human review based on your settings.

#### Simulation Results Overview

<aside class="positive">
<b>Risk Manager's Insight:</b> Review the impact of the simulated uncertainty on the predicted outcomes and, more importantly, the number of cases flagged for human review. This shows you where the model's automation might need human intervention due to increased risk or uncertainty.
</aside>

You will see:

*   A summary table and a bar chart showing the number of applications "Flagged for Human Review" versus those "Not Flagged".
    The bar chart illustrates the distribution of loan applications that require human review based on the set **Probability of Default Threshold** ($T_{HR}$). A higher number of flagged cases might indicate either an overly conservative threshold or a genuinely higher-risk portfolio under the simulated conditions. This visualization immediately tells the Risk Manager how much manual effort might be required to process the loan applications, highlighting operational risk.
*   **Sample of Applications Flagged for Human Review**: A table showing the top 10 applications with the highest simulated risk scores that were flagged.

<aside class="positive">
<b>Risk Manager's Action:</b> You have successfully simulated risk and identified cases requiring human oversight. This process validates the model's behavior under stress and reinforces the importance of human-in-the-loop decision-making for high-risk scenarios. This forms a crucial part of your assurance case.
</aside>

Click "Proceed to Risk Register & Governance" to formalize your findings.

## 7. Risk Register & Governance
Duration: 00:08:00

<aside class="positive">
This step is about turning observations into actionable governance. Formally documenting risks in a structured register ensures accountability, enables proactive management, and facilitates compliance with regulatory expectations.
</aside>

**What you're doing:** As a Risk Manager, after identifying potential biases and simulating various risk scenarios, it's crucial to formally document these risks, assess their severity, and propose concrete mitigation strategies. This step involves updating the institutional **Risk Register**, a central repository for tracking and managing all identified risks related to the ML model. This ensures a transparent and accountable governance framework.

**How this helps:** A well-maintained risk register provides a comprehensive overview of all model-related risks, their potential impact, and the planned actions to control them. This systematic approach allows for proactive risk management, facilitates compliance reporting, and informs strategic decisions to enhance model trustworthiness and reduce overall organizational exposure.

**Underlying concept:** A risk register is a key tool in enterprise risk management, providing a structured way to identify, analyze, and monitor risks. Governance refers to the framework of rules, practices, and processes by which an organization is directed and controlled. For ML models, this includes establishing clear responsibilities, audit trails, and decision-making protocols to ensure ethical and compliant AI deployment.

#### Current Model Risk Register

<aside class="positive">
<b>Risk Manager's Action:</b> Review the existing entries in the risk register. These might include risks identified during data quality audits, bias detection, or the risk simulation phase. Your role is to ensure all relevant risks are captured and adequately assessed.
</aside>

This section displays the current state of your risk register. It will contain any risks you've previously added.

#### Add New Risk Entry

<aside class="positive">
<b>Risk Manager's Action:</b> Use the form below to document any newly identified risks or to elaborate on existing ones. Be precise in your description, assign appropriate likelihood and impact, and propose clear, actionable mitigation strategies. This structured documentation is vital for governance and accountability.
</aside>

You will use a form to add a new risk entry:

*   **Risk ID**: An automatically generated identifier.
*   **Risk Name**: A concise name for the risk (e.g., "Gender Bias in Loan Approval").
*   **Category**: Classify the risk (e.g., "Data Quality", "Bias", "Model Performance").
*   **Description of the Risk**: Provide detailed information about the nature of the risk.
*   **Likelihood**: Select how probable the risk is to occur ("Low", "Medium", "High").
*   **Impact**: Select the severity of the consequences if the risk materializes ("Low", "Medium", "High").
*   **Proposed Mitigation Strategy**: Describe the actions planned or taken to reduce or eliminate the risk.
*   **Status**: Track the progress of the risk ("Open", "In Progress", "Closed").
*   **Owner**: Assign responsibility for managing the risk (e.g., "Head of Model Risk").

When you click "Add Risk to Register", the risk will be added to the table, and a **Risk Score** will be calculated based on your likelihood and impact choices. For example, if "Likelihood" and "Impact" are mapped to numerical values (e.g., Low=1, Medium=2, High=3), the Risk Score could be calculated as $Likelihood \times Impact$. A higher score indicates a more critical risk that needs immediate attention.

<aside class="positive">
<b>Risk Manager's Insight:</b> By maintaining a detailed risk register, you're not just identifying problems; you're actively contributing to the institution's robust model governance framework. This documentation is crucial for internal reviews and external regulatory compliance, demonstrating a proactive approach to managing AI-related risks.
</aside>

Click "Proceed to Audit Report & Insights" to generate your final report.

## 8. Audit Report & Insights
Duration: 00:05:00

<aside class="positive">
This is the grand finale! You'll compile all your hard work into a definitive audit report. This document is your assurance case, communicating the model's trustworthiness, identified risks, and mitigation efforts to all stakeholders.
</aside>

**What you're doing:** As a Risk Manager, you've meticulously worked through the data provenance, quality, bias detection, and risk simulation stages. Now, your final task is to compile all these findings into a comprehensive audit report. This report serves as a definitive assurance case, documenting the model's trustworthiness, compliance, and fairness for both internal stakeholders and regulatory bodies.

**How this helps:** The audit report is the culmination of your entire risk management process. It provides a clear, defensible summary of the model's adherence to standards, the risks identified, and the mitigation strategies proposed. This document is crucial for regulatory compliance, internal governance, and fostering trust in the automated decision-making system.

**Underlying concept:** An audit report formally communicates the results of an audit, including findings, conclusions, and recommendations. In the context of ML model risk, it synthesizes technical analyses into a business-relevant narrative, providing transparency and accountability for the model's lifecycle management. It acts as a formal record, supporting the overall model governance framework.

#### Comprehensive Model Audit Report Summary

<aside class="positive">
<b>Risk Manager's Action:</b> Review the automatically generated summary of the audit findings. This consolidates all your decisions and observations from the previous steps, providing a holistic view of the model's risk profile and the actions taken.
</aside>

This section presents a summary of all the actions and findings from the previous steps:

*   **Data Ingestion & Overview**: Summarizes initial data load and missing value counts.
*   **Data Provenance & Metadata Management**: Reports on the number and latest provenance log entries.
*   **Data Quality Audits**: Provides an overview of missing value resolution and outlier detection.
*   **Data Cleaning and Preprocessing**: Confirms data cleaning operations and their impact.
*   **Bias Detection & Analysis**: Summarizes bias findings, including approval rate disparities and feature distribution insights.
*   **Risk Simulation & Human Oversight**: Details the simulation parameters, the number of flagged applications, and the human review threshold.
*   **Risk Register & Governance**: Provides statistics on documented risks, including open risks and high-scoring risks.
*   **Final Narrative & Conclusion**: A concluding statement on the overall audit, emphasizing the importance of continuous monitoring and human oversight.

You will also find a **Download Full Audit Report (Text)** button, allowing you to save this comprehensive summary for your records or to share with stakeholders.

<aside class="positive">
<b>Risk Manager's Final Reflection:</b> You have successfully completed a full audit cycle for the ML loan underwriting model. The generated report is your testament to ensuring responsible AI. This rigorous process not only highlights areas for improvement but also provides the necessary evidence for regulatory compliance and stakeholder confidence.
</aside>

#### Next Steps for Governance:

*   **Regular Review:** Schedule periodic audits to reassess data quality, model performance, and bias metrics.
*   **Mitigation Tracking:** Continuously monitor the status of risks in the Risk Register and the effectiveness of implemented mitigation strategies.
*   **Policy Updates:** Propose updates to internal policies and procedures based on audit findings to strengthen model governance.

Congratulations on completing your audit with QuLab!
