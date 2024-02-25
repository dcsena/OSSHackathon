# from llama_index.core.schema import TextNode
# from llama_index.core.indices.managed.types import ManagedIndexQueryMode
# from llama_index.indices.managed.vectara import VectaraIndex
# from llama_index.indices.managed.vectara import VectaraAutoRetriever
#
# from llama_index.core.vector_stores import MetadataInfo, VectorStoreInfo
#
# from llama_index.llms.openai import OpenAI

TEMPERATURE = 0

class JobSearcher:
    def __init__(self, model_name):
        # self.llm = OpenAI(model=model_name, temperature=0)
        pass

    def get_relevant_jobs(self, resume_analysis):
        # index = VectaraIndex()
        # vector_store_info = VectorStoreInfo(
        #     content_info="information about a movie",
        #     metadata_info=[
        #         MetadataInfo(
        #             name="genre",
        #             description="The genre of the movie. One of ['science fiction', 'comedy', 'drama', 'thriller', 'romance', 'action', 'animated']",
        #             type="string",
        #         ),
        #         MetadataInfo(
        #             name="year",
        #             description="The year the movie was released",
        #             type="integer",
        #         ),
        #         MetadataInfo(
        #             name="director",
        #             description="The name of the movie director",
        #             type="string",
        #         ),
        #         MetadataInfo(
        #             name="rating",
        #             description="A 1-10 rating for the movie",
        #             type="float",
        #         ),
        #     ],
        # )
        #
        # retriever = VectaraAutoRetriever(
        #     index,
        #     vector_store_info=vector_store_info,
        # )
        return [{}]
