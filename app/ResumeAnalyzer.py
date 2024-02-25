class ResumeAnalyzer:
    def __init__(self):
        pass

    def analyze(self, resume_input):
        import nest_asyncio
        import os
        from llama_parse import LlamaParse
        import openai
        import json
        import textwrap
        nest_asyncio.apply()
        os.environ["LLAMA_CLOUD_API_KEY"] = "llx-X"
        documents = LlamaParse(result_type="text").load_data("./Resume_DSI.pdf")
        text = """Document(id_='96dd1b7f-6c8e-4158-b36b-a13cbd113fff', embedding=None, metadata={'file_path': './Resume_DSI.pdf'}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, 
        text='                              ULLAS TERAKANAMBI LOKESH\nSan Francisco, CA | (+1)3477556646 | uterakanambilokesh@sfsu.edu | www.linkedin.com/in/ullastl/ | github.com/ULLAS-T-L |
        \nTECHNICAL SKILLS\n• Languages: Python, R, SQL, Scala\n• Toolkit: Numpy, Pandas, TensorFlow, OpenCV, Flask, Streamlit, RStudio, Git, Jupyter, pinecone, SQL Server, MySQL, NoSQL, Neo4j,
        \n  MongoDB, Oracle database, Alteryx, Tableau, Hadoop, Azure DevOps, Confl        uence, Azure Cloud, Linux, Docker, Kubernetes
        \n• Machine Learning: Supervised Learning - Linear Regression, Logistic Regression, Classifi    cation, KNN, , A/B Testing, Hyperparam-
        \n  eter Tuning, Sentiment analysis, Decision Trees, Ensemble Trees, Bagging and Boosting techniques, Statistical analysis.
        \n  Unsupervised learning – Market Basket Analytics, Clustering (K-Means, Hierarchical, Fuzzy, DBScan) Dimensionality Reduction,
        \n  Optimization, Maximum Likelihood Estimation, Topic Modeling, Bayesian statistics, Probability, Deep Neural Networks
        \n• Data Visualization: Matplotlib, Seaborn, Tableau, Excel, ggplot, RShiny, Plotly\nWORK EXPERIENCE\nAgile DataPro Inc.                                                                                                       Campbell, CA\nData Science Intern                                                                                               Sep 2023 - Dec 2023\n• Spearheaded the exploration of resume parsing and scoring using spaCy, demonstrating profi       ciency in natural language process-\n  ing techniques.\n• Spearheaded the discussion and implementation of Pinecone, boosting the efficiency of resume search by 20% compared to\n  traditional semantic search through the use of advanced vector embeddings.\nNeoSoul Software Solutions Pvt Ltd                                                                                    Bengaluru, India\nData Analyst                                                                                                      June 2019 - July 2021\n• Designed and implemented an optimized facility location model utilizing Python, leveraging advanced data analytics techniques\n  and libraries. This model was applied to a dataset comprising 2 million transactions, resulting in a remarkable 35% increase in\n  revenue for the shipper’s new outbound facility locations.\n• Developed impactful dashboards and reports using Power BI and SQL for a hospitality company, enabling stakeholders to make\n  informed pricing decisions and contributing to a 20% year-over-year revenue increase. Implemented data modeling and KPIs,\n  leading to improvements in the average rating of the property.\nVetfab Technologies Pvt Ltd                                                                                           Bengaluru, India\nData Analyst                                                                                                      Feb 2018 - May 2019\n• Designed and implemented predictive models using Supervised Machine Learning in Python, eff           ectively resolving Shell India’s\n  financial discrepancies by meticulously analyzing two years of historical data. This initiative resulted in substantial cost and time\n  savings.\n• Conducted trend analysis to provide valuable support to distribution points and mid-scale manufacturers. This analysis empow-\n  ered them to better understand their data, manage inventory, and optimize product life cycles, leading to a remarkable 30%\n  increase in revenue.\n• Employed a multifaceted data analysis approach combining SQL and Python to scrutinize and interpret data from an educational\n  application. The communicated fi    ndings and insights directly contributed to a remarkable 25% increase in both downloads and\n  revenue for the application.\nGATE Indian Institute of Tutorials                                                                                    Bengaluru, India\nInstructor                                                                                                         Aug 2014 - Jan 2018\n• Inspired student interest and comprehension in probability, statistics, and engineering math, mentoring them for competitive\n  exams and university assessments. Implemented innovative teaching methods, earning positive student reviews.\nEDUCATION\n• San Francisco State University                                                                                     San Francisco, CA\n  Master’s in Statistical Data Science                                                                            Jan 2022 - May 2024\n• Visvesvaraya Technological University (VTU)                                                                        Bengaluru , India\n  Bachelors of Engineering, Electronics and Communication.                                                       Aug 2010 - June 2014\nACADEMIC PROJECTS\nEnd-to-End Text Summarization using Hugging Face Transformers | Github Link\n  Machine Learning | NLP | Python | Text Summarization | FastAPI | Docker| Streamlit\n• Utilized the system on the SAMSUN dataset to generate concise and informative document summaries.\n• Implemented the project using FastAPI for API integration, Docker for containerization, and Streamlit for a user-friendly interface.\nEnd-to-End Data Engineering Project - ETL Pipeline Automation | Github Link\n  AWS | Apache Airfl  ow | Python | ETL\n• Executed end-to-end automation, extracting OpenWeatherMap API data and loading into S3 using Apache Airfl           ow..\n• Proficient in AWS services, including IAM, EC2, S3, with expertise in Airflow concepts and ETL processes.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')"""
        client = openai.OpenAI(
        #     base_url = "https://api.fireworks.ai/inference/v1",
        #     api_key = fireworks_api_key,
            api_key = "sk-XXX",
        )
        # Not recommended to change the system prompt, 
        messages = [
            {"role": "system", "content": "You are a helpful assistant with access to functions."},
            {"role": "user", "content": "Please parse this resume:\n\n" + text},
        ]
        
        tools = [
            {
                "type": "function",
                "function": {
                    # name of the function 
                    "name": "parse_resume",
                    # a good, detailed description for what the function is supposed to do
                    "description": "Parses the resume.",
                    # a well defined json schema: https://json-schema.org/learn/getting-started-step-by-step#define
                    "parameters": {
                        # for OpenAI compatibility, we always declare a top level object for the parameters of the function
                        "type": "object",
                        # the properties for the object would be any arguments you want to provide to the function
                        "properties": {
                            "latest_job_title": {
                                "type": "string",
                                "description": "The latest job title.",
                            },
                            "company": {
                                "type": "string",
                                "description": "The last company.",
                            },
                            "job_experience": {
                                "type": "array",
                                "description": "List of professional working experiences.",
                                "items": {
                                    "type": "object",
                                    "description": "Individual job experience",
                                    "properties": {
                                        "company": {
                                            "description": "Name of company",
                                            "type": "string",
                                        },
                                        "title": {
                                            "type": "string",
                                            "description": "Title of job position",
                                        },
                                        "tenure": {
                                            "type": "string",
                                            "description": "Length at role: format this exactly as X years X months",
                                        },
                                    }
                                }
                            },
                            "years_of_experience": {
                                "type": "integer", 
                                # If the model does not understand how it is supposed to fill the field, a good description goes a long way 
                                "description": textwrap.dedent("""
                                Number of years of experience over all the paid positions.
                                Consider intern position as experience.
                                """),
                            },
                            "technical_skills_shown": {
                                "type": "array",
                                "description": textwrap.dedent("""
                                    The technical skills shown in the resume (such as Python, C++).
                                    NEVER include tools (Microsoft Word, VSCode).
                                    NEVER include soft skills (communication, presentation).
                                    This field could be empty if the position is not a technical position.
                                """.strip()),
                                "items": {
                                    "type": "string"
                                },
                            },
                            "education_history": {
                                "type": "array",
                                "description": "List of education history",
                                "items": {
                                    "type": "object",
                                    "description": "Individual education entry",
                                    "properties": {
                                        "education_qualification": {
                                            "type": "string",
                                            "description": textwrap.dedent("""
                                                The highest educational qualification,
                                                Should be either of High School, Bachelor's, Master's, PhD
                                            """
                                            ).strip()
                                        },
                                        "education_institution": {
                                            "type": "string",
                                            "description": textwrap.dedent("""
                                            The institution name of the highest educational qualification,
                                            """
                                        ).strip()
                                        },
                                        "duration": {
                                            "type": "string",
                                            "description": "Length at role: format this exactly as X years X months",
                                        },
                                    }
                                }
                            },                    
                            "highest_education_qualification": {
                                "type": "string",
                                "description": textwrap.dedent("""
                                    The highest educational qualification,
                                    This should be exactly either of High School, Bachelors, Masters, PhD
                                    """
                                ).strip()
                            },
                            "highest_education_institution": {
                                "type": "string",
                                "description": textwrap.dedent("""
                                    The institution name of the highest educational qualification,
                                    """
                                ).strip()
                            },
                            "was_ever_manager": {
                                "type": "string",
                                "description": "Whether the job requires managing reports.",
                            },
                        },
                        # You can specify which of the properties from above are required
                        # for more info on `required` field, please check https://json-schema.org/understanding-json-schema/reference/object#required
                        "required": ["latest_job_title", "job_experience", "technical_skills_required", "was_ever_manager"],
                    },
                },
            }
        ]
                chat_completion = client.chat.completions.create(
        #     model="accounts/fireworks/models/firefunction-v1",
            model="gpt-4-1106-preview",
            messages=messages,
            tools=tools,
            temperature=0.1
        )
        # print(chat_completion.choices[0].message.model_dump_json(indent=4))
        data=chat_completion.choices[0].message.tool_calls[0].function.arguments 
       query=(f"Job description has {data['years_of_experience']} years of experience, "
              f"these many technical skills: {data['technical_skills_shown']}, "
              f"and the highest qualification is {data['highest_education_qualification']}.")
        return query
