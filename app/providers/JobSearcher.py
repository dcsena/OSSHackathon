from llama_index.indices.managed.vectara import VectaraIndex
from llama_index.indices.managed.vectara import VectaraAutoRetriever

from llama_index.core.vector_stores.types import MetadataInfo, VectorStoreInfo

from llama_index.llms.openai import OpenAI

TEMPERATURE = 0


class JobSearcher:
    def __init__(self, model_name):
        self.llm = OpenAI(model=model_name, temperature=TEMPERATURE)

    def get_relevant_jobs(self, resume_analysis):
        index = VectaraIndex()
        vector_store_info = VectorStoreInfo(
            content_info="information about a job",
            metadata_info=[
                MetadataInfo(
                    name="is_remote",
                    description="",
                    type="bool",
                )
            ],
        )

        retriever = VectaraAutoRetriever(
            index,
            vector_store_info=vector_store_info,
        )
        results = retriever.retrieve("jobs")
        return [{}]
