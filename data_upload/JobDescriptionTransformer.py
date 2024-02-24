import openai
import textwrap

CHAT_TOOLS = [
    {
        "type": "function",
        "function": {
            # name of the function
            "name": "index_job_opening",
            # a good, detailed description for what the function is supposed to do
            "description": "Index the job opening.",
            # a well defined json schema: https://json-schema.org/learn/getting-started-step-by-step#define
            "parameters": {
                # for OpenAI compatibility, we always declare a top level object for the parameters of the function
                "type": "object",
                # the properties for the object would be any arguments you want to provide to the function
                "properties": {
                    "company": {
                        "type": "string",
                        "description": "The company with the job opening."
                    },
                    "job_title": {
                        "type": "string",
                        "description": "The title of the job.",
                    },
                    "years_of_experience_required": {
                        "type": "integer", 
                        "description": "The minimum number of years of experience required for the role.",
                    },
                    "education_qualification_required": {
                        "type": "string",
                        "description": textwrap.dedent("""
                            The required educational qualification,
                            This should be exactly either of High School, Bachelors, Masters, PhD
                            """
                        ).strip(),
                    },
                    "technical_skills_required": {
                        "type": "array",
                        "description": textwrap.dedent("""
                            The technical skills required (such as Python, C++).
                            NEVER include tools (Microsoft Word, VSCode).
                            NEVER include soft skills (communication, presentation).
                            This field could be empty if the position is not a technical position.
                        """.strip()),
                        "items": {
                            "type": "string"
                        },
                    },
                    "is_remote": {
                        "type": "string",
                        "description": "Whether the job can be done completely remotely.",
                    },
                    "is_intern": {
                        "type": "string",
                        "description": "Whether the job opening is an intern position.",
                    },
                    "is_new_grad": {
                        "type": "string",
                        "description": "Whether the job is specified to be open to a graduate fresh out of college.",
                    },
                    "is_manager": {
                        "type": "string",
                        "description": "Whether the job requires managing reports.",
                    },
                },
                # You can specify which of the properties from above are required
                # for more info on `required` field, please check https://json-schema.org/understanding-json-schema/reference/object#required
                "required": ["is_remote", "years_of_experience_required", "company"],
            },
        },
    }
]


class JobDescriptionTransformer:
    def __init__(self, chat_endpoint, chat_api_key, model):
        self.client = openai.OpenAI(
            base_url=chat_endpoint,
            api_key=chat_api_key
        )
        self.model = model

    def transform(self, input_jd):
        # Not recommended to change the system prompt,
        messages = [
            {"role": "system", "content": "You are a helpful assistant with access to functions."},
            {"role": "user", "content": "Please index the following job opening:\n\n" + input_jd},
        ]

        chat_completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=CHAT_TOOLS,
            temperature=0.1
        )
        return chat_completion.choices[0].message.model_dump_json(indent=4)
