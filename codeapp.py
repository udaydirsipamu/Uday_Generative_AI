import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBpBRtvT1h6X9LIWWsrrQE9d9HAvBWUZEk")
llm = genai.GenerativeModel('models/gemini-1.5-flash')

st.title(" 💬 An AI  Code Reviewer")
st.write("Enter your Python code here...")

code_input=st.text_area("")

if st.button("Generate"):
    if code_input.strip():
        
        bug_report_prompt = f"Analyze the following Python code and provide a detailed description of any bugs found, without including any corrections or fixed code. Only list the issues:\n{code_input}"
        bug_report_response=llm.generate_content(bug_report_prompt)
        bug_report=bug_report_response.text

        fixed_code_prompt = f"Provide the corrected code along with an explanation only, do not include bug description,do not include  quotes in python code part like ```:\n{code_input}"
        fixed_code_response=llm.generate_content(fixed_code_prompt)
        fixed_code=fixed_code_response.text
        
        st.subheader("Code Review")
        st.write("Bug Report")
        st.write(bug_report)

        st.subheader("Fixed Code")
        st.code(fixed_code)