import os

import streamlit as st

from app.JobSearcher import JobSearcher
from app.ResumeAnalyzer import ResumeAnalyzer

MODEL_API_KEY = os.environ["MODEL_API_KEY"]
MODEL_NAME = os.environ["MODEL_NAME"]
resume_analyzer = ResumeAnalyzer(MODEL_API_KEY, MODEL_NAME)
job_searcher = JobSearcher()

st.set_page_config(layout="wide")
st.markdown("## Let's find the best job for you.")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")
input_resume = None
if uploaded_file is not None:
    st.write(input_resume)

description_filter = st.text_input("Anything else you want to filter for?")
submit_button = st.button("Search")
if submit_button:
    print("Time to search")