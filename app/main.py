import os

import streamlit as st

from app.JobSearcher import JobSearcher
from app.ResumeAnalyzer import ResumeAnalyzer

MODEL_API_KEY = os.environ["MODEL_API_KEY"]
MODEL_NAME = os.environ["MODEL_NAME"]
resume_analyzer = ResumeAnalyzer(MODEL_API_KEY, MODEL_NAME)
job_searcher = JobSearcher()

OUTPUT_DIR = "resume_storage/"

st.set_page_config(layout="wide")
st.markdown("## Let's find the best job for you.")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")
if uploaded_file is not None:
    st.write("Resume uploaded.")
    resume_path = OUTPUT_DIR + "resume.pdf"
    with open(resume_path, "w") as file:
        file.write(uploaded_file.getvalue())

# description_filter = st.text_input("Anything else you want to filter for?")
submit_button = st.button("Search")
if submit_button:
    print("Time to search")
    resume_analysis = resume_analyzer.analyze(resume_path)
    st.write(resume_analysis)
    jobs = job_searcher.get_relevant_jobs(resume_analysis)
    st.write(jobs)