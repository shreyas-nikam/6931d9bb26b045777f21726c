Female' applicants is consistently lower and less spread out than for 'Male' applicants, it suggests an income disparity that the model might exploit, even if unintentionally. This disparity could lead to a biased prediction if not properly addressed.
            """)
    else:
        st.info("No numerical features available for distribution checks.")

    st.markdown("""
    --- 
    **Risk Manager's Insight:** You have now completed a critical assessment of potential biases in the loan application data. The identified disparities in approval rates or feature distributions highlight areas where the model might exhibit unfair behavior. These insights are crucial for developing mitigation strategies and ensuring responsible AI deployment.
    """)

    if st.button("Proceed to Risk Simulation & Human Oversight"):
        st.session_state.current_page = "6. Risk Simulation & Human Oversight"
        st.rerun()
