import nest_asyncio
from llama_parse import LlamaParse
import openai
import textwrap

TOOLS = [
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


class ResumeAnalyzer:
    def __init__(self, model_api_key, model_name):
        self.client = openai.OpenAI(
            api_key=model_api_key,
        )
        self.model_name = model_name

    def analyze(self, resume_path):
        nest_asyncio.apply()
        documents = LlamaParse(result_type="text").load_data(resume_path)
        text = str(documents[0])
        # Not recommended to change the system prompt,
        messages = [
            {"role": "system", "content": "You are a helpful assistant with access to functions."},
            {"role": "user", "content": "Please parse this resume:\n\n" + text},
        ]

        chat_completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            tools=TOOLS,
            temperature=0.1)
        return chat_completion.choices[0].message.tool_calls[0].function.arguments