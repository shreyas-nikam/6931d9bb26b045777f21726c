
import streamlit as st
import pandas as pd
import datetime

def main():
    st.markdown("### Step 2: Data Provenance & Metadata Management")

    st.markdown("""
    **What you're doing:** As a Risk Manager, it's critical to understand where your data comes from, how it's been transformed, and who has accessed or modified it. This step involves documenting the data's lineage and managing its metadata, which are essential for auditability and compliance.

    **How this helps:** A clear provenance trail helps in tracing back any anomalies or errors to their source, ensuring data integrity and providing a strong evidentiary basis for regulatory audits. Robust metadata management enhances data understanding and reusability.

    **Underlying concept:** Data provenance is the record of the origins and history of a piece of data. Metadata management involves creating and maintaining descriptive information about the data. Together, they form the foundation for data governance and trust in analytical results.
    """)

    st.markdown("#### Existing Metadata")
    st.dataframe(st.session_state.metadata)

    st.markdown("#### Provenance Logs")
    st.dataframe(st.session_state.provenance_logs)

    st.markdown("#### Document Data Lineage")
    st.markdown("""
    **Risk Manager's Action:** Document any significant actions taken on the data, its source, or any transformations. This log is crucial for maintaining a verifiable audit trail.
    """)

    action_description = st.text_area("Describe the data action or lineage event (e.g., "Initial data load from core banking system", "Schema validation performed"):")
    user_name = st.text_input("Your Name/User ID:", value="Risk_Manager_001")

    if st.button("Add to Provenance Log"):
        if action_description:
            new_log_entry = {
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Action": "Data Lineage Documentation",
                "Description": action_description,
                "User": user_name
            }
            st.session_state.provenance_logs = pd.concat(
                [st.session_state.provenance_logs, pd.DataFrame([new_log_entry])],
                ignore_index=True
            )
            st.success("Provenance log updated successfully!")
            st.dataframe(st.session_state.provenance_logs) # Display updated logs immediately
        else:
            st.warning("Please provide a description for the data action.")

    st.markdown("""
    --- 
    **Risk Manager's Insight:** By maintaining meticulous logs, you are building an undeniable record of data handling, which is paramount for justifying model decisions and meeting regulatory requirements.
    """)

    if st.button("Proceed to Data Quality Audits"):
        st.session_state.current_page = "3. Data Quality Audits"
        st.rerun()
