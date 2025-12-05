# QuLab: ML Model Risk Auditing (Streamlit Lab Project)

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## 1. Project Title and Description

**Project Title:** QuLab: ML Model Risk Auditing

**Description:**
QuLab is an interactive Streamlit application designed as a laboratory project for **Risk Managers** in financial institutions. It provides a comprehensive, step-by-step narrative to conduct a thorough **data provenance and risk audit** of an ML loan underwriting model.

In today's data-driven financial landscape, automated decisions in sensitive areas like loan underwriting carry inherent risks, including potential biases, lack of transparency, and non-compliance with regulatory standards. This application guides users through an end-to-end workflow to:

*   **Understand and manage the data lifecycle**: From initial ingestion to cleaning and preprocessing.
*   **Identify and mitigate risks**: Detect data quality issues, analyze potential biases, and simulate model behavior under uncertainty.
*   **Establish robust governance**: Document data lineage, maintain a risk register, and define human oversight mechanisms.
*   **Generate an assurance report**: Compile all findings into a comprehensive audit report for stakeholders and regulatory bodies.

The goal of QuLab is to build a strong assurance case, evidencing the model's trustworthiness, compliance, and fairness, thereby mitigating overall model risk for the institution.

## 2. Features

QuLab guides the Risk Manager through the following core stages, each accessible via the sidebar navigation:

1.  **Data Ingestion & Overview**:
    *   Load and display a sample of synthetic raw loan application data.
    *   Provide summary statistics and an initial overview of missing values.
    *   Understand the initial state of data before any transformations.

2.  **Data Provenance & Metadata Management**:
    *   Review existing metadata and provenance logs.
    *   Document data actions and lineage events, creating an auditable trail.

3.  **Data Quality Audits**:
    *   Visualize and analyze missing values across features (bar charts).
    *   Detect and visualize outliers in numerical features using box plots.
    *   Highlight potential data quality risks that can impact model performance and fairness.

4.  **Data Cleaning and Preprocessing**:
    *   Interactive controls to select imputation strategies for missing categorical and numerical values (Median, Mean, Mode, Remove Rows).
    *   Configure outlier handling strategies (None, Cap, Remove) using the IQR method with an adjustable multiplier.
    *   Display comparison of dataframes and statistics before and after cleaning.
    *   Log all cleaning actions in the provenance register.

5.  **Bias Detection & Analysis**:
    *   Identify and quantify potential biases within the dataset.
    *   Focus on demographic parity (e.g., loan approval rates across gender).
    *   Visualize distributions of key features for different sensitive groups to uncover disparities.
    *   (Note: The provided code snippet for this page is incomplete, but the intention is to perform these analyses).

6.  **Risk Simulation & Human Oversight**:
    *   Simulate uncertainty in key financial features (e.g., Applicant Income, Loan Amount, Credit History).
    *   Generate mock risk scores based on the (potentially perturbed) data.
    *   Define a customizable "Probability of Default" threshold for human review.
    *   Identify and display cases that are flagged for human intervention, illustrating the human-in-the-loop mechanism.

7.  **Risk Register & Governance**:
    *   Maintain an institutional risk register to formally document identified risks.
    *   Allow users to add new risk entries with details like ID, name, category, description, likelihood, impact, mitigation strategy, status, and owner.
    *   Automatically calculate a risk score (Likelihood * Impact).
    *   Update provenance logs for risk register actions.

8.  **Audit Report & Insights**:
    *   Generate a comprehensive summary of all audit findings from the previous steps.
    *   Provide insights into data quality, bias analysis results, simulation outcomes, and the current state of the risk register.
    *   Enable downloading of the full audit report as a text file.
    *   Suggest next steps for ongoing model governance.

## 3. Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   **Python 3.8+**
*   **pip** (Python package installer)
*   **Git** (for cloning the repository)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quolab-ml-risk-auditing.git
    cd quolab-ml-risk-auditing
    ```
    (Replace `your-username/quolab-ml-risk-auditing` with the actual repository path if different.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    First, create a `requirements.txt` file in the root of your project:

    ```bash
    # requirements.txt
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    ```

    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## 4. Usage

To run the Streamlit application:

1.  **Ensure your virtual environment is activated** (if you created one).
2.  **Navigate to the project's root directory** (where `app.py` is located).
3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This command will open the application in your default web browser (usually at `http://localhost:8501`).

**Basic Usage Instructions:**

*   **Navigation:** Use the sidebar on the left to navigate between the different audit stages (Steps 1 through 8).
*   **Interactivity:** Each page presents detailed explanations, data visualizations, and interactive widgets (sliders, select boxes, text inputs) to perform audit actions and configure parameters.
*   **Workflow:** Follow the numbered steps sequentially to experience the full model risk auditing narrative.
*   **Session State:** The application uses Streamlit's session state to maintain data and audit findings as you progress through the pages.

## 5. Project Structure

The project is organized as follows:

```
quolab-ml-risk-auditing/
├── app.py
├── application_pages/
│   ├── __init__.py
│   ├── page_1_data_ingestion.py
│   ├── page_2_data_provenance.py
│   ├── page_3_data_quality_audits.py
│   ├── page_4_data_cleaning.py
│   ├── page_5_bias_detection.py
│   ├── page_6_risk_simulation.py
│   ├── page_7_risk_register.py
│   └── page_8_audit_report.py
├── requirements.txt
└── README.md
```

*   `app.py`: The main Streamlit entry point. It sets up the page configuration, displays the welcome message, and manages navigation to individual application pages based on user selection.
*   `application_pages/`: A directory containing separate Python modules for each step of the audit process. This modular design helps keep the code organized and manageable.
*   `requirements.txt`: Lists all Python dependencies required to run the application.
*   `README.md`: This file, providing an overview of the project.

## 6. Technology Stack

*   **Streamlit**: The primary framework for building the interactive web application and its user interface.
*   **Pandas**: Used extensively for data manipulation, analysis, and management of tabular data (DataFrames).
*   **NumPy**: Provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays.
*   **Matplotlib**: A comprehensive library for creating static, animated, and interactive visualizations in Python.
*   **Seaborn**: A Python data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.

## 7. Contributing

This project is primarily a lab exercise. However, if you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 8. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if you plan to include one).

## 9. Contact

For any questions or feedback, please reach out:

*   **QuantUniversity** - [Website](https://www.quantuniversity.com/)
*   **Project Maintainer**: [Your Name/Org] - [Your Email/LinkedIn]

---
_Built with Streamlit for Responsible AI in Finance._


## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
