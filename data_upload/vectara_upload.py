import os

from bs4 import BeautifulSoup

from data_upload.JDMetadataExtractor import JDMetadataExtractor
from data_upload.VectaraClient import VectaraClient

INPUT_DIR = "../data_collection/resources"
VECTARA_CUSTOMER_ID = os.environ["VECTARA_CUSTOMER_ID"]
VECTARA_CORPUS_ID = os.environ["VECTARA_CORPUS_ID"]
VECTARA_API_KEY = os.environ["VECTARA_API_KEY"]

CHAT_ENDPOINT = os.environ["CHAT_ENDPOINT"]
CHAT_API_KEY = os.environ["CHAT_API_KEY"]
CHAT_MODEL = os.environ["CHAT_MODEL"]

def upload_jobs_to_vectara():
    jd_metadata_extractor = JDMetadataExtractor(CHAT_ENDPOINT, CHAT_API_KEY, CHAT_MODEL)
    vectara_client = VectaraClient(VECTARA_CUSTOMER_ID, VECTARA_CORPUS_ID, VECTARA_API_KEY)
    for file_name in os.listdir(INPUT_DIR):
        if ".html" not in file_name:
            continue
        with open(os.path.join(INPUT_DIR, file_name), 'r', encoding='utf-8') as file:
            job_id = file_name.strip(".html")
            text = BeautifulSoup(file.read()).get_text()
            metadata = jd_metadata_extractor.get_metadata(text)
            print(metadata)
            job_title = metadata["job_title"]
            document = vectara_client.construct_document(job_id, job_title, text, metadata)
            vectara_client.index_document(document)


if __name__ == "__main__":
    upload_jobs_to_vectara()
